import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        
        super().__init__()
        
        #pour l'image
        
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.png')
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.speed = 2
        
        
    #POUR LA COLISION DU JOUEUR (genre ces que a ces pied)    
    def save_location(self):
        self.old_position = self.position.copy()
        
    #POUR LE CHANGEMENT DE DIRECTION DU PERSO
    def change_animation(self,name):
        self.image = self.images[name]
        self.image.set_colorkey([0,0,0])
    
    #MODIFIE LA POSITION DU JOUEUER
    def move_right(self):
        self.position[0] += self.speed
    
    def move_left(self):
        self.position[0] -= self.speed
        
    def move_up(self):
        self.position[1] -= self.speed
        
    def move_down(self):
        self.position[1] += self.speed
        
    #position du joueeur
    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        
    #SI RECT EN CONTACT AVEC COLLITION ON REPLACE LE JOUEUR A LA POSITION AVANT
    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        
    #l'image du perso
    def get_image(self,x,y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0,0), (x, y, 32, 32))
        return image
    
    
    
    
    
    
    
     