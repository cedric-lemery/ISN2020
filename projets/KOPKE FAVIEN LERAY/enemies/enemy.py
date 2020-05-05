import pygame


class Enemy:
    imgs = []


    def __init__(self, x, y, width, height,vitx,vity):
        self.x = x
        self.y = y
        self.vitx = vitx
        self.vity = vity
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.chemin = []
        self.img = None

    def draw(self, win):
        self.animation_count +=1
        self.img = pygame.image.load(os.path.join("assets", self.imgs[self.animation_count]))
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        win.blit(self.img,(self.x,self.y))
        self.mouvement()

    def collision(self, X, Y):
        if X < self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    
    def mouvement(self) :
        self.x+=self.vitx
        self.y+=self.vity

    def hit(self):
        self.health -=1
        if self.health <= 0:
            return True