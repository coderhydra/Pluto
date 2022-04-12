import pygame

# 스크린 전체 크기 지정

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

# 색상 상수

BLACK = (0, 0, 0)

# pygame 초기화

pygame.init()

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame text test_title")

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

playing = True
while playing:

    # 이벤트 처리
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

    # 스크린 배경색 칠하기

    SCREEN.fill((255, 255, 255))

    # Font 객체 생성

    myFont = pygame.font.SysFont("arial", 30, True, False)

    # Text를 surface에 그리기, 안티알리어싱, 검은색

    text_Title = myFont.render("Pygame Text Test", True, BLACK)

    # Rect 생성

    text_Rect = text_Title.get_rect()

    # 가로 가운데, 세로 50 위치

    text_Rect.centerx = round(SCREEN_WIDTH / 2)

    text_Rect.y = 50

    # Text Surface SCREEN에 복사하기, Rect 사용

    SCREEN.blit(text_Title, text_Rect)

    # Text를 surface에 그리기, 알리어싱, 검은색

    text_Title2 = myFont.render("Pygame Text Test 2", True, BLACK)

    # Text Surface SCREEN에 복사하기, 좌표 사용

    SCREEN.blit(text_Title2, [50, 200])

    # 작업한 스크린의 내용을 갱신하기

    pygame.display.flip()

    # 1초에 60번의 빈도로 순환하기

    clock.tick(60)
