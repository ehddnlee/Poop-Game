import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Dowl Game")

background = pygame.image.load("C:/Users/multicampus/Desktop/파이썬 똥피하기 게임 프로젝트/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/multicampus/Desktop/파이썬 똥피하기 게임 프로젝트/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해온다.
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 가운데 위치
character_y_pos = screen_height - character_height # 화면 세로 맨 밑 위치

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    pygame.display.update()

pygame.quit()