import pygame

pygame.font.init()
pygame.mixer.init()

# Screen
screen_width = 1400
screen_height = 680

# Clock
clk = pygame.time.Clock()
hit_timer = 0
fps = 60

# Dragons
drawGroup = pygame.sprite.Group()
green_dragon = pygame.sprite.Sprite(drawGroup)
blue_dragon = pygame.sprite.Sprite(drawGroup)

blue_d = "blue_dragon"
green_d = "green_dragon"

blue_angle = 70
green_angle = -70

dragon_speed = 100

initial_bd_x_pos = 70
initial_gd_x_pos = 1230
initial_d_y_pos = 320

# Shields (walls)
blue_wall = pygame.sprite.Sprite(drawGroup)
green_wall = pygame.sprite.Sprite(drawGroup)
blue_w = "blue_wall"
green_w = "green_wall"

shield_speed = 5

initial_bw_x_pos = 200
initial_gw_x_pos = 1100
initial_w_y_pos = 325

# Game display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dragon-Flame")