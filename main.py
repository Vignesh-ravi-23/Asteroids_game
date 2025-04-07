import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot


def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # initialize pygame

    pygame.init()

    # creating a screen (Window)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    global asteroids  # Make these global if needed elsewhere
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    updatable.add(player)
    drawable.add(player)
    shots = []


    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            shot = player.shoot()
            if shot:
                shots.append(shot)
    
        # fill the screen with black fcolor

        updatable.update(dt)

        for shot in shots:
            shot.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                pygame.quit()
                exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()

        shots = [s for s in shots if s.alive()]

        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        for shot in shots:
            shot.draw(screen)
        
        #update the display
        pygame.display.flip()




    pygame.quit()

if __name__ == "__main__":
    main()