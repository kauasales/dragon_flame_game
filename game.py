import pygame
import time
from config import *
from dragon import *
from shield import *

pygame.init()
clock = pygame.time.Clock()

# Joystick settings
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

# Draw sprites
Dragon.draw_dragons(blue_dragon, blue_d, initial_bd_x_pos, initial_d_y_pos, dragon_speed, blue_angle)
Dragon.draw_dragons(green_dragon, green_d, initial_gd_x_pos, initial_d_y_pos, dragon_speed, green_angle)
Shield.draw_shields(blue_wall, blue_w, initial_bw_x_pos, initial_w_y_pos)
Shield.draw_shields(green_wall, green_w, initial_gw_x_pos, initial_w_y_pos)

class Game:
    def __init__(self):
        pass

    # Check if an event happens
    @staticmethod
    def check_events():
        global hit_timer
        clk.tick(60)
        if hit_timer > 0:
            hit_timer -= 1
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if abs(event.value) > 0.4:
                        blue_dragon.dir.x = event.value
                    else:
                        blue_dragon.dir.x = 0
                elif event.axis == 1:
                    if abs(event.value) > 0.4:
                        blue_dragon.dir.y = event.value
                    else:
                        blue_dragon.dir.y = 0

            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if abs(event.value) > 0.4:
                        green_dragon.dir.x = event.value
                    else:
                        green_dragon.dir.x = 0
                if event.axis == 1:
                    if abs(event.value) > 0.4:
                        green_dragon.dir.y = event.value
                    else:
                        green_dragon.dir.y = 0

    def game_loop(self):

        while True:
            dt = clock.tick() / 1000
            self.check_events()
            screen.fill([0, 0, 0])

            drawGroup.draw(screen)
            Dragon.dragon_move(green_dragon, dt)
            Dragon.dragon_move(blue_dragon, dt)

            pygame.display.flip()




