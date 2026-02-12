from direct.showbase.ShowBase import ShowBase
import math, sys, random
from panda3d.core import CollisionTraverser, CollisionHandlerPusher
from panda3d.core import CollisionNode, CollisionSphere

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.cTrav = CollisionTraverser()
        self.pusher = CollisionHandlerPusher()

        self.fighter = self.loader.loadModel('./Assets/sphere')
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0, 0.0, 0.0, 1.0)

        self.playerCNode = CollisionNode('player')
        self.playerCNode.addSolid(CollisionSphere(0, 0, 0, 1.5))
        self.playerCNodePath = self.fighter.attachNewNode(self.playerCNode)
        self.playerCNodePath.show()

        self.pusher.addCollider(self.playerCNodePath, self.fighter)
        self.cTrav.addCollider(self.playerCNodePath, self.pusher)
        self.accept('escape', self.quit)

        self.parent = self.loader.loadModel('./Assets/cube')

        x = 0
        for i in range(100):
            theta = x
            placeholder = self.render.attachNewNode('Placeholder')

            placeholder.setPos(
                50.0 * math.cos(theta),
                50.0 * math.sin(theta),
                0.0 * math.tan(theta)
            )

            red = 0.6 + random.random() * 0.4
            green = 0.6 + random.random() * 0.4
            blue = 0.6 + random.random() * 0.4
            placeholder.setColorScale(red, green, blue, 1.0)

            self.parent.instanceTo(placeholder)


            cubeCNode = CollisionNode('cube')
            cubeCNode.addSolid(CollisionSphere(0, 0, 0, 1.5))

            cubeCNodePath = placeholder.attachNewNode(cubeCNode)
            cubeCNodePath.show()


            x += 0.06


        self.cTrav.showCollisions(self.render)


        base.disableMouse()

        base.camera.setPos(0.0, 0.0, 250.0)
        base.camera.setHpr(0.0, -90.0, 0.0)

        self.accept('arrow_left', self.negativeX, [1])
        self.accept('arrow_left-up', self.negativeX, [0])

        self.accept('arrow_right', self.positiveX, [1])
        self.accept('arrow_right-up', self.positiveX, [0])

        self.accept('arrow_up', self.positiveY, [1])
        self.accept('arrow_up-up', self.positiveY, [0])

        self.accept('arrow_down', self.negativeY, [1])
        self.accept('arrow_down-up', self.negativeY, [0])

    def negativeX(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.moveNegativeX, 'moveNegativeX')
        else:
            self.taskMgr.remove('moveNegativeX')

    def moveNegativeX(self, task):
        self.fighter.setX(self.fighter, -1)
        return task.cont

    def positiveX(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.movePositiveX, 'movePositiveX')
        else:
            self.taskMgr.remove('movePositiveX')

    def movePositiveX(self, task):
        self.fighter.setX(self.fighter, 1)
        return task.cont

    def negativeY(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.moveNegativeY, 'moveNegativeY')
        else:
            self.taskMgr.remove('moveNegativeY')

    def moveNegativeY(self, task):
        self.fighter.setY(self.fighter, -1)
        return task.cont

    def positiveY(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.movePositiveY, 'movePositiveY')
        else:
            self.taskMgr.remove('movePositiveY')

    def movePositiveY(self, task):
        self.fighter.setY(self.fighter, 1)
        return task.cont

    def quit(self):
        sys.exit()


app = MyApp()
app.run()