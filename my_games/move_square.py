
# import the pygame module, so you can use it
import pygame


# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    # set the caption at top of game window
    pygame.display.set_caption("move square")

    # create a screen surface
    screen = pygame.display.set_mode((1000, 700))

    # create a background surface
    BG_COLOR = pygame.Color('blue')
    background = pygame.Surface(screen.get_size())
    background.fill(BG_COLOR)

    # blit the background on the screen
    screen.blit(background, (0, 0))

    # create a square surface
    SQ_HEIGHT = 100
    SQ_WIDTH = 100
    RECT_COLOR = pygame.Color('grey')
    sq_x_pos = 100
    sq_y_pos = 100
    square = pygame.Surface((SQ_WIDTH, SQ_HEIGHT))
    square.fill(RECT_COLOR)

    # blit the square on the screen
    screen.blit(square, (sq_x_pos, sq_y_pos))

    # define a variable to control the main loop
    running = True

    # game loop
    while running:

        # event handling, gets all events from the eventqueue
        for event in pygame.event.get():

            # exit event conditions
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    running = False

        # blit the background on the screen
        screen.blit(background, (0, 0))

        # move the square and blit
        sq_x_pos += 1
        sq_y_pos += 1
        screen.blit(square, (sq_x_pos, sq_y_pos))

        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
