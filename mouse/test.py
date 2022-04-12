import pyautogui

# 현재 사용하는 모니터의 해상도 출력
print(pyautogui.size())

# 현재 마우스 커서의 위치 출력
print(pyautogui.position())

print("test")


# 절대 좌표로 이동

pyautogui.moveTo(1080, 400)                 # 100, 100 위치로 즉시 이동
pyautogui.moveTo(-1000, 400)                 # 100, 100 위치로 즉시 이동
#pyautogui.moveTo(200, 200, duration=0.5)   # 200, 200 위치로 0.5초간 이동


# 상대 좌표로 이동

#pyautogui.move(100, 100, duration=1)    # 현재 위치 기준으로 100, 100만큼 1초간 이동