import pygame
import random

pygame.init()

# screen
WHITE = (71, 193, 71)
size = [400, 300]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

# img load¡
lucas = pygame.image.load('../images/lucas.png')
money = pygame.image.load('../images/8bit_money.png')
BG = pygame.image.load('../images/grass_BG.jpeg')
go_sound = pygame.mixer.Sound("../sounds/go go go.wav")
coin_sound = pygame.mixer.Sound("../sounds/coin.wav")
lucas = pygame.transform.scale(lucas, (60, 45))
money = pygame.transform.scale(money, (30, 30))
token = False
get = False
to_x = 0
to_y = 0


def random_x():
    return random.randrange(60, 340)

def random_y():
    return random.randrange(45, 215)


def runGame():
    global done, lucas, money, token, get, to_x, to_y
    lucas_x = random_x()
    lucas_y = random_y()
    money_x = random_x()
    money_y = random_y()
    go_sound.play()
    while not done:
        clock.tick(24)
        screen.fill(WHITE)
        # print(event.type) #이벤트 확인
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # 방향키 입력에 대한 이벤트 처리
            # while True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    to_y = -10
                elif event.key == pygame.K_DOWN:
                    to_y = 10
                elif event.key == pygame.K_LEFT:
                    to_x = -10
                elif event.key == pygame.K_RIGHT:
                    to_x = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    to_y = 0
                elif event.key == pygame.K_DOWN:
                    to_y = 0
                elif event.key == pygame.K_LEFT:
                    to_x = 0
                elif event.key == pygame.K_RIGHT:
                    to_x = 0

        lucas_x += to_x
        if lucas_x < 0:
            lucas_x = 0
        elif lucas_x > 345:
            lucas_x = 345
        lucas_y += to_y
        if lucas_y < 0:
            lucas_y = 0
        elif lucas_y > 250:
            lucas_y = 250
        screen.blit(BG, (0, 0))
        screen.blit(lucas, (lucas_x, lucas_y))

        if (money_x - 15 < lucas_x < money_x + 15) and (money_y - 30 < lucas_y < money_y + 30):
            get = True
            if token==False:
                coin_sound.play()
                token=True
            print("get")
        if get != True:
            screen.blit(money, (money_x, money_y))
        else:
            pass
        pygame.display.update()

runGame()
pygame.quit()
