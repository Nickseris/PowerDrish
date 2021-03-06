from pygame import *
font.init()
# дань, сорян, что так вышло, что я ничего не сделал за все это время... мне очень стыдно :(
# сейчас я просто чтобы на следующем занятии что-то сказать, добавлю музычку. 
mixer.init()
mixer.music.load('bg-music.mp3')
mixer.music.play()
hitsound = mixer.Sound('hitsound.mp3')
loose_hinsound = mixer.Sound('loose-hitsound.mp3')


WHITE = (255, 255, 255)


def reset_level():
    player.rect.x, player.rect.y = player_x, player_y
    monster1.rect.x, monster1.rect.y = monster_x1, monster_y1
    monster2.rect.x, monster2.rect.y = monster_x2, monster_y2
    monster3.rect.x, monster3.rect.y = monster_x3, monster_y3
    monster4.rect.x, monster4.rect.y = monster_x4, monster_y4
    monster5.rect.x, monster5.rect.y = monster_x5, monster_y5
    monster6.rect.x, monster6.rect.y = monster_x6, monster_y6
    goal.rect.x, goal.rect.y = goal_x, goal_y


def next_level0():
    player.rect.x, player.rect.y = player_x, player_y
    monster1.rect.x, monster1.rect.y = monster_x1, monster_y1
    monster2.rect.x, monster2.rect.y = monster_x2, monster_y2
    monster3.rect.x, monster3.rect.y = monster_x3, monster_y3
    monster4.rect.x, monster4.rect.y = monster_x4, monster_y4
    monster5.rect.x, monster5.rect.y = monster_x5, monster_y5
    monster6.rect.x, monster6.rect.y = monster_x6, monster_y6
    goal.rect.x, goal.rect.y = goal_x, goal_y

def tutorial_lev():
    # обновляем фон и персонажей
    window.fill(WHITE)
    window.blit(tutorial, (0, 0))
    player.update()
    monster1.horizontally_update(0, win_width)

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
    monster1.vertically_update(0, win_height)

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
    monster1.vertically_update(0, win_height)
    monster2.horizontally_update(0, win_width)

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
    global monster_x1, monster_y1, monster_x2, monster_y2, player_x, player_y, goal_x, goal_y, monster_x3, monster_y3, monster_x4, monster_y4, monster_x5, monster_y5
    # обновляем фон и персонажей
    window.blit(back_space, (0, 0))

    # передвижение спрайтов
    
    monster_x1, monster_y1 = win_width/2, win_height/2
    monster_x2, monster_y2 = win_width-200, win_height/2
    monster_x3, monster_y3 = win_width/2, win_height/2
    monster_x4, monster_y4 = 50, 0
    monster_x5, monster_y5 = 500, 0
    monster_x6, monster_y6 = 0, win_height/2

    player_x, player_y = 150, win_height/2
    goal_x, goal_y = win_width-150, win_height/2
    player.update()
    monster1.vertically_update(0, win_height)
    monster2.horizontally_update(0, win_width)
    monster3.horizontally_update(0, win_width)
    monster3.vertically_update(0, win_height)
    monster4.vertically_update(0, win_height)
    monster5.vertically_update(0, win_height)
    #monster6.horizontally_update(0, win_width)


    # отрисовка
    monster1.reset()
    monster2.reset()
    monster3.reset()
    monster4.reset()
    monster5.reset()
    monster6.reset()
    player.reset()
    goal.reset()

    # проверка на убийство игрока монстром 
    monster1.kill()
    monster2.kill()
    monster3.kill()
    monster4.kill()
    monster5.kill()
    monster6.kill()

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
        global finish, check, for_keys
        if self.rect.colliderect(player.rect):
            finish = True
            check = True
            for_keys = True
            window.blit(win, (215, win_height/2))
            hitsound.play()


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
    # горризонтальное передвижение
    def horizontally_update(self, start_pos, end_pos):
        if self.rect.left <= start_pos:
            self.direction_x = "right"
        if self.rect.right >= end_pos:
            self.direction_x = "left"
        if self.direction_x == 'left':
            self.rect.x -= self.speedx
        else:
            self.rect.x += self.speedx

    # вертикальне передвижение
    def vertically_update(self, start_pos, end_pos):
        if self.rect.top <= start_pos:
            self.direction_y = "down"
        if self.rect.bottom >= end_pos:
            self.direction_y = "up"
        if self.direction_y == 'up':
            self.rect.y -= self.speedy
        else:
            self.rect.y += self.speedy

    # смерть
    def kill(self):
        global finish, killing
        if self.rect.colliderect(player.rect):
            killing = True
            finish = True
            window.blit(lose, (215, win_height/2))
            loose_hinsound.play()
            
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
for_keys = False

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
monster_x3, monster_y3 = win_width/2, 150
monster_x4, monster_y4 = 50, 0
monster_x5, monster_y5 = 0, 0
monster_x6, monster_y6 = 0, 0
goal_x, goal_y = win_width/2, 50

# персонажы
player = Player('drish.png', player_x, player_y, 60, 60, 6, 6)
monster1 = Enemy('monster.png', monster_x1, monster_y1, 72, 62, 3, 3)
monster2 = Enemy('monster.png', monster_x2, monster_y2, 72, 62, 3, 3)
monster3 = Enemy('monster.png', monster_x3, monster_y3, 72, 62, 3, 3)
monster4 = Enemy('monster.png', monster_x4, monster_y4, 72, 62, 3, 3)
monster5 = Enemy('monster.png', monster_x5, monster_y5, 72, 62, 3, 3)
monster6 = Enemy('monster.png', monster_x6, monster_y6, 72, 62, 3, 3)
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
        
        if keys[K_SPACE] and check == False and for_keys == True:
            finish = False
            next_level0()

    # FPS
    display.update()
    clock.tick(FPS)
