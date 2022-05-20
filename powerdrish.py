from pygame import *
font.init()


WHITE = (255, 255, 255)

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
        global run
        if self.rect.colliderect(player.rect):
            window.blit(win, (215, win_height/2))



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
        if self.rect.x <= start_pos:
            self.direction_x = "right"
        if self.rect.x >= end_pos:
            self.direction_x = "left"
        if self.direction_x == 'left':
            self.rect.x -= self.speedx
        else:
            self.rect.x += self.speedx

    # вертикальне передвижение
    def vertically_update(self, start_pos, end_pos):
        if self.rect.y >= start_pos and self.rect.y <= end_pos:
            self.rect.y += self.speedy
        else:
            self.rect.y -= self.speedy

    # смерть
    def kill(self):
        global run
        if self.rect.colliderect(player.rect):
            window.blit(lose, (215, win_height/2))
            

win_width = 700
win_height = 500
clock = time.Clock()
icon = image.load('power.png')
display.set_icon(icon)
display.set_caption("PowerDrish")
window = display.set_mode((win_width, win_height))
FPS = 60


# текст
font = font.SysFont(None, 70)
lose = font.render("You lose ;(", True, (139, 0, 0))
win = font.render("You win ;)", True, (0, 139, 0))

# персонажы
player = Player('drish.png', win_width/2, win_height/2, 60, 60, 6, 6)
monsterforrest = Enemy('monster.png', win_width/2, 50, 72, 62, 3, 3)
goal = GameSprite('goal.png', win_width/2, 100, 50, 50, 0, 0)
''' должно быть хп тут '''

# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна

while run:

    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False

    # сама игра: действия спрайтов, проверка правил игры, перерисовка
    # обновляем фон и персонажей
    window.fill(WHITE)
    player.update()
    monsterforrest.horizontally_update(150, win_width-150)

    # отрисовка
    monsterforrest.reset()
    player.reset()
    goal.reset()

    # проверка на убийство игрока монстром 
    monsterforrest.kill()

    # проверка: игрока зашел в зону выигрыша?
    goal.check_goal()

    # FPS
    display.update()
    clock.tick(FPS)
