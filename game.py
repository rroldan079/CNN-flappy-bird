import pygame, sys
from pipe import Pipe
from player import Player


WHITE = (255,255,255)
screen = pygame.display.set_mode((600,600))
icon = pygame.image.load("imgs/bird1.png")

pygame.init()
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(icon)


score = 0
bird = Player()
bird2 = Player()
bird3 = Player()
text = pygame.font.SysFont("Arial", 24, True)
score_board = text.render(str(score), "black", True)


position = 650
pipes = [Pipe(position), Pipe(position + 150), Pipe(position + 300), Pipe(position + 450)]


background = pygame.image.load("imgs/bg.png").convert_alpha()
background = pygame.transform.scale(background, (600,600))


restart_button = pygame.Surface((100,50))
restart_button.fill((0,0,0))


clock = pygame.time.Clock()

pipe_movement = False
START = False
COLLIDE = False
while True:
    screen.fill(WHITE)
    screen.blit(background, (0,0))

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if events.type == pygame.KEYDOWN and bird.isRunning:
            if events.key == pygame.K_SPACE:
                START = True
                bird.isJumping = True 

    if pipe_movement:
        for pipe in pipes:
            pipe.update(screen)
            if bird.img_rect.x >= pipe.img1_rect.x - 1 and bird.img_rect.x <= pipe.img1_rect.x + 1:
                score += 1
                score_board = text.render(str(score), (0,0,0), True)
            if pipe.detect_collision(bird.img_rect):
                COLLIDE = True

           

    if START:
        bird.gravity = 1
        pipe_movement = True
    
    if COLLIDE:
        screen.blit(restart_button, (260,250))
        for pipe in pipes:
            bird.isJumping = False
            bird.isRunning = False
            pipe.stopMovement = True
            pipe.pipesMoving = False
            START = False
        
    
    bird.update(screen)
    screen.blit(score_board, (300, 200))
    clock.tick(30)
    pygame.display.flip()
    pygame.display.update()
        