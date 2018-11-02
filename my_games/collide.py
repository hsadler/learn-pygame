
# import the pygame module, so you can use it
import pygame


class GameObject():
    def __init__(self, obj, parent, color, x_pos, y_pos):
        self.obj = obj
        self.obj.fill(color)
        self.parent = parent
        self.x = x_pos
        self.y = y_pos
    def move(self, x_amount, y_amount):
        self.x += x_amount
        self.y += y_amount
    def update(self):
        self.parent.blit(self.obj, (self.x, self.y))
    def get_pos_rect(self):
        return self.obj.get_rect(
            center=(
                self.x + self.obj.get_width() / 2,
                self.y + self.obj.get_height() / 2
            )
        )


# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    # set the caption at top of game window
    pygame.display.set_caption("move square")

    # create screen surface
    screen = pygame.display.set_mode((1000, 700))

    # create background
    BG_COLOR = pygame.Color('blue')
    background = GameObject(
        obj=pygame.Surface(screen.get_size()),
        parent=screen,
        color=BG_COLOR,
        x_pos=0,
        y_pos=0
    )
    background.update()

    # create wall
    WALL_WIDTH = 100
    WALL_HEIGHT = screen.get_height()
    WALL_COLOR = pygame.Color('red')
    wall = GameObject(
        obj=pygame.Surface((WALL_WIDTH, WALL_HEIGHT)),
        parent=screen,
        color=WALL_COLOR,
        x_pos=300,
        y_pos=0
    )
    wall.update()

    # create square
    SQ_WIDTH = 100
    SQ_HEIGHT = 100
    SQ_COLOR = pygame.Color('grey')
    square = GameObject(
        obj=pygame.Surface((SQ_WIDTH, SQ_HEIGHT)),
        parent=screen,
        color=SQ_COLOR,
        x_pos=0,
        y_pos=screen.get_height() / 2 - SQ_HEIGHT / 2
    )
    square.update()

    is_collide = False

    # game loop
    running = True
    while running:

        # event handling, gets all events from the eventqueue
        for event in pygame.event.get():
            # exit event conditions
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    running = False

        background.update()
        wall.update()

        if(not is_collide):
            square.move(1, 0)
        square.update()

        # test if the square has collided with the wall
        if square.get_pos_rect().colliderect(wall.get_pos_rect()):
            is_collide = True

        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
