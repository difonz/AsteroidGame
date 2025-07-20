import pygame
from constants import *
from player import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt=0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = Player(x,y)
    while True:
        screen.fill(color=00000)
        
        player1.draw(screen)
        
        pygame.display.flip()
        player1.update(dt)
        dt =  (clock.tick(60)/ 1000 )
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        
if __name__ == "__main__":
    main()
     