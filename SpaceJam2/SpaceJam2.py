from direct.showbase.ShowBase import ShowBase
import SpaceJamClasses as spaceJamClasses
import DefensePaths as defensePaths

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
        self.SpaceStation = spaceJamClasses.SpaceStation(self.loader, "./Assets/Space Station/SpaceStation1B/SpaceStation1B/spaceStation.x", self.render, "SpaceStation", "./Assets/Space Station/SpaceStation1B/SpaceStation1B/SpaceStation1_NM.png", (0, 13000, 1500), 200, (-180, 60, 50))
        self.SpaceShip = spaceJamClasses.SpaceShip(self.loader, "./Assets/SpaceShips/Dumbledore/Dumbledore/Dumbledore.x", self.render, "SpaceShip", "./Assets/SpaceShips/Dumbledore/Dumbledore/spacejet_N.png", (0, 400, -70), 30, (0, 90, 0))

app = MyApp()
app.run()