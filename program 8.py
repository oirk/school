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
########################################################################

from charc import char
from map import maps
from wumpas import map_gen
import random
world = map_gen(5,5)



check = True
game_choice = ['Would you like to play a game?-->','Shall we play a game?-->']
game_start = (input(random.choice(game_choice))).lower()
while check == True:
    mapes = map_gen.gold_pos(map_gen.wumaps_pos(map_gen.place_pit(map_gen.make_map(world.width,world.heigth))))
## turn on for grader
    #for x in range(5):
     #   print(mapes[x])
    score = 0
    chars = char([4,0],1,['no'],['yes'],['yes'])
    poss = [4,0] 
    while game_start == 'yes' or game_start == 'y':
       


        if mapes[poss[0]][poss[1]] == 'p'  or mapes[poss[0]][poss[1]] == 3 or mapes[poss[0]][poss[1]] == 4:
            chars.alive.append('no')
            chars.alive.pop(0)
            score = 0
            print('you have died in a pit.')
            game_start = 'end'
            break
        if  mapes[poss[0]][poss[1]] == 'W':
            if chars.wumpas == ['no']:
                print('there is a dead wumpas here')
            else:
                chars.alive.append('no')
                
                chars.alive.pop(0)
                score = 0
                print('you have been eaten by the wumpas.')
                game_start = 'end'
                break
        maps.surrounding(mapes,poss)
        
        
        action = (input('What action do you want to take?(move,shoot,grab, climb,Quit)-->')).lower()
        
        if action == 'quit':
            exit()
        while action == 'move' or action == 'm':
            score -= 1
            step = 'start'
            dirction = (input('what dirction do you want to go?(north,south,east,west)-->')).lower()
           
            if dirction == 'north' or dirction == 'n':
                chars.move('north',poss)
                step = 'end'
            if dirction == 'south' or dirction == 's':
                chars.move('south',poss)
                step = 'end'
            if dirction == 'east' or dirction == 'e':
                chars.move('east',poss)
                step = 'end'
            if dirction == 'west' or dirction == 'w':
                chars.move('west',poss)
                step = 'end'
            if step == 'end':
                action = ''
                
                
        while action == 'shoot' or action == 's':
            score -= 10
            firing = 'start'
            dirction = (input('what dirction do you want to shoot?(north,east,south,west)-->')).lower()
            if dirction == 'north' or dirction == 'n':
                chars.shoot(mapes,'north',poss,chars.wumpas)
                firing = 'end'
            if dirction == 'south' or dirction == 's':
                chars.shoot(mapes,'south',poss,chars.wumpas)
                firing = 'end'
            if dirction == 'east' or dirction == 'e':
                chars.shoot(mapes,'east',poss,chars.wumpas)
                firing = 'end'
            if dirction == 'west' or dirction == 'w':
                chars.shoot(mapes,'west',poss,chars.wumpas)
                firing = 'end'
            if step == 'end':
                action = ''
        while action == 'grab' or action == 'g':
            if mapes[poss[0]][poss[1]] == 'G':
                (chars.gold).append('yes')
                print('you have picked up a bag of gold.')
                (chars.gold).pop(0)
                mapes[poss[0]][poss[1]] = 0
                action = ''
            if mapes[poss[0]][poss[1]] != 'G':
                score -= 1
        while action == 'climb' or action == 'c':
            if poss == [4, 0]:
                if chars.gold == ['yes']:
                    print('you climb the ladder out with a bag of gold.')
                    score += 1000
                    action = ''
                    game_start = 'end'
                if chars.gold == ['no']:
                    print('you climb the ladder out with your life.')
                    score += 100
                    action = ''
                    game_start = 'end'
                
            else :
                score -= 1
                action = ''
                print ('there is no ladder here.')
    re = True
    no = ['no','n']
    yes = ['yes','y']
    while re == True:
        replay = input ('do you want to play agian?-->').lower()
        if replay in no:
            
            check = False
            re= False

        if replay in yes:
            game_start = 'yes'
            re = False
    
print (score,'was your score.')
