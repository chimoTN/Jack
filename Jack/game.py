import pygame
import pytmx
import pyscroll

from TimeLine import Story
from Sprite import Player

class Game:
    
    def __init__(self):
        #la fenetre du jeu
        self.screen = pygame.display.set_mode((900,700))
        pygame.display.set_caption("Quest")
    
        #pour le temp d'action FPS(quand le perso bouge)
        self.clock = pygame.time.Clock()
    
        #instance de story
        self.story = Story()
        


    def set_portal_list(self,tmx_data):
        
        # Liste de rectangle de collisions
        self.portes = []
        
        for obj in tmx_data.objects:
            if obj.type == "porte":
                self.portes.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                
        #porte
        haut = tmx_data.get_object_by_name('haut')
        self.haut = pygame.Rect(haut.x, haut.y, haut.width, haut.height)
        
        bas = tmx_data.get_object_by_name('bas')
        self.bas = pygame.Rect(bas.x, bas.y, bas.width, bas.height)
        
        droite = tmx_data.get_object_by_name('droite')
        self.droite = pygame.Rect(droite.x, droite.y, droite.width, droite.height)
        
        gauche = tmx_data.get_object_by_name('gauche')
        self.gauche = pygame.Rect(gauche.x, gauche.y, gauche.width, gauche.height)
    
    
    #la liste des murs
    def set_walls_list(self,tmx_data):
        
        # Liste de rectangle de collisions
        self.walls = []
        
        for obj in tmx_data.objects:
            if obj.type == "mur":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                
                
               
    #SAVOIR QUELE PORTE IL ES EN COLISION
    def coli(self,tmx_data):
        
        test = False
        
        #verifier colision avec une porte
        if self.player.feet.colliderect(self.haut):
            print("haut")
            var = "haut"
            test = True
            
        if self.player.feet.colliderect(self.bas):
            print("bas")
            var = "bas"
            test = True
            
        if self.player.feet.colliderect(self.droite):
            print("droite")
            var = "droite"
            test = True
            
        if self.player.feet.colliderect(self.gauche):
            print("gauche")
            var = "gauche"
            test = True
          
        #si collision avec mur
        
        
        #si colision avec avec porte    
        if test == True:
        
            self.story.move_case(var)
                
            rep = self.story.get_map()
            self.set_map(rep)
        

    #POUR SAVOIR QU'ELLE TOUCHE ET ACTIONNER    
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            self.player.move_up()
             
        if pressed[pygame.K_DOWN]:
            self.player.move_down()
             
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
             
        if pressed[pygame.K_RIGHT]:
            self.player.move_right()
            
        
        
    #ON SET LA MAP
    def set_map(self, name):
        #Charger la premier carte.tmx
        tmx_data = pytmx.util_pygame.load_pygame(name + ".tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        
        #generer notre joueur
        player_position = tmx_data.get_object_by_name("Spawn")
        self.player = Player(player_position.x, player_position.y)
                
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 3)
        self.group.add(self.player)
        
        #on appele la methode qui cree la liste contenant les porte
        self.set_portal_list(tmx_data)
        self.set_walls_list(tmx_data)
        return tmx_data
        
        
    #BOUCLE DU JEU
    def run(self):
        
        #le plateau du jeu
        self.story.plateau()
        
        #la case acteulle
        rep = self.story.get_map()
        
        #on set la map
        tmx_data = self.set_map(rep)
        
        #pour avoir la liste des portaille de la case
        self.set_portal_list(tmx_data)
        
        
        play = True
        
        while play:
            
            self.group.update()
            
            #appelle la methode de deplacement
            self.handle_input()
            self.group.center(self.player.rect)
            
            #pour inprimer les layer
            self.group.draw(self.screen)
            pygame.display.flip()
            
            
            
            #self.story.move_case()
            
            #self.story.get_map()
            
            #self.story.scenario()
            
            
            #test sans arret la colision avec un element de la map
            self.coli(tmx_data)
            
            #detection de tapage de touche
            for event in pygame.event.get():
                #Si tu click sur la croix rouge
                if event.type == pygame.QUIT:
                    play = False
                    
                   
                
                elif event.type == pygame.KEYUP:
                    
                    #if event.key == pygame.K_ESCAPE:
                    #    self.set_map("foret.tmx",3)
                    #    print("in")

                    '''
                    if event.key == pygame.K_UP:
                        self.story.move_case("haut")
                        print("haut")
                                    
                    elif event.key == pygame.K_DOWN:
                        self.story.move_case("bas")
                        print("bas")
                                    
                    elif event.key == pygame.K_RIGHT:
                        self.story.move_case("droite")
                        print("droite")
                                    
                    elif event.key == pygame.K_LEFT:
                        self.story.move_case("gauche")
                        print("gauche")
                    
                    rep = self.story.get_map()
                    self.set_map(rep)
                    '''
                
                    
            self.clock.tick(60)
           
        pygame.quit()
        
        
        
        