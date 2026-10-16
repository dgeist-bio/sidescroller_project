import pygame

pygame.init()
pygame.font.init()
text = pygame.font.SysFont("Arial", 12)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")

    fps = clock.tick(60)
    fps_show = str(fps)
    fps_gui = text.render(fps_show, True, "red")
    screen.blit(fps_gui, (40, 40))

    pygame.display.flip()

pygame.quit()