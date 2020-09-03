import pygame

## Define global variables for window size
width = 500
height = 500
## Set win as the window with the correct width and height
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

## Create a player class, this is a colored rectangle
class Player():
    ## Initialize with x and y co-ordinate which will be updated to move the player around
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        ## Define the player rectangle
        self.rect = (x, y, width, height)
        ## Define the speed of the player
        self.vel = 0.25

    ## Show the player rectangle on the screen with the given color, size and position
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    ## Series of commands based on the key that is pressed by the user
    def move(self):
        ## Get a list of all keys being pressed, keys is a list of values that shows which keys are pressed
        keys = pygame.key.get_pressed()

        ## The following commands check if the specific key is pressed (keys[key]==True if that key is pressed)
        ## If the key is pressed, the rectangle moves on the screen at the specified speed (+/- defined vel value)
        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        ## We define rect at the start, we need to redefine the rect each time we move it
        self.rect = (self.x, self.y, self.width, self.height)


## Function to draw the window that is displayed to the user
def redrawWindow(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()

def main():
    ## Checking for collision, checking for events, runs in background
    run = True

    ## Initializes player class, creates rectangle
    p = Player(50, 50, 25, 25, (0, 255, 0))

    ## Runs perpetually, getting events as they occur and checking if it is a quit event
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        ## Unless the player quits, the script will run p.move, which continually scans for key inputs and updates
        ## the player position if a key is pressed. On update, the window will be redrawn with the new position
        p.move()
        redrawWindow(win, p)

main()