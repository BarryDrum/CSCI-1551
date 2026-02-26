from direct.showbase.ShowBase import ShowBase
from panda3d.core import Loader, NodePath
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
        self.model.setHpr(hprVec)

        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
    
    def Thrust(self, keyDown):
        if keyDown:
            taskMgr.add(self.ApplyThrust, "forward-thrust")
        else:
            taskMgr.remove("forward-thrust")
