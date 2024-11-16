import pygame, random


class Pipe:
    def __init__(self, x):
        self.img1 = pygame.image.load("imgs/pipe.png")
        self.img1 = pygame.transform.scale(self.img1, (50,300))
        self.img1_rect = self.img1.get_rect()

        self.img2 = pygame.image.load("imgs/pipe.png")
        self.img2 = pygame.transform.scale(self.img2, (50,300))
        self.img2 = pygame.transform.rotate(self.img2, -180)
        self.img2_rect = self.img2.get_rect()

        self.img1_rect.x = x
        self.img1_rect.y = random.randint(200,450)

        self.img2_rect.x = x
        self.img2_rect.y = self.img1_rect.y - 450
        self.pipesMoving = True
        self.stopMovement = False
        self.stopMusic = True

    def detect_collision(self, player):
        if self.img1_rect.colliderect(player) or self.img2_rect.colliderect(player):
            return True
        return False
        
    def update(self, screen):
            
        if self.img1_rect.x <= -50:
            self.img1_rect.x = 600
            self.img1_rect.y = random.randint(200,450)
        if self.img2_rect.x <= -50:
            self.img2_rect.x = 600
            self.img2_rect.y = self.img1_rect.y - 450


        screen.blit(self.img1, self.img1_rect)
        screen.blit(self.img2, self.img2_rect)

        if self.pipesMoving:
            self.img1_rect.x -= 3
            self.img2_rect.x -= 3