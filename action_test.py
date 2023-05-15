import pygame
import random

# 게임 화면의 너비와 높이
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# 색깔 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake의 초기 위치와 크기
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_size = 10

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# 방향 설정
direction = "RIGHT"
change_to = direction

# 게임 종료 여부
game_over = False

# 게임 루프
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"
            elif event.key == pygame.K_UP:
                change_to = "UP"
            elif event.key == pygame.K_DOWN:
                change_to = "DOWN"

    # 방향 전환
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    elif change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    elif change_to == "UP" and direction != "DOWN":
        direction = "UP"
    elif change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    # Snake 이동
    if direction == "RIGHT":
        snake_pos[0][0] += snake_size
    elif direction == "LEFT":
        snake_pos[0][0] -= snake_size
    elif direction == "UP":
        snake_pos[0][1] -= snake_size
    elif direction == "DOWN":
        snake_pos[0][1] += snake_size

    # 화면 그리기
    screen.fill(BLACK)
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    # 화면 업데이트
    pygame.display.update()

    # FPS 설정
    clock.tick(10)

# 게임 종료시 pygame 종료
pygame.quit()
