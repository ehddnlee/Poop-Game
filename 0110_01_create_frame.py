import pygame # pygame 설치여부 확인

# 환경설정, 프레임

pygame.init() # 초기화 (반드시 필요)

 # 1 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

 # 2 타이틀 설정
pygame.display.set_caption("Dowl Game") #게임 이름

 # 3 이벤트 루프
running = True # 게임이 진행중인가? 
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT: # 게임 창을 닫는 이벤트가 발생했나?
            running = False # 게임 진행중이 아님


 # 4 pygame 종료
pygame.quit()