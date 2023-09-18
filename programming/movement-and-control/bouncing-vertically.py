import pygame

#initialise all pygame functions
pygame.init()

# Define variables for colours in (r,g,b) format
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Define variables for the screen size and set up the game window
screenWidth = 500
screenHeight = 400
window = pygame.display.set_mode((screenWidth, screenHeight))

# Define variables for the box size
boxWidth = 50
boxHeight = 50

# Define variables for the initial box location and movement
xPos = 10
yPos = 10
xMove = 10
yMove = 10

# create a clock to help control the display window update
speed = 10
loopClock = pygame.time.Clock()

# create a variable to run the game. 
runGame = True

# Game loop
while runGame == True:
  # clear the screen, ready to be redrawn
  window.fill(WHITE)

  # draw the red box at position (xPos,yPos)
  pygame.draw.rect(window,RED,(xPos,yPos,boxWidth,boxHeight))

  # update the screen
  pygame.display.update()

  # wait
  loopClock.tick(speed)

  if yMove >= 0:
    if (yPos + boxHeight) == screenHeight:
       yMove = -yMove

  else:
    if yPos == 0:
      yMove = -yMove

  # Change y position
  yPos = yPos + yMove

  # key presses
  keyPresses = pygame.event.get()
  print(keyPresses)
  for key in keyPresses:
    print(key.type)
    if key.type == pygame.QUIT:
      runGame = False
    # stop game   


print('Exiting Game')
exit()
