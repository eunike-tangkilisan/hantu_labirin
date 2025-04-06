import math as m
from pygame import *
font.init()

width = 750
height = 750
screen = display.set_mode((width,height))
display.set_caption("Kuntilanak Maze")
background = transform.scale(image.load("background.jpg"),(width,height))

class karakter(sprite.Sprite):
    # class constructor
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        # Call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)

        # every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed

        # every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        

    #fungsi untuk tampilin char ke layar
    def show(self):
        #window adalah nama variabel screen.jadi
        screen.blit(self.image , (self.rect.x, self.rect.y))
    def tabrakan(self, player_lain):
        return self.rect.colliderect(player_lain)
class human(karakter):
    #control player
    def control(self):

        #untuk tau key apa yg kita tekan
        keys = key.get_pressed()

        if keys[K_a] and self.rect.x > 20: #kalo keyboard a
            self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < width-20: #kalo keyboard d
            self.rect.x += self.speed

        if keys[K_w] and self.rect.y > 20: #kalo keyboard w (kalo di pygame yang ke atas Y nya -)
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < height-20: #kalo keyboard s  (kalo di pygame yang ke bawah Y nya +)
            self.rect.y += self.speed

class ghost(karakter):
    def move_towards_player(self, Player):
        dx, dy = self.rect.x - Player.rect.x, self.rect.y - Player.rect.y
        dist = m.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist
        self.rect.x -= dx * self.speed
        self.rect.y -= dy * self.speed

class wall():
    def __init__(self,x,y,width,height,color):
        self.rect = Rect(x,y,width,height)
        self.color = color
    def draw(self):
        draw.rect(screen,self.color,self.rect)
    def collide_character(self,other_character):
        return self.rect.colliderect(other_character)

kuntilanak_width= 75
kuntilanak_height= 75
kuntilanak_speed= 1
kuntilanak = ghost("kuntilanak.png", 200, 50, kuntilanak_width, kuntilanak_height, kuntilanak_speed)

person_width= 75
person_height= 75
person_speed= 5
person = human("person.png", 25, 350, person_width, person_height, person_speed)

font1 = font.Font(None, 80) #80->ukuran font
warna_text = (255, 80, 0) #black
win = font1.render("Yeah You Win!", True, warna_text)
lose = font1.render("Nice Try", True, warna_text)

mixer.init()
mixer.music.load("horror.ogg")

warna_dinding = (255,255,255)
dinding1 = wall(0,0,750,15,warna_dinding)
dinding2 = wall(0,0,15,300,warna_dinding)
dinding3 = wall(0,400,15,350,warna_dinding)
dinding4 = wall(735,0,15,350,warna_dinding)
dinding5 = wall(735,450,15,300,warna_dinding)
dinding6 = wall(0,712,750,15,warna_dinding)
dinding7 = wall(0,300,150,15,warna_dinding)
dinding8 = wall(300,0,15,600,warna_dinding)
dinding9 = wall(150,175,150,15,warna_dinding)
dinding10 = wall(300,600,150,15,warna_dinding)
dinding11 = wall(600,450,150,15,warna_dinding)
dinding12 = wall(435,200,15,400,warna_dinding)
dinding13 = wall(150,500,150,15,warna_dinding)
dinding14 = wall(585,200,15,415,warna_dinding)

#set volume
mixer.music.set_volume(0.5)
#play backsound music
mixer.music.play()
run = True 
fps = time.Clock()
walls = [dinding1,dinding2,dinding3,dinding4,dinding5,dinding6,dinding7,dinding8,dinding9,dinding10,dinding11,dinding12,dinding13,dinding14]
while run:
    screen.blit(background,(0,0))
    kuntilanak.show()
    person.show()
    dinding1.draw()
    dinding2.draw()
    dinding3.draw()
    dinding4.draw()
    dinding5.draw()
    dinding6.draw()
    dinding7.draw()
    dinding8.draw()
    dinding9.draw()
    dinding10.draw()
    dinding11.draw()
    dinding12.draw()
    dinding13.draw()
    dinding14.draw()
    person.control()
    kuntilanak.move_towards_player(person)
    for e in event.get():
        if e.type == QUIT:
            quit()
    if any(sprite.collide_rect(person, wall) for wall in walls):
        person.rect.x = 50
        person.rect.y = 325
    if person.tabrakan(kuntilanak):
        person.speed = 0
        kuntilanak.speed = 0
        screen.blit(lose,(300,375))
    if person.rect.x > 690 and 325 < person.rect.y < 425:
        person.speed = 0
        kuntilanak.speed = 0
        screen.blit(win,(225,325))
    display.update()
    fps.tick(60)