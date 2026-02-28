from direct.showbase.ShowBase import ShowBase
from panda3d.core import Loader, NodePath, Vec3
from direct.task import Task



class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)

        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)


class Drone(ShowBase):

    droneCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec, scaleVec: float):
        Drone.droneCount += 1

        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)

        self.model.setName(f"{nodeName}_{Drone.droneCount}")
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)


class Universe(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, scaleVal: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setScale(scaleVal)
        self.model.setTwoSided(True)
        self.model.setLightOff()

        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)


class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec, scaleVec: float, hprVec):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        self.model.setHpr(hprVec)

        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)


class SpaceShip(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec, scaleVec: float, hprVec):

        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)


        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)

    def setKeyBindings(self):
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])

        self.accept('r', self.ReverseThrust, [1])
        self.accept('r-up', self.ReverseThrust, [0])

        self.accept('a', self.LeftTurn, [1])
        self.accept('a-up', self.LeftTurn, [0])

        self.accept('d', self.RightTurn, [1])
        self.accept('d-up', self.RightTurn, [0])

        self.accept('w', self.LookUp, [1])
        self.accept('w-up', self.LookUp, [0])

        self.accept('s', self.LookDown, [1])
        self.accept('s-up', self.LookDown, [0])

        self.accept('q', self.RollLeft, [1])
        self.accept('q-up', self.RollLeft, [0])

        self.accept('e', self.RollRight, [1])
        self.accept('e-up', self.RollRight, [0])

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
        rate = .5

        self.model.setH(self.model, 0.5)
        return Task.cont
    
    def RightTurn(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyRightTurn, 'right-turn')
        else:
            taskMgr.remove('right-turn')

    def ApplyRightTurn(self, task):
        rate = .5

        self.model.setH(self.model, -0.5)
        return Task.cont
    
    def LookUp(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyLookUp, 'look-up')
        else:
            taskMgr.remove('look-up')

    def ApplyLookUp(self, task):
        rate = .5

        self.model.setP(self.model, 0.5)
        return Task.cont
    
    def LookDown(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyLookDown, 'look-down')
        else:
            taskMgr.remove('look-down')

    def ApplyLookDown(self, task):
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
