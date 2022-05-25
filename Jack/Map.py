import pygame
import pytmx

class Map:
    
    def __init__(self,screen,player):
        self.maps = dict() # "house" -> Map("house", walls, group)
        self.screen = screen
        self.player = player
        self.current_map = "Fleurosia"
        
    

        
        
    
    
    
    def coli(self):

    
    
        # Liste de rectangle == a porte
        self.portes = []
        
        for obj in tmx_data.object:
            if obj.type == "porte":
                self.portes.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                
                
        #on cree la detection de colision avec les rect 
        name = self.story.get_map()
        tmx_data = pytmx.util_pygame.load_pygame(name + ".tmx")
        
        haut = tmx_data.get_object_by_name('haut')
        bas = tmx_data.get_object_by_name('bas')
        droite = tmx_data.get_object_by_name('droite')
        gauche = tmx_data.get_object_by_name('gauche')
        
        if self.player.feet.colliderect(haut):
            rep = haut
        
        if self.player.feet.colliderect(bas):
            rep = bas
            
        if self.player.feet.colliderect(droite):
            rep = droite
            
        if self.player.feet.colliderect(gauche):
            rep = gauche
            
        self.story.move_case(rep)
        rep = self.story.get_map()
        self.set_map(rep)

            
                
    #la  liste de tout ce qui a dans object
    objects = get by type porte
    
    #on recupere le nom de ce avec quoi on est en colision
    name = get by name 
    
    #on l'envoi a move_casee
    move_case(name)
    
    #on set la map avec la nouvelle carte
    #set_map
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        