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

# Fonts
FONT_SM = pygame.font.Font(None, 24)
FONT_MD = pygame.font.Font(None, 32)
FONT_MD2 = pygame.font.Font("Assets/Fonts/spacewarfont.ttf", 25)
FONT_LG = pygame.font.Font(None, 64)
FONT_LG2 = pygame.font.Font("Assets/Fonts/spacewarfont.ttf", 50)
FONT_XL = pygame.font.Font("Assets/Fonts/spacewarfont.ttf", 128)

# Images
background = pygame.image.load('Assets/Images/Backgrounds/blue2.png').convert()
background2 = pygame.image.load('Assets/Images/giphy_stars.gif')
ship_img = pygame.image.load('Assets/Images/Ships/playerShip2_blue.png')
laser_img = pygame.image.load('Assets/Images/Lasers/laserBlue01.png')
mob_img = pygame.image.load('Assets/Images/Enemies/enemyGreen1.png')
mob_img2 = pygame.image.load('Assets/Images/Enemies/enemyBlue3.png')
bomb_img = pygame.image.load('Assets/Images/Bombs/laserGreen14.png')

#Sounds

EXPLOSION = pygame.mixer.Sound('Assets/Sounds/Explosion3.wav')
LASER = pygame.mixer.Sound('Assets/Sounds/laser.ogg')
BOMB_SOUND = pygame.mixer.Sound('Assets/Sounds/Explosion5.wav')
BACKGROUND_SOUND = pygame.mixer.Sound('Assets/Sounds/Jupiter.ogg')

# Fonts
MY_FONT = pygame.font.Font(None, 50)

# Stages
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
        self.shield = 5

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
            #play hit sound
            self.shield -= 1

        if self.rect.right < 0:
            self.rect.right = 910
        elif self.rect.left > 900:
            self.rect.left = -5

        hit_list = pygame.sprite.spritecollide(self, mobs, False)
        if len(hit_list) > 0:
            self.shield = 0

        if self.shield == 0:
            EXPLOSION.play()
            self.kill()
            stage = END        

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

    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)

    def update(self, lasers, player):
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)

        if len(hit_list) > 0:
            EXPLOSION.play()
            player.score += 100
            self.kill()

        elif len(hit_list) == 0:
            stage = END

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
            

    
# Make game objects
ship = Ship(384, 620, ship_img)
mob1 = Mob(100, 30, mob_img)
mob2 = Mob(200, 30, mob_img2)
mob3 = Mob(300, 30, mob_img)
mob4 = Mob(400, 30, mob_img2)
mob5 = Mob(500, 30, mob_img)
mob6 = Mob(600, 30, mob_img2)
mob7 = Mob(700, 30, mob_img)
mob8 = Mob(100, 120, mob_img2)
mob9 = Mob(200, 120, mob_img)
mob10 = Mob(300, 120, mob_img2)
mob11 = Mob(400, 120, mob_img)
mob12 = Mob(500, 120, mob_img2)
mob13 = Mob(600, 120, mob_img)
mob14 = Mob(700, 120, mob_img2)


#Make sprite groups
player = pygame.sprite.GroupSingle()
player.add(ship)
player.score = 0

lasers = pygame.sprite.Group()

mobs = pygame.sprite.Group()
mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9, mob10, mob11, \
         mob12, mob13, mob14)

bombs = pygame.sprite.Group()


fleet = Fleet(mobs)

# set stages
stage = START


# Game helper functions
def show_title_screen():
    title_text = FONT_LG2.render("Welcome to the Beautiful", 1, WHITE)
    title_text_rect = title_text.get_rect(center = (WIDTH/2, 300))
    title_text2 = FONT_LG2.render("Space War Game!!!!", 1, WHITE)
    title_text_rect2 = title_text2.get_rect(center = (WIDTH/2, 400)) 
    title_text3 = FONT_MD.render("Press space to start.", 1, WHITE)
    title_text_rect3 = title_text3.get_rect(center = (WIDTH/2, 500))
    screen.blit(title_text, title_text_rect)
    screen.blit(title_text2, title_text_rect2)
    screen.blit(title_text3, title_text_rect3)

def show_end_title_screen():
    end_title_text = FONT_XL.render("Game Over", 1, WHITE)
    screen.blit(end_title_text, [350, 200])
    
def show_stats(player):
    score_text = FONT_MD2.render("Score: " + str(player.score), 1, WHITE)
    screen.blit(score_text, [32, 32])
    
    health_text = FONT_MD2.render("Player health: " + str(ship.shield), 1, WHITE)
    screen.blit(health_text, [32, 50])

# Game loop
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
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    LASER.play()
                    ship.shoot()

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            ship.move_left()
        elif pressed[pygame.K_RIGHT]:
            ship.move_right()     
    BACKGROUND_SOUND.play()
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        player.update(bombs)
        lasers.update()
        mobs.update(lasers, player)
        bombs.update()
        fleet.update()
    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    #screen.fill(BLACK)
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
    show_stats(player)

    if stage == START:
        show_title_screen()

    elif stage == END:
        show_end_title_screen()

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
