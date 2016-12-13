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

class maps(object):
    def surrounding(mapes,pos):
        dirctions = ['north','south','east','west']
        
        for item in dirctions:
            if item == 'north':
                check = [pos[0]-1,pos[1]]
                if check[0] > 4 or check [0] < 0:
                    check = [pos[0],pos[1]]
                if mapes[check[0]][check[1]] == 'p':
                    print('you feel a breeze.')
                if mapes[check[0]][check[1]] == 'W':
                    print('you smell a stench.')
                if mapes[check[0]][check[1]] == 'Ω':
                    print('you smell a stench')
                    print('you feel a breeze.')
                    
                if mapes[pos[0]][check[1]] == 'G':
                    print('you see a glint.')
                if mapes[check[0]][check[1]] == '3':
                    print('you smell a stench')
                    print('you feel a breeze.')
            if item == 'south':
                check = [pos[0]+1,pos[1]]
                if check[0] > 4 or check [0] < 0:
                    check = [pos[0],pos[1]]
                if mapes[check[0]][check[1]] == 'p':
                    print('you feel a breeze.')
                if mapes[check[0]][check[1]] == 'W':
                    print('you smell a stench.')
                if mapes[check[0]][check[1]] == 'Ω':
                    print('you smell a stench')
                    print('you feel a breeze.')
                    
                if mapes[pos[0]][check[1]] == 'G':
                    print('you see a glint.')
                if mapes[check[0]][check[1]] == '3':
                    print('you smell a stench')
                    print('you feel a breeze.')

            if item == 'east':
                check = [pos[0],pos[1]+1]
                if check[1] > 4 or check [1] < 0:
                    check = [pos[0],pos[1]]
                if mapes[check[0]][check[1]] == 'p':
                    print('you feel a breeze.')
                if mapes[check[0]][check[1]] == 'W':
                    print('you smell a stench.')
                if mapes[check[0]][check[1]] == 'Ω':
                    print('you smell a stench')
                    print('you feel a breeze.')
                    
                if mapes[check[0]][pos[1]] == 'G':
                    print('you see a glint.')
                if mapes[check[0]][check[1]] == '3':
                    print('you smell a stench')
                    print('you feel a breeze.')
            if item == 'west':
                check = [pos[0],pos[1]-1]
                if check[1] > 4 or check [1] < 0:
                    check = [pos[0],pos[1]]
                if mapes[check[0]][check[1]] == 'p':
                    print('you feel a breeze.')
                if mapes[check[0]][check[1]] == 'W':
                    print('you smell a stench.')
                if mapes[check[0]][check[1]] == 'Ω':
                    print('you smell a stench')
                    print('you feel a breeze.')
                    
                if mapes[check[0]][pos[1]] == 'G':
                    print('you see a glint.')
                if mapes[check[0]][check[1]] == '3':
                    print('you smell a stench')
                    print('you feel a breeze.')
                
