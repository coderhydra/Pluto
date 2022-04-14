import time

import pygame
import datetime
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

    watch_now = '{}:{}:{}'.format(datetime.datetime.now().hour,datetime.datetime.now().minute, datetime.datetime.now().second)
    datetime_weekday = datetime.datetime.now().weekday()
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    weekday = ""
    for i in range(len(weekdays)):
        if datetime_weekday==i:
            weekday = weekdays[i]
    # Text를 surface에 그리기, 안티알리어싱, 검은색
    date = myFont.render(str(datetime.datetime.now().date())+" "+weekday, True, BLACK)
    watch = myFont.render(str(watch_now), True, BLACK)
    # Rect 생성
    watch_Rect = watch.get_rect()
    date_Rect = date.get_rect()
    # 가로 가운데, 세로 50 위치
    date_Rect.centerx = round(SCREEN_WIDTH / 2)
    date_Rect.y = 50
    watch_Rect.centerx = round(SCREEN_WIDTH / 2)
    watch_Rect.y = 100

    # Text Surface SCREEN에 복사하기, Rect 사용
    SCREEN.blit(watch, watch_Rect)
    SCREEN.blit(date, date_Rect)

    # 작업한 스크린의 내용을 갱신하기
    pygame.display.flip()

    # 1초에 60번의 빈도로 순환하기
    clock.tick(60)
