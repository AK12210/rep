import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)


paddleW = 150
paddleH = 25


paddleSpeed = 20
ballSpeed = 6

paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1


game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

main_menu_button_img = pygame.transform.scale(pygame.image.load('assets/settings/back_main_menu_button.png'), (350, 50))
start_game_button_img = pygame.transform.scale(pygame.image.load('assets/main_menu/start_game_button.png'), (350, 50))
quit_game_button_img = pygame.transform.scale(pygame.image.load('assets/main_menu/quit_game_button.png'), (350, 50))
settings_button_img = pygame.transform.scale(pygame.image.load('assets/main_menu/settings_button.png'), (350, 50))
collision_sound = pygame.mixer.Sound('catch.mp3')

# Variable to track elapsed time
elapsed_time = 0

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


block_list = [
    {"rect": pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50), "color": (random.randrange(0, 255),
                                                                        random.randrange(0, 255),
                                                                        random.randrange(0, 255)),
     "breakable": random.choice([True, False]),  # Boolean, breakable/unbreakable
     "bonus": random.choice(["grow_paddle", None])}
    for i in range(10) for j in range(4)
]


losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)


winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

while not done:
    dt = clock.tick(FPS) / 1000
    elapsed_time += dt
    start_game_button = screen.blit(start_game_button_img, (120, 500))
        
    #Set options button
    settings_button = screen.blit(settings_button_img, (120, 570))
        
    #Set quit button
    quit_game_button = screen.blit(quit_game_button_img, (120, 640))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if main_menu_button.collidepoint(x, y):
          
    screen.fill(bg)

    [pygame.draw.rect(screen, block["color"], block["rect"]) for block in block_list]
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Adjust paddle size with time
    paddleW -= elapsed_time * 0.002  # Rate of shrinking
    if paddleW < 50:
        paddleW = 50


    paddle.width = paddleW
    paddle.left += (paddle.width - paddleW) // 2

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx

    if ball.centery < ballRadius + 50:
        dy = -dy

    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    for block in block_list:
        if ball.colliderect(block["rect"]):
            if block["breakable"]:
                if block["bonus"] == "grow_paddle":  # Bonus block
                    paddleW += 5  # Increase paddle width
                    if paddleW > W:
                        paddleW = W
                    pygame.mixer.Sound('bonus.mp3').play()
                else:
                    collision_sound.play()
                block_list.remove(block)
                dx, dy = detect_collision(dx, dy, ball, block["rect"])
                game_score += 1
            else:
                if dx > 0:
                    delta_x = ball.right - block["rect"].left
                else:
                    delta_x = block["rect"].right - ball.left
                if dy > 0:
                    delta_y = ball.bottom - block["rect"].top
                else:
                    delta_y = block["rect"].bottom - ball.top

                if abs(delta_x - delta_y) < 10:
                    dx, dy = -dx, -dy
                if delta_x > delta_y:
                    dy = -dy
                elif delta_y > delta_x:
                    dx = -dx

    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not block_list:
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
