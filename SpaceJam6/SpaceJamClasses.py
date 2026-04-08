from direct.showbase.ShowBase import ShowBase
from panda3d.core import Loader, NodePath, Vec3, TransparencyAttrib, CollisionHandlerEvent
from direct.interval.LerpInterval import LerpFunc
from direct.particles.ParticleEffect import ParticleEffect
import re
import random
from direct.gui.OnscreenImage import OnscreenImage
from direct.task import Task
from CollideObjectBase import *


class Planet(SphereCollideObj):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec, scaleVec: float):
        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, posVec, 1)

        self.model.setPos(posVec)
        self.model.setScale(scaleVec)

        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
        self.model.setTag("type", "Planet")

        speed = random.uniform(10, 40)
        self.model.hprInterval(speed, Vec3(360, 0, 0)).loop()


class Drone(SphereCollideObj):

    droneCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec, scaleVec: float):
        super(Drone, self).__init__(loader, modelPath, parentNode, nodeName, posVec, 1)
        
        Drone.droneCount += 1


        self.model.setPos(posVec)
        self.model.setScale(scaleVec)

        self.model.setName(f"{nodeName}_{Drone.droneCount}")
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
        self.model.setTag("type", "Drone")


class Universe(InverseSphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, scaleVal: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), scaleVal * 0.95)
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)

        self.model.setScale(scaleVal)
        self.model.setTwoSided(True)
        self.model.setLightOff()

        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)


class SpaceStation(CapsuleCollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec, scaleVec: float, hprVec):
        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName, -4, -1, 5, -4, -1, -5, 16)

        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        self.model.setHpr(hprVec)

        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
        self.model.setTag("type", "Space Station")
        self.model.hprInterval(100, Vec3(0, 0, 360)).loop()


class SpaceShip(SphereCollideObj):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec, scaleVec: float, hprVec, traverser):
        super(SpaceShip, self).__init__(loader, modelPath, parentNode, nodeName, posVec, 3)

        self.model.setPos(posVec)
        self.model.setScale(scaleVec)


        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)

        self.reloadTime = .25
        self.missileDistance = 4000
        self.missileBay = 1
        taskMgr.add(self.CheckIntervals, 'checkMissiles', 34)
        self.EnableHUD()
        self.SetParticles()
        self.cntExplode = 0
        self.explodeIntervals = {}

        self.traverser = traverser

        self.handler = CollisionHandlerEvent()

        self.handler.addInPattern('into')
        base.accept('into', self.HandleInto)

        self.isBoosting = False
        self.canBoost = True
        self.boostSpeed = 20
        self.normalSpeed = 5
        self.boostDuration = 2
        self.boostCooldown = 5

    def setKeyBindings(self):
        base.accept('space', self.Thrust, [1])
        base.accept('space-up', self.Thrust, [0])

        base.accept('r', self.ReverseThrust, [1])
        base.accept('r-up', self.ReverseThrust, [0])

        base.accept('a', self.LeftTurn, [1])
        base.accept('a-up', self.LeftTurn, [0])

        base.accept('d', self.RightTurn, [1])
        base.accept('d-up', self.RightTurn, [0])

        base.accept('w', self.LookUp, [1])
        base.accept('w-up', self.LookUp, [0])

        base.accept('s', self.LookDown, [1])
        base.accept('s-up', self.LookDown, [0])

        base.accept('q', self.RollLeft, [1])
        base.accept('q-up', self.RollLeft, [0])

        base.accept('e', self.RollRight, [1])
        base.accept('e-up', self.RollRight, [0])

        base.accept('f', self.Fire)

        base.accept('shift', self.StartBoost)

    def Thrust(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyThrust, 'forward-thrust')
        else:
            taskMgr.remove('forward-thrust')

    def ApplyThrust(self, task):
        rate = 5

        trajectory = render.getRelativeVector(self.model, Vec3(0, 1, 0))
        trajectory.normalize()

        self.model.setFluidPos(self.model.getPos() + trajectory * rate)

        return Task.cont
    
    def ReverseThrust(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyReverseThrust, 'backward-thrust')
        else:
            taskMgr.remove('backward-thrust')

    def ApplyReverseThrust(self, task):
        rate = 5

        trajectory = render.getRelativeVector(self.model, Vec3(0, -1, 0))
        trajectory.normalize()

        self.model.setFluidPos(self.model.getPos() + trajectory * rate)

        return Task.cont
    
    def LeftTurn(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyLeftTurn, 'left-turn')

        else:
            taskMgr.remove('left-turn')
        
    def ApplyLeftTurn(self, task):
        if self.isBoosting:
            return Task.cont
        rate = .5

        self.model.setH(self.model, 0.5)
        return Task.cont
    
    def RightTurn(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyRightTurn, 'right-turn')
        else:
            taskMgr.remove('right-turn')

    def ApplyRightTurn(self, task):
        if self.isBoosting:
            return Task.cont
        rate = .5

        self.model.setH(self.model, -0.5)
        return Task.cont
    
    def LookUp(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyLookUp, 'look-up')
        else:
            taskMgr.remove('look-up')

    def ApplyLookUp(self, task):
        if self.isBoosting:
            return Task.cont
        rate = .5

        self.model.setP(self.model, 0.5)
        return Task.cont
    
    def LookDown(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyLookDown, 'look-down')
        else:
            taskMgr.remove('look-down')

    def ApplyLookDown(self, task):
        if self.isBoosting:
            return Task.cont
        rate = .5

        self.model.setP(self.model, -0.5)
        return Task.cont
    
    def RollLeft(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyRollLeft, 'roll-left')
        else:
            taskMgr.remove('roll-left')

    def ApplyRollLeft(self, task):
        rate = .5

        self.model.setR(self.model, -0.5)
        return Task.cont
    
    def RollRight(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyRollRight, 'roll-right')
        else:
            taskMgr.remove('roll-right')

    def ApplyRollRight(self, task):
        rate = .5

        self.model.setR(self.model, 0.5)
        return Task.cont
    
    def Fire(self):
        if self.missileBay:
            travRate = self.missileDistance
            aim = render.getRelativeVector(self.model, Vec3.forward())
            aim.normalize()
            fireSolution = aim * travRate
            inFront = aim * 150
            travVec = fireSolution + self.model.getPos()
            self.missileBay -= 1
            tag = 'Missile' + str(Missile.missileCount)
            posVec = self.model.getPos() + inFront
            currentMissile = Missile(loader, './Assets/Phaser/phaser.egg', render, tag, posVec, 4.0)

            self.traverser.addCollider(currentMissile.collisionNode, self.handler)

            Missile.Intervals[tag] = currentMissile.model.posInterval(2.0, travVec, startPos = posVec, fluid = 1)
            Missile.Intervals[tag].start()
        else:
            if not taskMgr.hasTaskNamed('reload'):
                print('Initializing reload...')

                taskMgr.doMethodLater(0, self.Reload, 'reload')
                return Task.cont
            
    def Reload(self, task):
        if task.time > self.reloadTime:
            self.missileBay += 1
        if self.missileBay > 1:
            self.missileBay = 1
            print("Reload complete.")
            Task.done
        elif task.time <= self.reloadTime:
            print("Reload proceeding...")
            return Task.cont
    
    def CheckIntervals(self, task):
        for i in Missile.Intervals:
            if not Missile.Intervals[i].isPlaying():
                Missile.cNodes[i].detachNode()
                Missile.fireModels[i].detachNode()
                del Missile.Intervals[i]
                del Missile.fireModels[i]
                del Missile.cNodes[i]
                del Missile.CollisionSolids[i]
                print(i + ' has reached the end of its fire solution.')
                break
        return Task.cont
    
    def EnableHUD(self):
        self.Hud = OnscreenImage(image = "./Assets/Hud/Reticle3b.png", pos = Vec3(0, 0, 0), scale = 0.1)
        self.Hud.setTransparency(TransparencyAttrib.MAlpha)

    def HandleInto(self, entry):
        fromNode = entry.getFromNodePath().getName()
        print("fromNode: " + fromNode)
        intoNode = entry.getIntoNodePath().getName()
        print("intoNode: " + intoNode)

        intoPosition = Vec3(entry.getSurfacePoint(render))

        tempVar = fromNode.split('_')
        print("tempVar: " + str(tempVar))
        shooter = tempVar[0]
        print("Shooter: " + str(shooter))
        tempVar = intoNode.split('-')
        print("TempVar1: " + str(tempVar))
        tempVar = intoNode.split('_')
        print("TempVar2: " + str(tempVar))
        victim = tempVar[0]
        print("Victim: " + str(victim))

        intoNP = entry.getIntoNodePath()
        objType = intoNP.getNetTag("type")

        if objType in ["Drone", "Planet", "Space Station"]:
            print(victim, ' hit at ', intoPosition)
            intoNP = entry.getIntoNodePath()
            self.DestroyObject(intoNP, intoPosition)

        print(shooter + ' is DONE.')
        if shooter in Missile.Intervals:
            Missile.Intervals[shooter].finish()

    def DestroyObject(self, nodePath, hitPosition):
        root = nodePath

        while root.getParent() != render:
            root = root.getParent()

        root.detachNode()

        self.explodeNode.setPos(hitPosition)
        self.Explode()

    def Explode(self):
        self.cntExplode += 1
        tag = 'particles-' + str(self.cntExplode)

        self.explodeIntervals[tag] = LerpFunc(self.ExplodeLight, duration = 4.0)
        self.explodeIntervals[tag].start()

    def ExplodeLight(self, t):
        if t == 1.0 and self.explodeEffect:
            self.explodeEffect.disable()

        elif t <= 0.01:
            self.explodeEffect.start(self.explodeNode)

    def SetParticles(self):
        base.enableParticles()
        self.explodeEffect = ParticleEffect()
        self.explodeEffect.loadConfig("./Assets/Part-Fx/Part-Efx/basic_xpld_efx.ptf")
        self.explodeEffect.setScale(20)
        self.explodeNode = render.attachNewNode('ExplosionEffects')

    def StartBoost(self):
        if self.canBoost and not self.isBoosting:
            self.isBoosting = True
            self.canBoost = False

            taskMgr.add(self.ApplyBoost, 'boost')

            taskMgr.doMethodLater(self.boostDuration, self.StopBoost, 'stop-boost')


    def StopBoost(self, task):
        self.isBoosting = False
        taskMgr.remove('boost')

        taskMgr.doMethodLater(self.boostCooldown, self.ResetBoost, 'reset-boost')
        return Task.done


    def ResetBoost(self, task):
        self.canBoost = True
        print("Boost ready")
        return Task.done

    def ApplyBoost(self, task):
        trajectory = render.getRelativeVector(self.model, Vec3(0, 1, 0))
        trajectory.normalize()

        self.model.setFluidPos(self.model.getPos() + trajectory * self.boostSpeed)

        return Task.cont

class Missile(SphereCollideObj):
    fireModels = {}
    cNodes = {}
    CollisionSolids = {}
    Intervals = {}

    missileCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float = 1.0):
        super(Missile, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1.0)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)

        Missile.missileCount += 1
        Missile.fireModels[nodeName] = self.model
        Missile.cNodes[nodeName] = self.collisionNode
        Missile.CollisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
        Missile.cNodes[nodeName].show()
        print("Fire torpedo #" + str(Missile.missileCount))





