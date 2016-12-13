########################################################################
##
## CS 101
## Program #8
## Name: Colby Chandler
## Email: crcn96@mail.umkc.edu
##
## PROBLEM : wumpas world
##
## ALGORITHM : 
##      
##       
##      
##      
##       
## 
## 
##
## 
########################################################################

import random
cnt = 0
class map_gen(object):
    
    def __init__ (self,width ,heigth ):
        self.width = width
        self.heigth = heigth
        

    def make_map(width,height):
        world = [[0 for x in range(width)] for y in range(height)]
        return world
    def pit_or_not():
        
        global cnt
        ran_chioce = random.choice([1,2,3,4,5])
        if cnt < 5 :
            if ran_chioce == 1:
                cnt += 1
                return ('p','p')
            if ran_chioce == 2 or ran_chioce == 3 or ran_chioce == 4 or ran_chioce == 5:
            
                return (0,0)
        else:
            
            return (0,0)

    def place_pit(world):
        global cnt
        worlds = world
        for x in range(5):
            for y in range(5):
                if x == 4 and y == 0:
                    worlds[x][y] = 0
                else:
                    worlds[x][y] = random.choice(map_gen.pit_or_not())
                    
        if cnt < 5:
           
           while cnt < 5  :
                pick= [random.choice(range(5)),random.choice(range(5))]
                
                if worlds[pick[0]][pick[1]] == 0 and pick != [4,0] :
                    worlds[pick[0]][pick[1]] = 'p'
                    cnt += 1
                    
                               
        cnt = 0        
        return worlds
    def wumaps_pos(world):
        worlds = world
        number = (0,1,2,3,4)
        wumpas = (random.choice(number),random.choice(number))
        
        check = True
        while check == True:
            if worlds[wumpas[0]][wumpas[1]] == 'p':
                worlds[wumpas[0]][wumpas[1]] = 3
                break
            if wumpas == (4,0):
                wumpas = (random.choice(number),random.choice(number))
            else:
                worlds[wumpas[0]][wumpas[1]] = 'W'
                check =  False
        return worlds
    def gold_pos(world):
        worlds = world
        number = (0,1,2,3,4) 
        gold = (random.choice(number),random.choice(number))
        check = True
        while check == True:
            if worlds[gold[0]][gold[1]] == 'p':
                worlds[gold[0]][gold[1]] = 4
                
                break
            if worlds[gold[0]][gold[1]] == 3:
                worlds[gold[0]][gold[1]] = 'Ω'
                break
            if gold == (4,0):
                gold = (random.choice(number),random.choice(number))
            else:
                worlds[gold[0]][gold[1]] = 'G'
                check =  False
        return worlds



