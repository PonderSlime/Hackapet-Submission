import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time
from adafruit_display_text import label
import random

pygame.init()

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()

color_bitmap = displayio.Bitmap(128, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x0000FF

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette)
splash.append(bg_sprite)

square_bitmap = displayio.Bitmap(16, 16, 1)
square_palette = displayio.Palette(1)
square_palette[0] = 0xFF0000

square = displayio.TileGrid(square_bitmap, pixel_shader=square_palette, x=56, y=56)
splash.append(square)

display.show(splash)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Program terminated.")
            exit()

    keys = pygame.key.get_pressed()
    pygame.display.update()

    time.sleep(0.1)