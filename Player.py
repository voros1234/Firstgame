class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win, walkRight, walkLeft, char):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (round(self.x), round(self.y)))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (round(self.x), round(self.y)))
            self.walkCount += 1
        else:
            win.blit(char, (round(self.x), round(self.y)))    