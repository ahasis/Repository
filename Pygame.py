import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Paddle Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle
paddle_width = 100
paddle_height = 10
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 20

# Ball
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = 2
ball_dy = 2

# Score
score = 0

# Fonts
font = pygame.font.Font(None, 36)

# Countdown
for i in range(3, 0, -1):
    screen.fill(black)
    text = font.render(str(i), True, white)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(1)

# Game Loop
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 3
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += 3

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x <= 0 or ball_x >= screen_width:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy
    elif ball_y >= screen_height:
        text = font.render("Game Over. Score: " + str(score), True, white)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(2)
        running = False

    if ball_y + ball_radius >= paddle_y and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_dy = -ball_dy
        score += 1

    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)
  
pygame.quit()
