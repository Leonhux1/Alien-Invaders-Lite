# Name = Faizan Rafieuddin.
# Name of the Program = "Pygame Alien Invaders Lite"
# Descrption = "This program is basically a copy of the Professor's program
#               with a little amendments. In place of the stars that were made
#               to bounce by the professor, I've added gifs of aliens. I've
#               also changed the speeds of the aliens by changing the values
#               in the list for the speeds of the stars (aliens), and the speed
#               of the overall program by reducing the time.delay. I've added
#               a spaceship and made it to move and shoot bullets which clears the 
#               part that involves user-directional mods. I've changed the screen
#               size and the background as well. On hitting the aliens with the bullets,
#               points get added to the score board at the top-left corner of the screen.
#               The target is, basically to reach 30 points, from which a winning message
#               is displayed on the screen"

print ("Game console initialized\n")

# Printing out the instructions for playing the game.
print("Instructions:\n")
print("1. Hit the enemy with bullets using the spacebar.\n\n2. Every bullet damages the enemy.\n")
print("3. Score 30 Points while hitting the enemy after which you will win the game.\n")
print("4. Tackling them with your ship also gives you points.\n\nGood Luck!\n")

# Importing the sys and math module for exiting the game window and for calculating distances respectively.
import pygame, sys, math

# Importing the mixer library to add music (Seen on a tutorial).
from pygame import mixer

# Setting up the main window.

pygame.init()

screenSize = width,height = 700, 500

display = pygame.display.set_mode(screenSize)

# Loading in the new background.

background = pygame.image.load("background.gif")

# Adding an alien.

starImage = pygame.image.load("mygif.gif")

starBox = starImage.get_rect()

# Adding a second alien.

starImage2 = pygame.image.load("mygif.gif")

starBox2 = starImage2.get_rect()

keepPlaying = True

# Adding a spaceship.

spaceShip = pygame.image.load("spaceship.gif")

# Adding the image of the bullet

bullet = pygame.image.load("bullet.gif")

# Loading the background music in the game.
mixer.music.load("Music.wav")
mixer.music.play(-1)

# Setting up the coordinates and the speed and other variables for the elements in the game.

bulletX = 0             # Initializing the x coordinate of the bullet to 0 which will be changed later on.

bulletY = 400           # Initializing the y coordinate of the bullet such that it appears to be shot from the center of the ship.

speed = [6,8]           # Have changed the speed values for both of the mygifs.

speed2 = [8,6]

x = 3                   # Initializing the x coordinate of the spaceship.

y = 400                 # Initializing the y coordinate of the spaceship.

playerX_Change = 0      # When the user presses any key, added or subtracted x coordinates of the ship will be stored in this variable.

bullet_State = ''       # A variable useful for maintaining the trajectory of the bullet (Learned through a youtube tutorial).

score = 0               # The score will be accumulated in this variable.

font = pygame.font.Font('freesansbold.ttf', 32)     # Setting the font to display the score on the screen.

font2 = pygame.font.Font('freesansbold.ttf', 70)    # Setting the font to display the ending message on the screen.

fontX = 8             # The x coordinate for displaying the score.

fontY = 8             # The y coordinates for displaying the score.

score_value = ''      # This is helpful in printing the score out to the screen.

ending_Message = ''   # This variable is helpful in printing the ending message out to the screen.

black = 0, 0, 0       # Setting up the RGB value of the color black (done by Professor, I've changed its placing in the program).

while keepPlaying:

    display.fill((black))

    # Adding the background to the entire screen.

    display.blit(background, (0, 0))
    
    # See if it's time to end the game.

    for event in pygame.event.get():

    # Did someone click the X to close the window?

        if event.type == pygame.QUIT:
            mixer.music.set_volume(0)           # On clicking the exit button, the volume of the music is muted.
            keepPlaying = False
            

            # This closes the display.

            pygame.display.quit()
            sys.exit()

    # Check if the arrow keys have been pressed for the ship to act accordingly.
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                playerX_Change -= 20
                
            if event.key == pygame.K_RIGHT:
                playerX_Change += 20

            if event.key == pygame.K_SPACE:
                bullet_State = "fire"
                bulletY -= 15
                
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    # Altering the value of the x coordinate of the spaceship for its movement.
    x += playerX_Change

    # If the value of the bullet reaches the end of the page, the bullet is reset to the middle of the spaceship.
    if bulletY <= 0:
        bulletY = 400
        bullet_State = "ready"

    # These if statements set up the bounds of the screen for the spaceship.
    if x <= 0:
        x = 0

    if x >= 636:
        x = 636


    # Draw the stars on the screen.

    starBox = starBox.move(speed)

    starBox2 = starBox2.move(speed2)
    

    # Update their speed, changing direction if needed.

    if starBox.left < 0 or starBox.right > width:

        speed[0] = - speed[0]

    if starBox.top < 0 or starBox.bottom > height:

        speed[1] = - speed[1]

    if starBox2.left < 0 or starBox2.right > width:

        speed2[0] = - speed2[0]

    if starBox2.top < 0 or starBox2.bottom > height:

        speed2[1] = - speed2[1]

    # See if they collide, print BOOM on the console if they do.

    collide = True

    if starBox.left > starBox2.right:

        collide = False

    elif starBox.right < starBox2.left:

        collide = False

    elif starBox.top > starBox2.bottom:

        collide = False

    elif starBox.bottom < starBox2.top:

        collide = False

    else:

        print ("Boom!")

    # Extracting out the x and y values of the aliens for collision detection with the bullet.
    alienX = starBox[0]

    alienY = starBox[1]

    alienX2 = starBox2[0]

    alienY2 = starBox2[1]

    # This is for making the bullet continuosly travel across the screen when the spacebar is pressed
    # (Otherwise, it stops after every 15 pixels).
    if bullet_State == "fire":
        bulletY -= 15

    # This allows the bullet to follow its original path from which it was shot rather than move with the space ship.
    if bullet_State == "ready":
        bulletX = x

    # This block looks for any collisions between the bullet and the alien and does things accordingly (Using the distance formula).

    distance1 = math.sqrt((math.pow(bulletX - alienX, 2)) +(math.pow(bulletY - alienY, 2)))

    distance2 = math.sqrt((math.pow(bulletX - alienX2, 2)) +(math.pow(bulletY - alienY2, 2)))

    # If the distance between the bullet and either of the aliens is less than 23, add one to the score.
    
    if distance1 < 23 or distance2 < 23:
        score += 1

    # Printing the score to the screen.
    
    score_value = font.render("Points: " + str(score), True, (0, 255, 255))
        
    # If the score reaches 30 points, the game finishes and the volume of the music is lowered to 0.
    if score == 30:
        ending_Message = font2.render("YOU WON!" , True, (255, 255, 255))
        display.blit(ending_Message, (160, 190))
        mixer.music.set_volume(0)
        keepPlaying = False
        
    
    # Updating the display and drawing the new elements on the screen again.

    display.blit(starImage, starBox)

    display.blit(starImage2, starBox2)

    # Displaying the bullet and the score out on the screen.

    display.blit(score_value, (fontX, fontY))

    display.blit(bullet, (bulletX + 16, bulletY + 10))

    pygame.time.delay(50)                       # Delaying the excecution by 50th of a millisecond.

    # Displaying the spaceship on the screen.

    display.blit(spaceShip, (x, y))

    pygame.display.flip()

    



