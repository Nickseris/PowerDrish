from pygame import *
font.init()
from random import randint


WHITE = (255, 255, 255)


def reset_level():
    player.rect.x, player.rect.y = player_x, player_y
    monster1.rect.x, monster1.rect.y = monster_x1, monster_y1
    monster2.rect.x, monster2.rect.y = monster_x2, monster_y2
    goal.rect.x, goal.rect.y = goal_x, goal_y

def next_level0():
    player.rect.x, player.rect.y = player_x, player_y
    monster1.rect.x, monster1.rect.y = monster_x1, monster_y1
    monster2.rect.x, monster2.rect.y = monster_x2, monster_y2
    goal.rect.x, goal.rect.y = goal_x, goal_y


def tutorial_lev():
    # обновляем фон и персонажей
    window.fill(WHITE)
    window.blit(tutorial, (0, 0))
    player.update()
    monster1.update(0, win_width)

    # отрисовка
    monster1.reset()
    player.reset()
    goal.reset()

    # проверка на убийство игрока монстром 
    monster1.kill()

    # проверка: игрока зашел в зону выигрыша?
    goal.check_goal()

def forest_lev():
    global monster_x1, monster_y1, player_x, player_y, goal_x, goal_y
    # обновляем фон и персонажей
    window.blit(back_forest, (0, 0))

    # передвижение спрайтов
    monster_x1, monster_y1 = win_width/2, win_height/2
    player_x, player_y = 150, win_height/2
    goal_x, goal_y = win_width-150, win_height/2
    player.update()
    monster1.update(0, win_height)

    # отрисовка
    monster1.reset()
    player.reset()
    goal.reset()

    # проверка на убийство игрока монстром 
    monster1.kill()

    # проверка: игрока зашел в зону выигрыша?
    goal.check_goal()

def egept_lev():
    global monster_x1, monster_y1, monster_x2, monster_y2, player_x, player_y, goal_x, goal_y
    # обновляем фон и персонажей
    window.blit(back_egept, (0, 0))

    # передвижение спрайтов
    monster_x1, monster_y1 = win_width/2, win_height/2
    monster_x2, monster_y2 = win_width-200, win_height/2
    player_x, player_y = 150, win_height/2
    goal_x, goal_y = win_width-150, win_height/2
    player.update()
    monster1.update(0, win_height)
    monster2.update(0, win_width)

    # отрисовка
    monster1.reset()
    monster2.reset()
    player.reset()
    goal.reset()

    # проверка на убийство игрока монстром 
    monster1.kill()
    monster2.kill()

    # проверка: игрока зашел в зону выигрыша?
    goal.check_goal()

def space_lev():
    global monster_x1, monster_y1, player_x, player_y, goal_x, goal_y
    # обновляем фон и персонажей
    window.blit(back_space, (0, 0))

    # передвижение спрайтов
    monster_x1, monster_y1 = win_width/2, win_height/2
    player_x, player_y = 150, win_height/2
    goal_x, goal_y = win_width-150, win_height/2
    player.update()
    monster1.vertically_update(0, win_height)

    # отрисовка
    monster1.reset()
    player.reset()
    goal.reset()

    # проверка на убийство игрока монстром 
    monster1.kill()

    # проверка: игрока зашел в зону выигрыша?
    goal.check_goal()

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_x, player_speed_y):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speedx = player_speed_x
        self.speedy = player_speed_y

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

 # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def check_goal(self):
        global finish, level, check
        if self.rect.colliderect(player.rect):
            finish = True
            window.blit(win, (215, win_height/2))
            check = True

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтов стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.top > 0:
            self.rect.y -= self.speedy
        if keys[K_s] and self.rect.bottom < win_height:
            self.rect.y += self.speedy
        if keys[K_a] and self.rect.left > 0:
            self.rect.x -= self.speedx
        if keys[K_d] and self.rect.right < win_width:
            self.rect.x += self.speedx

class Enemy(GameSprite):
    # метод для автоматического управления ботов
    direction_x = "left"
    direction_y = "up"
    # передвижение
    def update(self, start_pos, end_pos):
        change_direction = randint(1,2) # for random changing direction of sprite, on x
        if change_direction == 1:
            direction_x = 'left'
        else: # simp, yeah
            direction_x = 'right'
        
        change_direction = randint(1,2) # on y
        if change_direction == 1:
            direction_y = 'up'
        else:
            direction_y = 'down'

        if self.rect.left <= start_pos: # i really wish it'll work
            self.direction_x = "right"
        if self.rect.right >= end_pos:
            self.direction_x = "left"
        if self.direction_x == 'left':
            self.rect.x -= self.speedx
        else:
            self.rect.x += self.speedx

        
    # смерть
    def kill(self):
        global finish, killing
        if self.rect.colliderect(player.rect):
            killing = True
            finish = True
            window.blit(lose, (215, win_height/2))
            
# настройки игры
win_width = 700
win_height = 500
clock = time.Clock()
icon = image.load('power.png')
display.set_icon(icon)
display.set_caption("PowerDrish")
window = display.set_mode((win_width, win_height))

back_forest = transform.scale(image.load("forrest#1.jpg"), (700, 500))
back_egept = transform.scale(image.load("egept.jpg"), (700, 500))
back_space = transform.scale(image.load("universe.jpg"), (700, 500))

FPS = 60
killing = False
check = False

# текст
font_l_w = font.SysFont(None, 70)
font_tutor = font.SysFont(None, 27)
lose = font_l_w.render("You lose ;(", True, (139, 0, 0))
win = font_l_w.render("You win ;)", True, (0, 139, 0))
tutorial = font_tutor.render("This is a tutorial!!! U can move on WSDA and press button 'SPACE' when u die...)", True, (0, 139, 0))

# местоположение
player_x, player_y = win_width/2, 400
monster_x1, monster_y1 = win_width/2, 150
monster_x2, monster_y2 = 0, 0
goal_x, goal_y = win_width/2, 50

# персонажы
player = Player('drish.png', player_x, player_y, 60, 60, 6, 6)
monster1 = Enemy('monster.png', monster_x1, monster_y1, 72, 62, 3, 3)
monster2 = Enemy('monster.png', monster_x2, monster_y2, 72, 62, 3, 3)
goal = GameSprite('goal.png', goal_x, goal_y, 50, 50, 0, 0)
''' должно быть хп тут '''

# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
finish = False

level = 0

while run:

    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        
        # сама игра: действия спрайтов, проверка правил игры, перерисовка
        if level == 0:
            tutorial_lev()

        if level == 1:
            forest_lev()

        if level == 2:
            egept_lev()

        if level == 3:
            space_lev()

    if check:
        level += 1
        check = False

    else:
        keys = key.get_pressed()
        if keys[K_SPACE] and killing == True:
            finish = False
            reset_level()
        
        if keys[K_SPACE] and killing == False:
            finish = False
            next_level0()

    # FPS
    display.update()
    clock.tick(FPS)
