# PE8: all imports at the beginning
import pygame, sys


# --- constants ---

WINDOW_SIZE = (1500, 1000)
bullet_y = 0

# --- classes --- # PEP8: all classes before main part


class Player(pygame.sprite.Sprite):
    # PEP8: empty line before method
    def __init__(self):
        # pygame.sprite.Sprite.__init__(self)  # Python 2 & 3
        super().__init__()  # only Python 3
        self.health = 3
        self.hits = 0
        self.images = []
        self.current_image = 0
        self.images.append(pygame.image.load('data/idle/idle2.png'))
        self.images.append(pygame.image.load('data/idle/idle3.png'))
        self.images.append(pygame.image.load('data/idle/idle2.png'))

        self.image = self.images[self.current_image]
        self.facing = 1

        self.rect = self.image.get_rect()
        self.rect.centerx = 377
        self.rect.bottom = 270

        self.is_jump = False  # PEP8: `lower_case_names` for variables
        self.jump_count = 5  # PEP8: `lower_case_names` for variables

        self.movement = pygame.math.Vector2(0, 0)
        self.speed = pygame.math.Vector2(0, 0)
        self.aimingup = False
        self.moving_right = False
        self.moving_left = False
        self.aimingdown = False
        self.vertical_momentum = 0
        self.air_timer = 0
        self.frame_counter = 0
        self.facing_left = False
    def update(self):
        self.images = []

        self.images.append(pygame.image.load('data/idle/idle2.png'))
        self.images.append(pygame.image.load('data/idle/idle3.png'))
        self.images.append(pygame.image.load('data/idle/idle2.png'))

        if player.moving_right or player.moving_left:
            self.images = []
            self.images.append(pygame.image.load('data/run/run1.png'))
            self.images.append(pygame.image.load('data/idle/idle3.png'))
            self.images.append(pygame.image.load('data/run/run2.png'))
        if player.aimingup:
            self.images = []
            self.images.append(pygame.image.load('data/idle/shootup.png'))
            self.images.append(pygame.image.load('data/idle/shootup.png'))
            self.images.append(pygame.image.load('data/idle/shootup.png'))
        if player.aimingup and (player.moving_right or player.moving_left):
            self.images = []
            self.images.append(pygame.image.load('data/run/shootuprun1.png'))
            self.images.append(pygame.image.load('data/idle/shootup.png'))
            self.images.append(pygame.image.load('data/run/shootuprun2.png'))
        if player.aimingdown:
            self.images = []
            self.images.append(pygame.image.load('data/idle/shootdown.png'))
            self.images.append(pygame.image.load('data/idle/shootdown.png'))
            self.images.append(pygame.image.load('data/idle/shootdown.png'))
        if player.aimingdown and (player.moving_right or player.moving_left):
            self.images = []
            self.images.append(pygame.image.load('data/run/shootdownrun1.png'))
            self.images.append(pygame.image.load('data/idle/shootdown.png'))
            self.images.append(pygame.image.load('data/run/shootdownrun2.png'))

        self.speed.x = 0
        self.frame_counter += 1
        if self.frame_counter == 10:
            self.current_image += 1
            self.frame_counter = 0
        if self.current_image == 3:
            self.current_image = 0
        if self.moving_left:
            self.facing_left = True
        elif self.moving_right:
            self.facing_left = False
        if self.facing_left:
            self.image = pygame.transform.flip(self.images[self.current_image],True,False)
        else:
            self.image = self.images[self.current_image]

    def draw(self, screen, offset):
        screen.blit(self.image, self.rect.move(-offset))

class Boss(pygame.sprite.Sprite):

    def __init__(self, x, y,num):
        # pygame.sprite.Sprite.__init__(self)  # Python 2 & 3
        super().__init__()  # only Python 3

        if num == 1:
            self.image = pygame.image.load('data/boss.png')
            self.rect = self.image.get_rect()
            self.bossrect = self.image.get_rect()
            self.bossrect.centerx = y
            self.bossrect.bottom = x
            self.rect.centerx = y
            self.rect.bottom = x
            self.speedx = 1
            self.speedy = 1
            self.num = num
            self.health = 20

        self.rect1 = self.rect.x
    def update(self):

        if collision_test(self.rect,map_data.tile_rects):
            self.speedx *= -1

        if self.rect.centerx < player.rect.centerx:
            self.rect.centerx += self.speedx

        if self.rect.centerx > player.rect.centerx:
            self.rect.centerx -= self.speedx

        if self.rect1 - self.rect.x < 0:
            self.image = pygame.image.load('data/boss.png')

        else:
            self.image = pygame.image.load('data/boss.png')

        self.rect1 = self.rect.x

    def draw(self, screen, offset):
        screen.blit(self.image, self.rect.move(-offset))

class Mob(pygame.sprite.Sprite):

    def __init__(self, x, y,num):
        # pygame.sprite.Sprite.__init__(self)  # Python 2 & 3
        super().__init__()  # only Python 3

        self.counter = 1
        self.enemy_framerate = 1
        if num == 0:
            self.image = pygame.image.load('data/mob1.1.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = y
            self.rect.bottom = x
            self.speedx = 1
            self.speedy = 1
            self.movement = pygame.math.Vector2(1, 1)
            self.num = num
            self.health = 2
            self.movex = False
            self.movey = False
            self.trackingRadius = 80

        self.rect1 = self.rect.x
    def update(self):
        if (abs(self.rect.centerx - player.rect.x) <= self.trackingRadius) and (abs(self.rect.centery - player.rect.y) <= self.trackingRadius):
            #self.movement = pygame.math.Vector2(1, 1)

            collisions = mobCollisions(self, map_data)

            if self.rect.centerx <= player.rect.centerx:
                self.movement.x = 1
            if self.rect.centery <= player.rect.centery:
                self.movement.y = 1

            if self.rect.centerx >= player.rect.centerx:
                self.movement.x = -1
            if self.rect.centery >= player.rect.centery:
                self.movement.y = -1

        else:
            self.rect.centerx += self.movement.x
            if collision_test(self.rect, map_data.tile_rects):
                self.movement.x *= -1

        if self.rect1 - self.rect.x < 0:
            if self.num == 0:
                self.image = pygame.image.load('data/mob1.1.png')

        else:
            if self.num == 0:
                self.image = pygame.image.load('data/mob1.2.png')

        self.rect1 = self.rect.x

    def draw(self, screen, offset):
        screen.blit(self.image, self.rect.move(-offset))

class Bullet(pygame.sprite.Sprite):

    def __init__(self,num,varx,vary):
        # pygame.sprite.Sprite.__init__(self)  # Python 2 & 3
        super().__init__()  # only Python 3
        self.num = num

        if num == 0:
            self.image = pygame.Surface((3, 3))
            self.image.fill((255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.centerx = player.rect.centerx
            self.rect.bottom = player.rect.centery + 2
            self.speedx = 6
            self.speedx *= player.facing
            if bullet_y == 0:
                self.speedy = 0
            elif bullet_y == 1:
                self.speedy = -6
                self.speedx = 0
            elif bullet_y == -1:
                self.speedy = 6
                self.speedx = 0

        if num == 2:
            self.image = pygame.Surface((5, 5))
            self.image.fill((255, 0,0))
            self.rect = self.image.get_rect()
            self.rect.centerx = player.rect.centerx
            self.rect.bottom = player.rect.centery + 2
            self.speedx = 6
            self.speedx *= player.facing
            if bullet_y == 0:
                self.speedy = 0
            elif bullet_y == 1:
                self.speedy = -6
                self.speedx = 0
            elif bullet_y == -1:
                self.speedy = 6
                self.speedx = 0

        if num == 1:
            self.image = pygame.Surface((3, 3))
            self.image.fill((250, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.centerx = boss.rect.centerx + varx
            self.rect.bottom = boss.rect.centery + vary
            self.speedy = 4
            self.speedx = 0


    def update(self):
            self.rect.centerx += self.speedx
            self.rect.centery += self.speedy

    def draw(self, screen, offset):
        screen.blit(self.image, self.rect.move(-offset))

class Item(pygame.sprite.Sprite):

    def __init__(self, x, y,num):
        super().__init__()  # only Python 3
        self.image = pygame.Surface((8, 8))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = y
        self.rect.bottom = x
        self.num = num
        if self.num == 0:
            self.image.fill((200, 200, 255))

    def draw(self, screen, offset):
        screen.blit(self.image, self.rect.move(-offset))

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = (195, 155, 119)
        self.image = pygame.Surface((740, 700))
        self.image.fill(self.color)
        self.image2 = pygame.Surface((84,48))
        self.image2.fill(self.color)
        self.image3 = pygame.Surface((84, 48))
        self.image3.fill(self.color)
        self.image4 = pygame.image.load('data/darkdirt.png')
        self.image5 = pygame.image.load('data/back1.png')
        self.image5 = pygame.transform.scale(self.image5,(700,300))
        self.image6 = pygame.image.load('data/back2.png')
        self.image6 = pygame.transform.scale(self.image6, (900, 200))
        self.image7 = pygame.image.load('data/back3.png')
        self.image7 = pygame.transform.scale(self.image7, (700, 300))

        self.rect = self.image.get_rect()
        self.rect.centerx = 380
        self.rect.bottom = 320
        self.rect2 = self.image.get_rect()
        self.rect2.centerx = 382
        self.rect2.bottom = 972
        self.rect3 = self.image.get_rect()
        self.rect3.centerx = 1026
        self.rect3.bottom = 972
        self.rect4 = self.image.get_rect()
        self.rect4.centerx = 100
        self.rect4.bottom = 961

        self.rect5 = self.image.get_rect()
        self.rect5.centerx = 300
        self.rect5.bottom = 760

        self.rect6 = self.image.get_rect()
        self.rect6.centerx = 200
        self.rect6.bottom = 760
        self.rect7 = self.image.get_rect()
        self.rect7.centerx = 300
        self.rect7.bottom = 670

    def draw(self, screen, offset):
        screen.blit(self.image7, self.rect7.move(-offset / 3.2))
        screen.blit(self.image6, self.rect6.move(-offset / 3.75))

        screen.blit(self.image5, self.rect5.move(-offset / 4.2))
        screen.blit(self.image2, self.rect2.move(-offset))
        screen.blit(self.image3, self.rect3.move(-offset))
        screen.blit(self.image4, self.rect4.move(-offset))

def load_map(path):
   f = open(path + '.txt', 'r')
   data = f.read()
   f.close()
   data = data.split('\n')
   game_map = []
   for row in data:
    game_map.append(list(row))
   return game_map

class Map():

    def __init__(self, game_map):
        self.game_map = game_map

        self.grass_img = pygame.image.load('data/grass.png')
        self.dirt_img = pygame.image.load('data/dirt.png')

        self.tile_rects = []

        for y, layer in enumerate(self.game_map):
            for x, tile in enumerate(layer):
                if tile != '0':
                    self.tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))

    def draw(self, screen, offset):

        for y, layer in enumerate(self.game_map):
            for x, tile in enumerate(layer):
                if tile == '1':
                    display.blit(self.dirt_img, (x * 16 - offset.x, y * 16 - offset.y))
                elif tile == '2':
                    display.blit(self.grass_img, (x * 16 - offset.x, y * 16 - offset.y))

def collision_test(rect, tiles):
    hit_list = []

    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)

    return hit_list

def move(player, map_game):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}  # PEP8: spaces

    player.rect.centerx += player.movement.x

    hit_list = collision_test(player.rect, map_game.tile_rects)

    for tile in hit_list:
        if player.movement.x > 0:
            player.rect.right = tile.left
            collision_types['right'] = True
            break
        elif player.movement.x < 0:
            player.rect.left = tile.right
            collision_types['left'] = True
            break

    player.rect.y += player.movement.y

    hit_list = collision_test(player.rect, map_game.tile_rects)

    for tile in hit_list:
        if player.movement.y > 0:
            player.rect.bottom = tile.top
            collision_types['bottom'] = True
            break
        elif player.movement.y < 0:
            player.rect.top = tile.bottom
            collision_types['top'] = True
            break

    return collision_types

def mobCollisions(mob, map_game):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}  # PEP8: spaces

    hit_list = collision_test(mob.rect, map_game.tile_rects)

    mob.rect.centerx += mob.movement.x

    for tile in hit_list:
        if mob.movement.x > 0:
            mob.rect.right = tile.left
            collision_types['right'] = True
            break
        elif mob.movement.x < 0:
            mob.rect.left = tile.right
            collision_types['left'] = True
            break

    mob.rect.centery += mob.movement.y

    hit_list = collision_test(mob.rect, map_game.tile_rects)

    for tile in hit_list:
        if mob.movement.y > 0:
            mob.rect.bottom = tile.top
            collision_types['bottom'] = True
            break
        elif mob.movement.y < 0:
            mob.rect.top = tile.bottom
            collision_types['top'] = True
            break

    return collision_types

game_map = load_map('data/map')

pygame.init()

pygame.mixer.music.load('data/sample_b.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.5)

pygame.display.set_caption('Space Cadet')

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the windoSw
display_scale = 1
display = pygame.Surface((300*display_scale, 200*display_scale))  # used as the surface for rendering, which is scaled

scroll = pygame.math.Vector2(0, 0)

map_data = Map(game_map)
player = Player()
bosses = [Boss(400,500,1)]
mobs = [Mob(315, 254,0), Mob(315, 500,0), Mob(705, 800,0), Mob(620, 500,0), Mob(625, 800,0), Mob(495, 800,0), Mob(635, 630,0), Mob(540, 630,0), Mob(530, 270,0),Mob(1055,500,0),Mob(990,1000,0),Mob(960,1000,0),Mob(942,390,0),Mob(893,390,0)]
bullets = []
enemy_bullets = []
all_sprites = pygame.sprite.Group()
background = Background()
items =[Item(300,730,0),Item(425,1160,0), Item(1050,160,1),Item(685,1850,2)]
# - main loop -

font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(('HP:' + str(player.health - player.hits - 1)), True, (100,100,200))

end_text = font.render('GAME OVER!', True, (255,255,255))
end_textRect = end_text.get_rect()
end_textRect.center = (150, 100)

end_text2 = font.render('YOU WON!', True, (255,255,255))
end_textRect2 = end_text2.get_rect()
end_textRect2.center = (150, 100)

item_0_text = font.render("Allows additional bullet on screen.",True, (255,255,255))
item_0_textRect = item_0_text.get_rect()
item_0_textRect.center = (150, 180)

item_1_text = font.render("High Jump",True, (255,255,255))
item_1_textRect = item_1_text.get_rect()
item_1_textRect.center = (150, 180)

item_2_text = font.render("Extra Health",True, (255,255,255))
item_2_textRect = item_2_text.get_rect()
item_2_textRect.center = (150, 180)

textRect = text.get_rect()

textRect.center = (20, 10)

clock = pygame.time.Clock()
max_bullets = 1
max_jump = 0
invincibility = False
invincibility_counter = 0
boss_bullet_counter = 0
rapid_fire = False
color = 255

end = False
while True:

    if boss_bullet_counter <= 30:
        boss_bullet_counter += 1
    else:
        boss_bullet_counter = 0


    item_text = -1
    text = font.render(('HP:' + str(player.health - player.hits - 1)), True, (100, 100, 200))

    all_sprites.add(player, mobs, bullets,items,enemy_bullets,bosses)
    # - all updates -
    all_sprites.update()

    player.movement.update(0, 0)

    if player.moving_right == True:
        player.movement.x += 2

    if player.moving_left == True:
        player.movement.x -= 2

    player.movement.y += player.vertical_momentum

    player.vertical_momentum += .25
    if player.vertical_momentum > 4:
        player.vertical_momentum =4

    if invincibility:
        invincibility_counter += 1
        if (invincibility_counter % 10) <= 5:
            all_sprites.remove(player)
        if invincibility_counter >= 120:
            invincibility_counter = 0
            invincibility = False

    collisions = move(player, map_data)

    if collisions['bottom'] == True:
        player.air_timer = 0
        player.jump_count = 0
        player.vertical_momentum = 0
    else:
        player.air_timer += 1
    if collisions['top'] == True:
        player.vertical_momentum = 0
    try:
        for boss in bosses:
            if pygame.sprite.collide_rect(player, boss):
                if invincibility == False:
                    player.hits += 1
                    invincibility = True
            for bullet in bullets:
                if pygame.sprite.collide_rect(bullet, boss):
                    bullets.pop(bullets.index(bullet))
                    all_sprites.remove(bullet)
                    boss.health -= 1
                    if boss.health <= 0:
                        bosses.pop(bosses.index(boss))
                        all_sprites.remove(boss)
                        end = True

        for mob in mobs:
            for bullet in bullets:
                        if pygame.sprite.collide_rect(bullet, mob):
                            bullets.pop(bullets.index(bullet))
                            all_sprites.remove(bullet)
                            mob.health -= 1
                            if mob.health <= 0:
                                mobs.pop(mobs.index(mob))
                                all_sprites.remove(mob)

            if pygame.sprite.collide_rect(player, mob):
                if invincibility == False:
                    player.hits += 1
                    invincibility = True

        for enemy_bullet in enemy_bullets:
            if collision_test(enemy_bullet.rect, map_data.tile_rects):
                enemy_bullets.pop(enemy_bullets.index(enemy_bullet))
                all_sprites.remove(enemy_bullet)

            if pygame.sprite.collide_rect(enemy_bullet, player):
                if invincibility == False:
                    player.hits += 1
                    invincibility = True

        for bullet in bullets:

            if collision_test(bullet.rect, map_data.tile_rects):
                bullets.pop(bullets.index(bullet))
                all_sprites.remove(bullet)
            if bullet.num == 0:
                if abs(bullet.rect.x - player.rect.x) >= 200:
                    bullets.pop(bullets.index(bullet))
                    all_sprites.remove(bullet)
            if bullet.num == 2:
                if abs(bullet.rect.x - player.rect.x) >= 50:
                    bullets.pop(bullets.index(bullet))
                    all_sprites.remove(bullet)
                if abs(bullet.rect.y - player.rect.y) >= 50:
                    bullets.pop(bullets.index(bullet))
                    all_sprites.remove(bullet)
                if color == 0:
                    color = 255
                else:
                    color -= 1
                    bullet.image.fill((color, 0, 0))

        for item in items:
            if abs(item.rect.y - player.rect.y) <= 80 and abs(item.rect.x - player.rect.x) <= 80:
                if item.num == 0:
                    item_text = 0
                if item.num == 1:
                    item_text = 1
                if item.num == 2:
                    item_text = 2

            if pygame.sprite.collide_rect(player, item):
                all_sprites.remove(item)
                items.pop(items.index(item))
                if item.num == 0:
                    max_bullets += 1
                elif item.num == 1:
                    max_jump += 1
                elif item.num == 2:
                    player.health += 1
    except:
        print("Exception")

    if player.moving_left:
        player.facing = -1
    if player.moving_right:
        player.facing = 1

    scroll.update(player.rect.centerx - 150, player.rect.centery - 120)

    offset = pygame.math.Vector2(int(scroll.x), int(scroll.y))

    display.fill((146, 244, 255))  # PEP8: spaces after `,`F
    background.draw(display,offset)
    if rapid_fire:
        bullets.append(Bullet(2, 0, 0))

    if end == False:
        if boss_bullet_counter == 10:
            enemy_bullets.append(Bullet(1,0,20))
        if boss_bullet_counter == 20:
            enemy_bullets.append(Bullet(1,-20,20))
        if boss_bullet_counter == 30:
            enemy_bullets.append(Bullet(1,20,20))

    map_data.draw(display, offset)
    for item in all_sprites:
        item.draw(display, offset)
    display.blit(text, textRect)
    if item_text == 0:
        pygame.draw.rect(display,(0,0,0),(0,160,300,100))
        display.blit(item_0_text,item_0_textRect)
    if item_text == 1:
        pygame.draw.rect(display,(0,0,0),(0,160,300,100))
        display.blit(item_1_text,item_1_textRect)
    if item_text == 2:
        pygame.draw.rect(display,(0,0,0),(0,160,300,100))
        display.blit(item_2_text,item_2_textRect)

    if player.hits >= player.health:
        display.fill((0, 0, 0))
        display.blit(end_text,end_textRect)

    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))

    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():  # event loop
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.moving_right = True
            if event.key == pygame.K_a:
                player.moving_left = True
            if event.key == pygame.K_w:
                player.aimingup = True
                bullet_y = 1
            if event.key == pygame.K_s:
                bullet_y = -1
                player.aimingdown = True
            if event.key == pygame.K_SPACE:
                if player.air_timer < 6:
                    player.vertical_momentum = -5 - max_jump
            if event.key == pygame.K_PERIOD:
                if end == False:
                    if len(bullets) < max_bullets:
                        bullets.append(Bullet(0, 0, 0))

                else:
                    rapid_fire = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_PERIOD:
                rapid_fire = False

            if event.key == pygame.K_d:
                player.moving_right = False
            if event.key == pygame.K_a:
                player.moving_left = False
            if event.key == pygame.K_w:
                player.aimingup = False
                bullet_y = 0
            if event.key == pygame.K_s:
                player.aimingdown = False
                bullet_y = 0




