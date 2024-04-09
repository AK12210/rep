import pygame
import sys
import math

pygame.init()

screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

current_color = (0, 255, 0)

tool = None
drawing = False

def draw_text(text, position, color):
    font.render_to(screen, position, text, color)

screen.fill((255, 255, 255))
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Drawing figures
            drawing = False
            endp = event.pos
            if tool == 'rectangle':
                pygame.draw.rect(screen, current_color, pygame.Rect(startp, (endp[0] - startp[0], endp[1] - startp[1])))
            elif tool == 'circle':
                radius = int(math.hypot(endp[0] - startp[0], endp[1] - startp[1]))
                pygame.draw.circle(screen, current_color, startp, radius)
            elif tool == 'square':
                side_length = max(abs(endp[0] - startp[0]), abs(endp[1] - startp[1]))
                pygame.draw.rect(screen, current_color, pygame.Rect(startp[0], startp[1], side_length, side_length))
            elif tool == 'triangle':
                pygame.draw.polygon(screen, current_color, [startp, (startp[0], endp[1]), endp])
            elif tool == 'equilateral':
                base_length = math.hypot(endp[0] - startp[0], endp[1] - startp[1])
                height = (math.sqrt(3) / 2) * base_length
                apex_x = (startp[0] + endp[0]) / 2
                apex_y = startp[1] - height
                pygame.draw.polygon(screen, current_color, [startp, endp, (apex_x, apex_y)])
            elif tool == 'rhombus':
                dx = (endp[0] - startp[0]) / 2
                dy = (endp[1] - startp[1]) / 2
                mid_x = (startp[0] + endp[0]) / 2
                mid_y = (startp[1] + endp[1]) / 2
                vert1 = (mid_x - dy, mid_y + dx)
                vert2 = (mid_x + dy, mid_y - dx)
                pygame.draw.polygon(screen, current_color, [startp, vert1, endp, vert2])
            pygame.display.flip()
            
        elif event.type == pygame.KEYDOWN:  # Figures selection
            if event.key == pygame.K_r:
                tool = 'rectangle'
            elif event.key == pygame.K_c:
                tool = 'circle'
            elif event.key == pygame.K_e:
                tool = 'eraser'
            elif event.key == pygame.K_p:
                if current_color == (0, 255, 0):
                    current_color = (255, 0, 0)
                elif current_color == (255, 0, 0):
                    current_color = (0, 0, 255)
                elif current_color == (0, 0, 255):
                    current_color = (0, 255, 0)
            elif event.key == pygame.K_s:
                tool = 'square'
            elif event.key == pygame.K_t:
                tool = 'triangle'
            elif event.key == pygame.K_o:
                tool = 'equilateral'
            elif event.key == pygame.K_l:
                tool = 'rhombus'

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            startp = event.pos

        elif event.type == pygame.MOUSEMOTION and drawing:  # Eraser
            if tool == 'eraser':
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(event.pos[0], event.pos[1], 10, 10))
            pygame.display.flip()


    pygame.display.flip()
