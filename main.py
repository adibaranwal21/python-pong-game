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
    ball_accel_x *= -1
  if random.randint(1, 2) == 1:
    ball_accel_y *= -1

  while True: # Game loop
    """
    set the back ground color to black
    needs to be called everytime the game updates
    """
    screen.fill(COLOR_BLACK)

    for event in pygame.event.get():
      if event.type == pygame.QUIT: # If exited
        return # Exit and finish

if __name__ == '__main__':
  main()