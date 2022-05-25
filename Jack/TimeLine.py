from dataclasses import dataclass
import sys
from random import *


# On va remplire une liste d'entier de 1 a 9 
# chaque chiffre corespond a un decor (1 = chateau ex)
# Il von aleatoirement etre placer dans les case qui porte les nom de a, b,c ....
# a peut avoir selon les partit  1 ou 4 (chateau ou jungle
# 1 sera tjr agale a chateau
#la variable n designe le lieu actuelle (desert , lac) et nom pas la case (a,b,c)

@dataclass
class Carte:
    
    code: int
    name: str
    
class Story:
    
    def __init__(self):
        
        self.fin = False
        self.play = True
        self.histoir = False
        self.casse = "a"
        self.inventaire = []
        self.L = []
        
        self.n = 0
        self.a = 0 
        self.b = 0 
        self.c = 0 
        self.d = 0 
        self.e = 0 
        self.f = 0 
        self.g = 0 
        self.h = 0 
        self.i = 0 
        

    
    def reed(self):
    
        
        
        print("Lumbs")
        print("Start Game")
        print("oui   non")
        self.rep = input()
        
        if self.rep != "oui":
            self.play = False
        else:
            print("lets go")
            
        return self.play
        
        
        
        
    def plateau(self): 
        
        #atribution des case en aleatoire
        L = []
        while len(L) != 9:
            a = randint(1, 9)
            print(a)
            
            if a not in L:
                L.append(a)
               
        
        self.a = L[0]
        self.b = L[1]
        self.c = L[2]
        self.d = L[3]
        self.e = L[4]
        self.f = L[5]
        self.g = L[6]
        self.h = L[7]
        self.i = L[8]   
        
        self.n = self.a
        self.L = L
        
        print(self.L)
    
        
        '''
        #presentation du jeu
        print(" ")
        print("Objectif :")
        print(" ")
        print("Tu rentre de la chasse mais tu as oublier le chemun de ta maison")
        print("ton personnage va ce deplacer de case en case , a chaque case ")
        print("diferente une interaction comme un combat ou un dialogue va ce ")
        print("lancer. A toi de faire le bon choix pour ne pas mourire et ")
        print("atteindre ton objectif qui es de revenire chez toi .")
        print(" ")
        print("Le jeux posaide 9 case qui ne sont jamais au meme androit celon")
        print("les partie . Bonne chance")
        print(" ")
        '''
        
    def move_case(self,name):
        
        #Le plateaux de deplacement
        if self.casse == 'a' :
                
                
            print(" ")
        
            print("ou veux tu allez bas droite gauche haut")
            rep = name
            
            if rep == "haut" :
                self.casse = "g" 
                self.n = self.g
                
            if rep == "bas" :
                self.casse = "d" 
                self.n = self.d
                
            if rep == "gauche" :
                self.casse = "c"
                self.n = self.c
                
            if rep == "droite" :
                self.casse = "b"    
                self.n = self.b
                    
        #on es sur le bloc b
        elif self.casse == 'b' :
                
            print(" ")
        
            print("ou veux tu allez bas droite gauche haut")
            rep = name
            
            if rep == "haut" :
                self.casse = "h" 
                self.n = self.h
                
            if rep == "bas" :
                self.casse = "e" 
                self.n = self.e
                
            if rep == "gauche" :
                self.casse = "a"
                self.n = self.a
                
            if rep == "droite" :
                self.casse = "c"  
                self.n = self.c
                        
        #on es sur le bloc c
        elif self.casse == 'c' :
                
            print(" ")
        
            print("ou veux tu allez bas droite gauche haut")
            rep = name
            
            if rep == "haut" :
                self.casse = "i" 
                self.n = self.i
                
            if rep == "bas" :
                self.casse = "f" 
                self.n = self.f
                
            if rep == "gauche" :
                self.casse = "b"
                self.n = self.b
                
            if rep == "droite" :
                self.casse = "a"   
                self.n = self.a  
                     
        #on es sur le bloc d
        elif self.casse == 'd' :
                
            print(" ")
        
            print("ou veux tu allez bas droite gauche haut")
            rep = name
            
            if rep == "haut" :
                self.casse = "a" 
                self.n = self.a
                
            if rep == "bas" :
                self.casse = "g" 
                self.n = self.g
                
            if rep == "gauche" :
                self.casse = "f"
                self.n = self.f  
                
            if rep == "droite" :
                self.casse = "e"  
                self.n = self.e 
                
                          
        #on es sur le bloc e
        elif self.casse == 'e' :
                
            print(" ")
        
        
            print("ou veux tu allez bas droite gauche haut")
            rep = name
            
            if rep == "haut" :
                self.casse = "b" 
                self.n = self.b
            if rep == "bas" :
                self.casse = "h" 
                self.n = self.h 
                
            if rep == "gauche" :
                self.casse = "d"
                self.n = self.d
                
            if rep == "droite" :
                self.casse = "f" 
                self.n = self.f   
                        
        #on es sur le bloc f
        elif self.casse == 'f' :
                 
            print(" ")
        
            print("ou veux tu allez bas droite gauche haut")
            rep = name
            
            if rep == "haut" :
                self.casse = "c" 
                self.n = self.c 
                
            if rep == "bas" :
                self.casse = "i" 
                self.n = self.i 
                
            if rep == "gauche" :
                self.casse = "e"
                self.n = self.e
                
            if rep == "droite" :
                self.casse = "d"  
                self.n = self.d
                            
        #on es sur le bloc g
        elif self.casse == 'g' :
                 
            print(" ")
        
            print("ou veux tu allez bas droite gauche haut")
            rep = name
            
            if rep == "haut" :
                self.casse = "d" 
                self.n = self.d
                
            if rep == "bas" :
                self.casse = "a" 
                self.n = self.a
                
            if rep == "gauche" :
                self.casse = "i"
                self.n = self.i
                
            if rep == "droite" :
                self.casse = "h" 
                self.n = self.h
                          
        #on es sur le bloc h
        elif self.casse == 'h' :
                 
            print(" ")
        
            print("ou veux tu allez bas droite gauche haut")
            rep = name
            
            if rep == "haut" :
                self.casse = "e" 
                self.n = self.e
                
            if rep == "bas" :
                self.casse = "b" 
                self.n = self.b
                
            if rep == "gauche" :
                self.casse = "g"
                self.n = self.g
                
            if rep == "droite" :
                self.casse = "i"   
                self.n = self.i
                        
        #on es sur le bloc i
        elif self.casse == 'i' :
                                             
            print(" ")
        
            print("ou veux tu allez bas droite gauche haut")
            rep = name
            
            if rep == "haut" :
                self.casse = "f" 
                self.n = self.f
                
            if rep == "bas" :
                self.casse = "c" 
                self.n = self.c 
                
            if rep == "gauche" :
                self.casse = "h"
                self.n = self.h 
                
            if rep == "droite" :
                self.casse = "g"
                self.n = self.g
        
        
        
    
    
        
    def scenario(self):
        #Le magnifique senario
        
        print(" ")
        
        play = True
        
        print("casse =" + self.casse)
        
        if self.n == 1:
            print("tu es dans une jungle")
            
            
        if self.n == 2:
            print("tu es dans une Foret")
                
                
        if self.n == 3:
            print("tu es dans un desert")
                       
            
        if self.n == 4:
            print("tu es dans une ville")
                   
                      
        if self.n == 5:
            print("tu es dans une campagne")
                   
                      
        if self.n == 6:
            print("tu es dans une ferme")
                   
                       
        if self.n == 7:
            print("tu es dans un chateau")
                   
                       
        if self.n == 8:
            print("tu a trouvez ta Maison!")
            play = False
            
        if self.n == 9:
            print("tu es dans un lac")
           
        print(" ")
        
        return play
    
    #on va definir 
    def get_map(self):
        
        '''
        a = 1 / a = jungle
        a = 7 / a = chateau
        on fait un dico de tout ca 
        
        '''
        les_carte = {"jungle":1, "foret":2, "desert":3, "ville":4, "campagne":5, "ferme":6, "chateau":7, "maison":8, "lac":9 }
        
        for cle, valeur in les_carte.items():
            if self.n == valeur :
                print("position = ", cle)
                return cle 
        
        
        


    