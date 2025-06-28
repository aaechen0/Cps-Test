import pygame, time, sys
SCREEN_W, SCREEN_H = 1024, 600
#------------------functions---------------
def RT_show_txt(scr, txt, font, x, y, c):
    img = font.render(txt, True, c)
    scr.blit(img, (x, y))
    return
def draw_screen(screen):
    RT_show_txt(screen, 'Clicks: ' + str(cnt), font64, 300, 100, (255, 255, 255))
    RT_show_txt(screen, 'CPS: ' + str(cnt / (time.time() - t)), font64, 300, 150, (255, 255, 255))
    pygame.draw.rect(screen, (255, 255, 255), (sX, sY, sL, sH), 0)
#-------------------pygame init---------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("CPS test")
font64 = pygame.font.Font("simkai.ttf", 32)
#----------------data-------------------
cnt = 0
t = 0
sX, sY = SCREEN_W // 2, SCREEN_H // 2
sL, sH = 100, 100
#-------------main----------------
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] <= sX + sL and event.pos[0] >= sX - sL and event.pos[1] <= sY + sH and event.pos[1] >= sY - sH:
                    cnt += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cnt = 0
                    t = 0
        if cnt == 1 and t == 0:
            t = time.time()
        screen.fill((0, 0, 0))
        draw_screen(screen)
        pygame.display.update()
except:
    print('Error occured')
    pygame.quit()
    sys.exit()
