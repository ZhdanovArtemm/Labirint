#создай игру "Лабиринт"!
from pygame import *
init()
window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (700, 500))

enemy_x1 = 180
enemy_x2 = 600
player_speed = 2
player_x = 70
player_y = 425
xv = 470
yv = 215
x1 = 540
y1 = 20
window.blit(background, (0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size_x, player_size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys_pressed[K_s] and self.rect.y < 440:
            self.rect.y += self.speed

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        
        if keys_pressed[K_d] and self.rect.x < 620:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size_x, player_size_y):
        super().__init__(player_image, player_x, player_y, player_speed, player_size_x, player_size_y)
        self.direction = 'left'
    def update(self):
        if self.rect.x <= enemy_x1:
            self.direction = 'right'
        
        if self.rect.x >= enemy_x2:
            self.direction = 'left'
        
        if self.direction == 'right':
            self.rect.x += self.speed

        if self.direction == 'left':
            self.rect.x -= self.speed

class Wall(sprite.Sprite)   :
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



wall1 = Wall(162, 162, 137, 150, 100, 30, 500)
wall2 = Wall(162, 162, 137, 315, 0, 30, 80)
wall3 = Wall(162, 162, 137, 315, 180, 122, 30)
wall4 = Wall(162, 162, 137, 419, 80, 16, 120)
wall5 = Wall(162, 162, 137, 515, 0, 13, 220)
wall8 = Wall(162, 162, 137, 515, 300, 13, 140)
wall6 = Wall(162, 162, 137, 150, 290, 290, 30)
wall7 = Wall(162, 162, 137, 290, 400, 230, 38)
hero = Player("hero.png", player_x, player_y, player_speed, 60, 60)
villian = Enemy("cyborg.png", xv, yv, 2.5, 90, 85)
treasure = GameSprite("treasure.png", x1, y1, 0, 120, 80)
mixer.music.load('jungles.ogg')
mixer.music.play()
mixer.music.set_volume(1)
FPS = 240
clock = time.Clock()
finish = False
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
font = font.SysFont("Arial", 70)
win = font.render('YOU WIN', True, (255, 215, 0))
lose =  font.render('YOU Lose', True, (255, 0, 0))

game = True
while game:
    if finish != True:
        window.blit(background, (0, 0))

        if sprite.collide_rect(hero, treasure):
            window.blit(win, (200, 200))
            finish = True
            money.play()

        if sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6) or sprite.collide_rect(hero, wall7) or sprite.collide_rect(hero, wall8):
            hero.rect.x = 70
            hero.rect.y = 425
            kick.play()
        
        if sprite.collide_rect(hero, villian):
            window.blit(lose, (200, 200))
            finish = True
            kick.play()


        hero.reset()
        villian.reset()
        treasure.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        hero.update()
        villian.update()

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    clock.tick(FPS)
    display.update()
