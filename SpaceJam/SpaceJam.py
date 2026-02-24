from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)


        self.camera.setPos(0, -10000, 0)

        self.SetupScene()

    def SetupScene(self):
        # Universe Section
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(17000)
        self.Universe.setTwoSided(True)
        self.Universe.setLightOff()

        universeTex = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        
        self.Universe.setTexture(universeTex, 1)

        # Planet 1 Section
        self.earthPlanet = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.earthPlanet.reparentTo(self.render)
        self.earthPlanet.setPos(-3000, 14500, 3000)
        self.earthPlanet.setScale(350)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Earth.png")
        self.earthPlanet.setTexture(planetTex, 1)

        # Planet 2 Section
        self.sherbertPlanet = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.sherbertPlanet.reparentTo(self.render)
        self.sherbertPlanet.setPos(-2000, 5000, 500)
        self.sherbertPlanet.setScale(550)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Sherbert.png")
        self.sherbertPlanet.setTexture(planetTex, 1)

        # Planet 3 Section
        self.lavaPlanet = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.lavaPlanet.reparentTo(self.render)
        self.lavaPlanet.setPos(3000, 14500, 3000)
        self.lavaPlanet.setScale(250)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Lava.jpg")
        self.lavaPlanet.setTexture(planetTex, 1)

        # Planet 4 Section
        self.neptunePlanet = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.neptunePlanet.reparentTo(self.render)
        self.neptunePlanet.setPos(-2300, 15000, 2000)
        self.neptunePlanet.setScale(400)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Neptune.jpg")
        self.neptunePlanet.setTexture(planetTex, 1)

        # Planet 5 Section
        self.jupiterPlanet = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.jupiterPlanet.reparentTo(self.render)
        self.jupiterPlanet.setPos(-2500, 13000, -1000)
        self.jupiterPlanet.setScale(300)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Jupiter.jpg")
        self.jupiterPlanet.setTexture(planetTex, 1)

        # Planet 6 Section
        self.marsPlanet = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.marsPlanet.reparentTo(self.render)
        self.marsPlanet.setPos(2500, 12000, 0)
        self.marsPlanet.setScale(600)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Mars.jpg")
        self.marsPlanet.setTexture(planetTex, 1)
        # Space Station Section
        self.SpaceStation = self.loader.loadModel("./Assets/Space Station/SpaceStation1B/SpaceStation1B/spaceStation.x")
        self.SpaceStation.reparentTo(self.render)
        self.SpaceStation.setPos(0, 13000, 1500)
        self.SpaceStation.setScale(200)
        self.SpaceStation.setHpr(-180, 60, 50)

        stationTex = self.loader.loadTexture("./Assets/Space Station/SpaceStation1B/SpaceStation1B/SpaceStation1_Dif2.png")
        stationTex = self.loader.loadTexture("./Assets/Space Station/SpaceStation1B/SpaceStation1B/SpaceStation1_NM.png")
        self.SpaceStation.setTexture(stationTex, 1)

        # Space Ship Section
        self.SpaceShip = self.loader.loadModel("./Assets/SpaceShips/Dumbledore/Dumbledore/Dumbledore.x")
        self.SpaceShip.reparentTo(self.render)
        self.SpaceShip.setPos(0, 400, -70)
        self.SpaceShip.setScale(30)
        self.SpaceShip.setHpr(0, 90, 0)

        shipTex = self.loader.loadTexture("./Assets/SpaceShips/Dumbledore/Dumbledore/spacejet_C.png")
        shipTex = self.loader.loadTexture("./Assets/SpaceShips/Dumbledore/Dumbledore/spacejet_N.png")
        self.SpaceShip.setTexture(shipTex, 1)

app = MyApp()
app.run()