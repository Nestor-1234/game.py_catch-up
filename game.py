import pygame 

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Доганялки")

background = pygame.transform.scale(pygame.image.load("pole.png"), (700, 500))

people = pygame.transform.scale(pygame.image.load("people.png"), (1280/4, 1280/4))

running = True
clock = pygame.time.Clock()
fps = 60

p_x = 100
p_y = 100

b_x = 400
b_y = 100

speed = 10

while running:
    window.blit(background, (0, 0))
    window.blit(people, (p_x, p_y))
    window.blit(people, (b_x, b_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and p_y > 5:
        p_y -= speed
    if keys[pygame.K_s] and p_y < 495:
        p_y += speed
    if keys[pygame.K_a] and p_x > 5:
        p_x -= speed
    if keys[pygame.K_d] and p_x < 695:
        p_x += speed

    if keys[pygame.K_UP] and b_y > 5:
        b_y -= speed
    if keys[pygame.K_DOWN] and b_y < 495:
        b_y += speed
    if keys[pygame.K_LEFT] and b_x > 5:
        b_x -= speed
    if keys[pygame.K_RIGHT] and b_x < 695:
        b_x += speed





    pygame.display.update()
    clock.tick(fps)
pygame.quit()

