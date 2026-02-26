from direct.showbase.ShowBase import ShowBase
import SpaceJamClasses as spaceJamClasses
import DefensePaths as defensePaths
import math

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()

    def SetupScene(self):
  
        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, "Universe", "./Assets/Universe/Universe.jpg", 17000)
        self.earthPlanet = spaceJamClasses.Planet(self.loader, "./Assets/Universe/protoPlanet.x", self.render, "Earth", "./Assets/Planets/Earth.png", (-3000, 14500, 3000), 350)
        self.sherbertPlanet = spaceJamClasses.Planet(self.loader, "./Assets/Universe/protoPlanet.x", self.render, "Sherbert", "./Assets/Planets/Sherbert.png", (-2000, 5000, 500), 550)
        self.lavaPlanet = spaceJamClasses.Planet(self.loader, "./Assets/Universe/protoPlanet.x", self.render, "Lava", "./Assets/Planets/Lava.jpg", (3000, 14500, 3000), 250)
        self.neptunePlanet = spaceJamClasses.Planet(self.loader, "./Assets/Universe/protoPlanet.x", self.render, "Neptune", "./Assets/Planets/Neptune.jpg", (-2300, 15000, 2000), 400)
        self.jupiterPlanet = spaceJamClasses.Planet(self.loader, "./Assets/Universe/protoPlanet.x", self.render, "Jupiter", "./Assets/Planets/Jupiter.jpg", (-2500, 13000, -1000), 300)
        self.marsPlanet = spaceJamClasses.Planet(self.loader, "./Assets/Universe/protoPlanet.x", self.render, "Mars", "./Assets/Planets/Mars.jpg", (2500, 12000, 0), 600)
        self.SpaceStation = spaceJamClasses.SpaceStation(self.loader, "./Assets/Space Station/SpaceStation1B/SpaceStation1B/spaceStation.x", self.render, "SpaceStation", "./Assets/Space Station/SpaceStation1B/SpaceStation1B/SpaceStation1_NM.png", (0, 13000, 1500), 100, (-180, 60, 50))
        self.SpaceShip = spaceJamClasses.SpaceShip(self.loader, "./Assets/SpaceShips/Dumbledore/Dumbledore/Dumbledore.x", self.render, "SpaceShip", "./Assets/SpaceShips/Dumbledore/Dumbledore/spacejet_N.png", (0, 400, -70), 30, (0, 90, 0))
        fullCycle = 60

        for j in range(fullCycle):

            spaceJamClasses.Drone.droneCount += 1

            t = (j / fullCycle) * 2 * math.pi

            earthName = f"EarthDrone{spaceJamClasses.Drone.droneCount}"
            stationName = f"StationDrone{spaceJamClasses.Drone.droneCount}"
            sherbertName = "SherbertXDrone" + str(spaceJamClasses.Drone.droneCount)
            marsName = "MarsYDrone" + str(spaceJamClasses.Drone.droneCount)
            jupiterName = "JupiterZDrone" + str(spaceJamClasses.Drone.droneCount)

            self.DrawCloudDefense(self.earthPlanet, earthName)
            self.DrawBaseballSeams(self.SpaceStation, stationName, j, fullCycle, 2)
            self.DrawCircleX(self.sherbertPlanet, sherbertName, 600, t)
            self.DrawCircleY(self.marsPlanet, marsName, 600, t)
            self.DrawCircleZ(self.jupiterPlanet, jupiterName, 600, t)
        


 
    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.model.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.model.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/DroneDefender/octotoad1_auv.png", position, 10)

    def DrawCircleX(self, centralObject, droneName, radius, t):
        unitVec = defensePaths.CircleX(radius, t)
        position = unitVec + centralObject.model.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCircleY(self, centralObject, droneName, radius, t):
        unitVec = defensePaths.CircleY(radius, t)
        position = unitVec + centralObject.model.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCircleZ(self, centralObject, droneName, radius, t):
        unitVec = defensePaths.CircleZ(radius, t)
        position = unitVec + centralObject.model.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/DroneDefender/octotoad1_auv.png", position, 5)

app = MyApp()
app.run()