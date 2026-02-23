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
        self.Universe.setScale(15000)
        self.Universe.setTwoSided(True)
        self.Universe.setLightOff()

        universeTex = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        
        self.Universe.setTexture(universeTex, 1)

        # Planet 1 Section
        self.Planet1 = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(-3000, 14500, 3000)
        self.Planet1.setScale(350)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Earth.png")
        self.Planet1.setTexture(planetTex, 1)

        # Planet 2 Section
        self.Planet2 = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(-2000, 5000, 500)
        self.Planet2.setScale(550)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Sherbert.png")
        self.Planet2.setTexture(planetTex, 1)

        # Planet 3 Section
        self.Planet3 = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(3000, 14500, 3000)
        self.Planet3.setScale(250)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Lava.jpg")
        self.Planet3.setTexture(planetTex, 1)

        # Planet 4 Section
        self.Planet4 = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(-2300, 15000, 2000)
        self.Planet4.setScale(400)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Neptune.jpg")
        self.Planet4.setTexture(planetTex, 1)

        # Planet 5 Section
        self.Planet5 = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(-2500, 13000, -1000)
        self.Planet5.setScale(300)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Jupiter.jpg")
        self.Planet5.setTexture(planetTex, 1)

        # Planet 6 Section
        self.Planet6 = self.loader.loadModel("./Assets/Universe/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(2500, 12000, 0)
        self.Planet6.setScale(600)
        
        planetTex = self.loader.loadTexture("./Assets/Universe/sphere1_auv.jpg")
        planetTex = self.loader.loadTexture("./Assets/Planets/Mars.jpg")
        self.Planet6.setTexture(planetTex, 1)
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