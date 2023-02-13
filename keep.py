import game
from config import *


class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def draw_dragons(self, sprite, x, y, ang):

        self.rect = pygame.Rect(x, y, 0, 0)
        self.image = pygame.transform.scale(self.image, [90, 70])
        self.image = pygame.transform.rotate(self.image, ang)

    def dragon_move(self, dx, dy):








        def game_loop(self):
            while True:
                self.check_events()
                pygame.display.update()
                clk.tick(fps)

                Dragon.draw_dragons(blue_dragon, blue_d, initial_bd_x_pos, initial_d_y_pos, 70)
                Dragon.draw_dragons(green_dragon, green_d, initial_gd_x_pos, initial_d_y_pos, -40)
                Shield.draw_shields(blue_wall, blue_w, initial_bw_x_pos, initial_w_y_pos)
                Shield.draw_shields(green_wall, green_w, initial_gw_x_pos, initial_w_y_pos)

                drawGroup.draw(screen)

