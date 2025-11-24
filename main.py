import pygame
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# Dimensions of height x width

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Values of RGB

def main():
  # Game setup, every time on restart

  pygame.init() # Initializes pygame library
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creates screen for the game
  pygame.display.set_caption("Pong") # Title for window

  """
  these are the players' game paddles
  the pygame.Rect function need the x, y, width and height
  of the rectangles we will be drawing
  """
  paddle_1_rect = pygame.Rect(30, 0, 7, 100)
  paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

  # this is to track by how much the players' paddles will move per frame
  paddle_1_move = 0
  paddle_2_move = 0

  # this is the rectangle that represents the ball
  ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)

  # determine the x and y speed of the ball (0.1 is just to scale the speed down)
  ball_accel_x = random.randint(2, 4) * 0.1
  ball_accel_y = random.randint(2, 4) * 0.1

  # randomize the direction of the ball
  if random.randint(1, 2) == 1:
    ball_accel_x *= -1 # X-Coordinate of ball
  if random.randint(1, 2) == 1:
    ball_accel_y *= -1 # Y-Coordinate of ball

  clock = pygame.time.Clock() # Creates clock for game

  """
  This is to check whether or not to move the ball.
  We will make it move after 3 seconds.
  """
  started = False
  delta_time = clock.tick(60) #Sets up FPS of the game

  while True: # Game loop
    """
    set the back ground color to black
    needs to be called everytime the game updates
    """
    screen.fill(COLOR_BLACK)

    # make the ball move after 3 seconds
    if not started:
    # load the Consolas font
        font = pygame.font.SysFont('Consolas', 30)

    # draw some text to the center of the screen
    text = font.render('Press Space to Start', True, COLOR_WHITE)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen.blit(text, text_rect)

    # update the display
    pygame.display.flip()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                started = True
      
    # draw player 1 and player 2's paddle rects with the white color
    pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
    pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)

    # draw the ball with the white color
    pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

    # update the display (this is necessary for Pygame)
    pygame.display.update()

if __name__ == '__main__':
  main()