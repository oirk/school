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
########################################################################



class char(object):

    def __init__ (self,pos,arrow,gold,alive,wumpas):
        self.pos = pos
        self.arrow = arrow
        self.gold = gold
        self.alive = alive
        self.wumpas = wumpas    
    
    def move(self,dirc,pose):
        
        if dirc == 'north':
            pose[0] -= 1
        if dirc == 'south':
            pose[0] += 1
        if dirc == 'east':
            pose[1] += 1
        if dirc == 'west':
            pose[1] -= 1
        if pose[0] > 4 :
           pose[0] -= 1
           print('you hit a wall')
        if pose[1] > 4:
            print('you hit a wall')
            pose[1] -= 1
            
        if pose[0] < 0 :
            pose[0] += 1
            print('you hit a wall')
        if pose[1] < 0: 
            pose[1] += 1
            print('you hit a wall')
            
    def shoot(self,world,dirc,pose,wumpas):
        hit_list = ['W',3,'Ω']
        lst_for_wumpas = []
        number = []
        if dirc == 'north':
            number = [x for x in range(pose[0])]
            for item in number:
                lst_for_wumpas.append(world[item][pose[1]])
        if dirc == 'south':
            number = [x for x in range(pose[0],5)]
            for item in number:
                lst_for_wumpas.append(world[item][pose[1]])
        if dirc == 'east':
            number = [x for x in range(pose[1],5)]
            for item in number:
                lst_for_wumpas.append(world[pose[0]][item])
        if dirc == 'west':
            number = [x for x in range(pose[1])]
            for item in number:
                lst_for_wumpas.append(world[pose[0]][item])
        for item in hit_list:
            if item in lst_for_wumpas:
                print('you hear a horible scream.')
                wumpas.pop(0)
                wumpas.insert(0,'no')
