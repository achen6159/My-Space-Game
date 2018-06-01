# Imports
import pygame
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 900
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)
TITLE = "Spectacular Space War"
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption(TITLE)

background = pygame.Surface(screen.get_size())
background.fill((250, 250, 250))

#Background
theClock = pygame.time.Clock()

spacebg = pygame.image.load('Assets/Images/Backgrounds/star2_giphy.gif')

background_size = background.get_size()
background_rect = background.get_rect()
screen = pygame.display.set_mode(background_size)
x, h = background_size
x = 0
y = 0

x1 = 0
y1 = -h


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
FRONT_BLUE = (176, 196, 232)
GREY_BLUE = (29, 77, 155)

# Fonts
FONT_SM = pygame.font.Font("Assets/Fonts/Transformers Movie.ttf", 24)
FONT_MD = pygame.font.Font("Assets/Fonts/Transformers Movie.ttf", 32)
FONT_MD2 = pygame.font.Font("Assets/Fonts/spacewarfont.ttf", 25)
FONT_LG = pygame.font.Font("Assets/Fonts/Transformers Movie.ttf", 64)
FONT_LG2 = pygame.font.Font("Assets/Fonts/spacewarfont.ttf", 50)
FONT_XL = pygame.font.Font("Assets/Fonts/spacewarfont.ttf", 128)
MY_FONT = pygame.font.Font("Assets/Fonts/Transformers Movie.ttf", 50)

# Images
background = pygame.image.load('Assets/Images/Backgrounds/blue2.png').convert()
background2 = pygame.image.load('Assets/Images/giphy_stars.gif')
ship_img = pygame.image.load('Assets/Images/Ships/playerShip2_blue.png')
laser_img = pygame.image.load('Assets/Images/Lasers/laserBlue01.png')
mob_img = pygame.image.load('Assets/Images/Enemies/enemyGreen1.png')
mob_img2 = pygame.image.load('Assets/Images/Enemies/enemyBlue3.png')
bomb_img = pygame.image.load('Assets/Images/Bombs/laserGreen14.png')
shield_img = pygame.image.load('Assets/Images/Shields/powerupBlue_shield.png')
ufo_img = pygame.image.load('Assets/Images/Enemies/ufoBlue.png')

#Sounds

EXPLOSION = pygame.mixer.Sound('Assets/Sounds/Explosion3.wav')
LASER = pygame.mixer.Sound('Assets/Sounds/laser.ogg')
HIT_SOUND = pygame.mixer.Sound('Assets/Sounds/hit_sound.ogg')
BOMB_SOUND = pygame.mixer.Sound('Assets/Sounds/Explosion5.wav')

#Stages
START = 0
PLAYING = 1
END = 2
    
# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 3
        self.shield = 3

    def health(self):
        if ship.shield == 3:
            screen.blit(shield_img, (50, 100))
            screen.blit(shield_img, (100, 100))
            screen.blit(shield_img, (150, 100))
        elif ship.shield == 2:
            screen.blit(shield_img, (50, 100))
            screen.blit(shield_img, (100, 100))
        elif ship.shield == 1:
            screen.blit(shield_img, (50, 100))

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

    def shoot(self):
        laser = Laser(laser_img)
        laser.rect.centerx = self.rect.centerx
        laser.rect.centery = self.rect.top
        lasers.add(laser)

    def update(self, bombs):
        hit_list = pygame.sprite.spritecollide(self, bombs, True)

        for hit in hit_list:
            
            self.shield -= 1

            if self.shield > 0:
                HIT_SOUND.play()
            elif ship.shield == 0:
                EXPLOSION.play()

        if self.rect.right < 0:
            self.rect.right = 910
        elif self.rect.left > 900:
            
            self.rect.left = -5

        hit_list = pygame.sprite.spritecollide(self, mobs, False)
        if len(hit_list) > 0:
            self.shield = 0

class Laser(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.speed = 5

    def update(self):
        self.rect.y -= self.speed


        if self.rect.bottom < 0:
            self.kill()

    
class Mob(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.shield = 3

    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)

    def update(self, lasers, player):
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)

        for hit in hit_list:
            HIT_SOUND.play()
            self.shield -= 1

        if self.shield == 0:
            EXPLOSION.play()
            player.score += 100
            self.kill()

        if self.rect.bottom < 0:
            self.kill()
            
class Mob2(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.shield = 3

    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)

    def update(self, lasers, player):
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)

        for hit in hit_list:
            HIT_SOUND.play()
            self.shield -= 1

        if self.shield == 0:
            EXPLOSION.play()
            player.score += 150
            self.kill()

        if self.rect.bottom < 0:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.speed = 3

    def update(self):
        self.rect.y += self.speed

        if self.rect.bottom < 0:
            self.kill()
    
    
class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.moving_right = True
        self.speed = 4
        self.bomb_rate = 60 

    def move(self):
        reverse = False
        
        for m in mobs:
            if self.moving_right:
                m.rect.x += self.speed
                if m.rect.right >= WIDTH:
                    reverse = True
            else:
                m.rect.x -= self.speed
                if m.rect.left <= 0:
                    reverse = True

        if reverse == True:
            self.moving_right = not self.moving_right
            for m in mobs:
                m.rect.y += 32

    def choose_bomber(self):
        rand = random.randrange(0, self.bomb_rate)
        all_mobs = mobs.sprites()
        
        if len(all_mobs) > 0 and rand == 0:
            return random.choice(all_mobs)
        else:
            return None
    
    def update(self):
        self.move()

        bomber = self.choose_bomber()
        if bomber != None:
            BOMB_SOUND.play()
            bomber.drop_bomb()
            
class UFO(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()
        
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 8
        self.moving_right = True

    def move(self):
        for u in UFOs:
            if self.moving_right:
                u.rect.x += self.speed
                if u.rect.right >= WIDTH:
                    self.kill()

    def update(self, lasers, player):
        self.move()
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)

        for hit in hit_list:
            EXPLOSION.play()
            player.score += 200
            self.kill()            

ufo_position = random.randint(-3000, -200)

# Game helper functions
def setup():
    global ship, mobs, stage, player, bombs, lasers, fleet, UFOs, high_score
    
    # Make game objects
    ship = Ship(384, 620, ship_img)
    mob1 = Mob(100, 30, mob_img2)
    mob2 = Mob(200, 30, mob_img2)
    mob3 = Mob(300, 30, mob_img2)
    mob4 = Mob(400, 30, mob_img2)
    mob5 = Mob(500, 30, mob_img2)
    mob6 = Mob(600, 30, mob_img2)
    mob7 = Mob(700, 30, mob_img2)
    mob8 = Mob2(101, 120, mob_img)
    mob9 = Mob2(201, 120, mob_img)
    mob10 = Mob2(301, 120, mob_img)
    mob11 = Mob2(401, 120, mob_img)
    mob12 = Mob2(501, 120, mob_img)
    mob13 = Mob2(601, 120, mob_img)
    mob14 = Mob2(701, 120, mob_img)
    ufo = UFO(ufo_position, 10, ufo_img)

    with open('high_score.txt') as high_score_file:
        high_score = int(high_score_file.read())


    # Make sprite groups
    player = pygame.sprite.GroupSingle()
    player.add(ship)
    player.score = 0

    lasers = pygame.sprite.Group()

    mobs = pygame.sprite.Group()
    mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7)

    mobs2 = pygame.sprite.Group()
    mobs.add(mob8, mob9, mob10, mob11, mob12, mob13, mob14)


    bombs = pygame.sprite.Group()


    fleet = Fleet(mobs)
    
    UFOs = pygame.sprite.Group()
    UFOs.add(ufo)

    # set stages
    stage = START
    pygame.mixer.music.load('Assets/Sounds/Jupiter.ogg')
    pygame.mixer.music.play(2)


def show_title_screen():
    title_text = FONT_LG2.render("Welcome to the Beautiful", True, WHITE)
    title_text_rect = title_text.get_rect(center = (WIDTH/2, 300))
    title_text2 = FONT_LG2.render("Space War Game!!!!", True, WHITE)
    title_text_rect2 = title_text2.get_rect(center = (WIDTH/2, 400)) 
    title_text3 = FONT_MD.render("Press space to start.", True, WHITE)
    title_text_rect3 = title_text3.get_rect(center = (WIDTH/2, 500))
    screen.blit(title_text, title_text_rect)
    screen.blit(title_text2, title_text_rect2)
    screen.blit(title_text3, title_text_rect3)

def show_end():
    if ship.shield == 0:
        lose_title_text = FONT_LG2.render("Game Over", True, GREY_BLUE)
        lose_title_text_rect = lose_title_text.get_rect(center = (WIDTH/2, 300))
        end_title_text = FONT_LG.render("Press r to restart.", True, GREY_BLUE)
        end_title_text_rect = end_title_text.get_rect(center = (WIDTH/2, 400))
        screen.blit(lose_title_text, lose_title_text_rect)
        screen.blit(end_title_text, end_title_text_rect)
    elif len(mobs) == 0:
        win_title_text = FONT_XL.render("You Win!!", True, GREY_BLUE)
        win_title_text_rect = win_title_text.get_rect(center = (WIDTH/2, 300))
        end_title_text = FONT_LG.render("Press r to restart.", True, GREY_BLUE)
        end_title_text_rect = end_title_text.get_rect(center = (WIDTH/2, 400))
        screen.blit(win_title_text, win_title_text_rect)
        screen.blit(end_title_text, end_title_text_rect)
        
def show_stats(player):
    score_text = FONT_MD2.render("Score: " + str(player.score), 1, WHITE)
    screen.blit(score_text, [32, 32])
    high_score_text = FONT_MD2.render("High Score: " + str(high_score), 1, WHITE)
    screen.blit(high_score_text, [32, 64])

# Game loop
setup()
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    pygame.mixer.music.load('Assets/Sounds/William-Tell-Overture-Finale.ogg')
                    pygame.mixer.music.play(2)
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    LASER.play()
                    ship.shoot()
            elif stage == END:
                if event.key == pygame.K_r:
                    setup()

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            ship.move_left()
        elif pressed[pygame.K_RIGHT]:
            ship.move_right()
  
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        player.update(bombs)
        lasers.update()
        mobs.update(lasers, player)
        bombs.update()
        fleet.update()
        UFOs.update(lasers, player)
        if stage == PLAYING:
            if len(mobs) == 0:
                stage = END
                pygame.mixer.music.load('Assets/Sounds/George Gershwin - An American in Paris.mp3')
                pygame.mixer.music.play(2)
            elif ship.shield == 0:
                stage = END
                pygame.mixer.music.load('Assets/Sounds/George Gershwin - An American in Paris.mp3')
                pygame.mixer.music.play(2)
    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.blit(spacebg, background_rect)
    y1 += 5
    y += 5
    screen.blit(spacebg,  (x, y))
    screen.blit(spacebg, (x1, y1))
    if y > h:
        y = -h
    if y1 > h:
        y1 = -h
    lasers.draw(screen)
    player.draw(screen)
    bombs.draw(screen)
    mobs.draw(screen)
    UFOs.draw(screen)
    show_stats(player)
    ship.health()

    if stage == START:
        screen.blit(background, (0, 0))
        show_title_screen()


    elif stage == END:
        show_end()
        if player.score > high_score:
            writehighscore = open("high_score.txt", "w")
            writehighscore.write(str(player.score))
   
            
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
