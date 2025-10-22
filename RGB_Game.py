import pygame
import random
pygame.init()

width = 800
height = 600
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
Screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("RPG")

BROWN = (150,75,0)

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.color = (255, 0, 0)
        self.speed = 5
        self.health = 3
        self.inventory = []
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        
    def move(self,keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed

player = Player(500, 250)

class Enemy:
    def __init__(self, x, y):
        self.speed = 2
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect(topleft=(x, y))
        
    def draw(self, surface):
        surface.blit(self.image, self.rect) 
        
    def move_towards(self, target_rect):
        if(self.rect.x < target_rect.x):
            self.rect.x += self.speed
        elif(self.rect.x > target_rect.x):
            self.rect.x -= self.speed
        if(self.rect.y < target_rect.y):
            self.rect.y += self.speed
        elif(self.rect.y > target_rect.y):
            self.rect.y -= self.speed
enemy = Enemy(100,100)

running = True
while running:
    Screen.fill(BROWN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.draw(Screen)
    enemy.draw(Screen)
    enemy.move_towards(player.rect)

    Keys=pygame.key.get_pressed()   
    
    player.move(Keys)

    clock.tick(60)
    
    health_text = font.render(f"Health: {player.health}", True, (255,255,255))
    Screen.blit(health_text, (5, 5))
    
    # enemy collision
    if player.rect.colliderect(enemy.rect):
        player.health -= 1
        
        enemy.rect.x = random.randint(5,750)
        enemy.rect.y = random.randint(5,550)
        
    if(player.health < 1):
        running=False
        
        print("Game Over")
    
    pygame.display.update() 