"""
platformer.py
Author: Robbie
Credit: Matt
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# THIS IS BOXY
class Boxy(Sprite):
    Black=Color(0,1)
    oline= LineStyle(0, Black)
    blue=Color(0x0000ff, 1.0)
    asset= RectangleAsset(25, 50, oline, blue)
    
    def __init__(self, position):
        super().__init__(Boxy.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0.25
        Platformer.listenKeyEvent("keydown", "d", self.MoveRIGHT)
        Platformer.listenKeyEvent("keyup", "d", self.MoveOff)
        Platformer.listenKeyEvent("keydown", "a", self.MoveLEFT)
        Platformer.listenKeyEvent("keyup", "a", self.MoveOff)
      
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
    def MoveRIGHT(self, event):
        self.vx = 5
    
    def MoveLEFT(self, event):
        self.vx = -5
        
    def MoveOff(self, event):
        self.vx = 0
        
        # MAKE A WALL
class Wall(Sprite):
    Black = Color(0,1)
    noline = LineStyle(0, Black)
    asset = RectangleAsset(25, 25, noline, Black)
    
    def __init__(self, position):
        super().__init__(Wall.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0

            

       
    #THIS IS BOXY'S WORLD
class Platformer(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        black=Color(1, 0)
        Black=Color(0, 1)
        blue=Color(0x0000ff, 1.0)
        noline=LineStyle(5, Black)
        Noline=LineStyle(0, Black)
        bg_asset=RectangleAsset(width, height, noline, black)
        Platformer.listenKeyEvent("keydown", "w", self.Wall)
        Platformer.listenMouseEvent("mousemove" , self.mousemove)
        bg=Sprite(bg_asset, (0, 0))
        Boxy((100, 100))
        self.x= 0
        self.y = 0
    
    def step(self):
        for ship in self.getSpritesbyClass(Boxy):
            ship.step()
    
    def mousemove(self, event):
        self.x = event.x
        self.y = event.y
        
    def Wall(self, event):
        Wall((self.x, self.y))
       
    
myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()