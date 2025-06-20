import pygame
import sys

# Inisialisasi Pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Demo Antialiasing Line")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Loop utama
running = True
while running:
    screen.fill(WHITE)

    # Tanpa Antialiasing - Garis biasa
    pygame.draw.line(screen, BLACK, (50, 100), (350, 300), 1)

    # Dengan Antialiasing - Menggunakan aaline
    pygame.draw.aaline(screen, BLACK, (450, 100), (750, 300), 1)

    # Judul
    font = pygame.font.SysFont(None, 24)
    text1 = font.render("Tanpa Antialiasing", True, BLACK)
    text2 = font.render("Dengan Antialiasing", True, BLACK)
    screen.blit(text1, (120, 320))
    screen.blit(text2, (520, 320))

    pygame.display.flip()

    # Event keluar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()