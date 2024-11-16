import pygame, time


class Player:
    def __init__(self):
        self.img1 = pygame.image.load("imgs/bird1.png")
        self.img2 = pygame.image.load("imgs/bird2.png")
        self.img3 = pygame.image.load("imgs/bird3.png")
        self.img = [self.img1, self.img2, self.img3]  
        

        
        self.ground = pygame.image.load("imgs/base.png")
        self.ground = pygame.transform.scale(self.ground, (600,100))
        self.ground_rect = self.ground.get_rect()
        self.ground_rect.x = 0
        self.ground_rect.y = 500

        self.ground2 = pygame.image.load("imgs/base.png")
        self.ground2 = pygame.transform.scale(self.ground, (600,100))
        self.ground_rect2 = self.ground.get_rect()
        self.ground_rect2.x = 600
        self.ground_rect2.y = 500
        
        self.img_rect = self.img1.get_rect()
        self.img_rect.x = 300
        self.img_rect.y = 300
        self.start_time = time.time()
        self.current_time = time.time()
        self.i = 0

        self.gravity = 0
        self.velocity = 0
        self.isJumping = False
        self.isRunning = True

    def jump_sound(self):
        pygame.mixer.music.load('imgs/toy-button-105724.mp3')
        pygame.mixer.music.play(0)
    
    def crash_sound(self):
        pygame.mixer.music.load('imgs/mixkit-dramatic-metal-explosion-impact-1687.mp3')
        pygame.mixer.music.play(5)
        self.stopMusic = False

    def jump(self):
        self.velocity = 10
        self.jump_sound()
    
    def update(self, screen):
        if self.isRunning:
            if self.current_time - self.start_time >= 0.25:
                self.i+=1
                self.start_time = time.time()

            if self.i > 2:
                self.i = 0

            
            if self.ground_rect.x <= -600:
                self.ground_rect.x = 600
                
            if self.ground_rect2.x <= -600:
                self.ground_rect2.x = 600

            self.ground_rect.x -=3
            self.ground_rect2.x -=3


        if self.isJumping:
            self.jump()
            self.isJumping = False

        if self.img_rect.y >= 470:
            self.velocity = 0
            self.gravity = 0
            self.isRunning = False
            #self.crash_sound()

        self.img_rect.y -= self.velocity
        self.velocity -= self.gravity

        screen.blit(self.img[self.i], self.img_rect)
        screen.blit(self.ground, self.ground_rect)
        screen.blit(self.ground2, self.ground_rect2)
        self.current_time = time.time()