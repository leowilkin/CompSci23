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

# Define variables for the box location and movement
xPos = (screenWidth -boxWidth)/2
yPos = (screenHeight -boxHeight)/2
xMove = 0
yMove = 0
sTep = 20

# create a clock to help control the display window update
speed = 10
loopClock = pygame.time.Clock()

# create a variable to run the game. If the variable
# changes to false, stop the loop
runGame = True

while runGame == True:
    # clear the screen, ready to be redrawn
    window.fill(BLACK)

    # draw the box at position (xPos,yPos)
    pygame.draw.rect(window,RED,(xPos,yPos,boxWidth,boxHeight))

    # update the screen
    pygame.display.update()

    # wait
    loopClock.tick(speed)

    # Set xMove and yMove to 
    xMove = 0
    yMove = 0

    keyPresses = pygame.event.get()
    
    for event in keyPresses:
        if event.type == pygame.QUIT:
            runGame = False
        # Arrow event capture
        else:
            #if a key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # go left, so no motion vertically (yMove = 0)
                    # and set xMove to negative
                    xMove = -sTep
                    yMove = 0

                elif event.key == pygame.K_RIGHT:
                    # go left, so no motion vertically (yMove = 0)
                    # and set xMove to negative
                    xMove = sTep
                    yMove = 0

                elif event.key == pygame.K_UP:
                    yMove = -sTep
                    xMove = 0

                elif event.key == pygame.K_DOWN:
                    yMove = sTep
                    xMove = 0



        if xMove > 0:
          if (xPos + boxWidth) >= screenWidth:
            xMove = -xMove
        else:
          if xPos <= 0:
            xMove = -xMove
    
        if yMove > 0:
          if (yPos + boxHeight) >= screenHeight:
            yMove = -yMove
        else:
          if yPos <= 0:
            yMove = -yMove
            

    # Now update box coordinates
    xPos += xMove
    yPos += yMove

    # End of while loop, heading back to top

print('Exiting Game')
exit()
