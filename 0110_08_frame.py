import pygame
######################################################
# 1. 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Dowl Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
######################################################
# 2. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 이벤트 루프 (무조건 있어야 하는 부분)
running = True  # 게임이 진행중인가? Yes
while running:
    dt = clock.tick(60)  # 게임화면 초당 프레임 수 (60FPS)
    print("fps : " + str(clock.get_fps()))

# 3. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    # 어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생했나?
            running = False             # 게임이 진행중이 아니다.
        
# 4. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

# 5. 충돌 처리

# 6. 화면에 그리기

    pygame.display.update()

pygame.quit()