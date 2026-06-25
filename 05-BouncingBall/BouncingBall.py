import pygame
import sys
import random


class Ball:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.radius = random.randint(3, 30)
        self.x = random.randint(self.radius, screen.get_width() - self.radius)
        self.y = random.randint(self.radius, screen.get_height() - self.radius)
        self.speed_x = random.randint(-10, 10)
        self.speed_y = random.randint(-10, 10)
        while self.speed_y == 0 or self.speed_x == 0:
            self.speed_x = random.randint(-10, 10)
            self.speed_y = random.randint(-10, 10)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < self.radius or self.x + self.radius > self.screen.get_width():
            self.speed_x *= -1
        if self.y < self.radius or self.y + self.radius > self.screen.get_height():
            self.speed_y *= -1


def main():
    pygame.init()
    screen = pygame.display.set_mode((1300, 1300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    ball1 = Ball(screen)
    balls = []
    for k in range(1000):
        new_ball = Ball(screen)
        balls.append(new_ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # ball1.move()
        # ball1.draw()
        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()


main()
