import pygame
import sys
import random
pygame.init()
pygame.font.init()


# Arguments :

size = (840, 640)
snake_size = 1
window = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
done = False
screen = pygame.Surface((400, 400))
punkt = 0
font_menu = pygame.font.Font(None, 50)

rect_x = start_cord()
rect_y = start_cord()

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

points_font = pygame.font.Font(None, 32)

rect_change_x = rect_x
rect_change_y = rect_y

rect_h = 20
rect_w = 20
moove_direction = random.randint(0, 4)
food_rect_x = start_cord()
food_rect_y = start_cord()
food_rect_h = 20
food_rect_w = 20
points = 0

# -- MOVE:
moove_left = -20
moove_right = +20
moove_up = -20
moove_down = +20

snake_x = []
snake_y = []
snake_dir = []
#*****************************************************************************
def new_snake():
     nonlocal  snake_x, snake_y, snake_dir, rect_x, rect_y, moove_direction
     snake_x = []
     snake_y = []
     snake_dir  = []
     rect_x = start_cord()
     rect_y = start_cord()
     moove_direction = random.randint(0, 4)

     snake_x.append(snake_x)
     snake_y.append(snake_y)
     snake_dir.append(moove_direction)

class Menu:
    def __init__(self, punkts = (1024, 600, 'Punkts', (250,0,0), (250,30,250), 0)):
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        done_menu = True
        punkt = 0
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0,0)
        pygame.mouse.set_visible(True)
        """ ----------------------------------- """
        while done_menu:
            window.blit(screen, (220, 120))
            screen.fill((0,100,200))
            mp =  pygame.mouse.get_pos()
            # print(mp)
            for i in self.punkts:
                if mp[0] > i[0] + 200 and mp[0] < i[0] +300 and mp[1] > i[1] + 110 and mp[1] < i[1] + 160:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        if punkt == 0:
                            done_menu = False
                        elif punkt == 1:
                            sys.exit()
                        done_menu = False
                    if e.key == pygame.K_F4:
                        sys.exit()
                    if  e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                    if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                        if punkt == 0:
                            done_menu = False
                        elif punkt == 1:
                            sys.exit()
            pygame.display.flip()
# ----------------------------------= F U N C T I O N S =----------------------------------

def start_cord():
    x = random.randint(3, 28)
    x *= 20
    return x
# ----------------------------------= P E R E M E N S =------------------------------------------


snake_x.append(rect_x)
snake_y.append(rect_y)
snake_dir.append(moove_direction)

if snake_dir[0] == 0:
    for kor in range(2):
        snake_x.append(rect_x)
        rect_y += moove_up
        snake_y.append(rect_y)
        snake_dir.append(snake_dir[0])

if snake_dir[0] == 1:
    for kor in range(2):
        rect_change_x += moove_right
        snake_x.append(rect_change_x)
        snake_y.append(rect_change_y)
        snake_dir.append(moove_direction)

if snake_dir[0] == 2:
    for kor in range(2):
        snake_x.append(rect_x)
        rect_change_y += moove_down
        snake_y.append(rect_y)
        snake_dir.append(moove_direction)

if snake_dir[0] == 3:
    for kor in range(2):
        rect_x += moove_left
        snake_x.append(rect_x)
        snake_y.append(rect_y)
        snake_dir.append(moove_direction)

punkts =[(160, 140, 'Play', (250,250,30), (250, 30, 250), 0),
         (160, 210, 'Quit', (250, 250, 30), (250, 30, 250), 1)]

game = Menu(punkts)
game.menu()

# ----------------------------------= GO GO GO =------------------------------------------
while done == False:
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.menu()
                pygame.key.set_repeat(1,1)
                pygame.mouse.set_visible(False)
            if snake_dir[0] == 0:
                if event.key == pygame.K_LEFT:
                    snake_dir[0] = 3
                if event.key == pygame.K_RIGHT:
                    snake_dir[0] = 1
            if snake_dir[0] == 1:
                if event.key == pygame.K_UP:
                    snake_dir[0] = 0
                if event.key == pygame.K_DOWN:
                    snake_dir[0] = 2
            if snake_dir[0]  == 2:
                if event.key == pygame.K_LEFT:
                    snake_dir[0] = 3
                if event.key == pygame.K_RIGHT:
                    snake_dir[0] = 1
            if snake_dir[0]  == 3:
                if event.key == pygame.K_UP:
                    snake_dir[0] = 0
                if event.key == pygame.K_DOWN:
                    snake_dir[0] = 2

    end = len(snake_x)

    if snake_dir[0] == 0:
        snake_y[0] += moove_up
    if snake_dir[0] == 1:
        snake_x[0] += moove_right
    if snake_dir[0] == 2:
         snake_y[0] += moove_down
    if snake_dir[0] == 3:
        snake_x[0] += moove_left

    window.fill((50, 50, 50))
    window.blit(points_font.render('Счет: ' + str(points), 1, red), (700, 60))
    pygame.draw.rect(window, green, [40, 20, 600, 20])
    pygame.draw.rect(window, green, [40, 20, 20, 600])
    pygame.draw.rect(window, green, [640, 20, 20, 600])
    pygame.draw.rect(window, green, [40, 600, 600, 20])

    for kub in range(end):
        pygame.draw.rect(window, white, [snake_x[kub], snake_y[kub], rect_h, rect_w])

    pygame.draw.rect(window, red, [food_rect_x, food_rect_y, food_rect_h, food_rect_w])

    snake_x[1 : end] = snake_x[0: end - 1]
    snake_y[1: end] = snake_y[0: end - 1]
    snake_dir[1 : end] = snake_dir[0: end - 1]

    if snake_x[0] == food_rect_x and snake_y[0] == food_rect_y:
        snake_size = +1
        points += 8
        snake_x.append(food_rect_x)
        snake_y.append(food_rect_y)
        snake_dir.append(snake_dir[end-1])
        choise = True
        while choise:
            food_rect_x = start_cord()+20
            food_rect_y = start_cord()+20
            for i in range(end):
                if food_rect_x == snake_x[i] or food_rect_y == snake_y[i]:
                   pass
                else:
                    choise = False

    if snake_x[0] < 60 or snake_x[0] > 620 or snake_y[0] < 40 or snake_y[0] > 580:
        snake_x = []
        snake_y = []
        snake_dir =[]

        points = 0
        rect_x = start_cord()
        rect_y = start_cord()
        snake_x.append(rect_x)
        snake_y.append(rect_y)
        moove_direction = random.randint (0, 4)
        snake_dir.append(moove_direction)
        kor = 0

        if snake_dir[0] == 0:
            for kor in range(2):
                snake_x.append(rect_x)
                rect_y += moove_up
                snake_y.append(rect_y)
                snake_dir.append(snake_dir[0])

        if snake_dir[0] == 1:
            for kor in range(2):
                rect_change_x += moove_right
                snake_x.append(rect_change_x)
                snake_y.append(rect_change_y)
                snake_dir.append(moove_direction)

        if snake_dir[0] == 2:
            for kor in range(2):
                snake_x.append(rect_x)
                rect_change_y += moove_down
                snake_y.append(rect_y)
                snake_dir.append(moove_direction)

        if snake_dir[0] == 3:
            for kor in range(2):
                rect_x += moove_left
                snake_x.append(rect_x)
                snake_y.append(rect_y)
                snake_dir.append(moove_direction)
        game.menu()
        pygame.key.set_repeat(1, 1)
        pygame.mouse.set_visible(False)

    # rect_y += rect_change_y

    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ

    # Ограничить до 20 кадров в секунду
    pygame.display.flip()
    clock.tick(6)
    print("Hello")
pygame.quit()
