import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Dowl Game")

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/multicampus/Desktop/파이썬 똥피하기 게임 프로젝트/background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((0, 0, 255)) # fill 로 RGB 값을 이용한 화면 채우기도 할 수 있다.
    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() # 게임 화면 다시 그리기 (일종의 프레임)

pygame.quit()