########################################################################
##
## CS 101
## Program #makeup
## Name: Colby Chandler
## Email: crcn96@mail.umkc.edu
##
## PROBLEM : recurcive intagral.
##
## ALGORITHM : 
##      1. get point a and b with the toalurance.
##      2. intgrate with them 
##      3. print out the info
##      
##       
## 
## 
##
## 
########################################################################


def f(floats):
    eqation = (floats**2)
    return eqation
def exact(a,b):
    exa = (b**3/3)-(a**3/3)
    return exa
def total(ver):
    total = 0
    
    for item in ver:
        if item == ver[0]:
            total += f(item)
            
        if item != ver[0] or item != ver[-1]:
            total += (2*f(item))
        else:
            total += f(item)
    return total

def intgrate(a,b,varation):
    global splits
    global exacts
    global ingrate
    full_range = StepRange(a,b,splits)
    left = StepRange(a,(b/2)-splits,splits)
    right= StepRange(b/2,b,splits)
    left_total = total(left)
    right_total = total(right)
    
    ingrate = ((b-a)/(2*(len(full_range))))*(left_total+right_total)
    
    if ingrate < exacts+varation and ingrate > exacts-varation:
        return 
    else:
        splits = splits / 2
        
        intgrate(a,b,varation)
    


def StepRange(start, stop, step):
    r = [start]
    cnt = start
    while cnt < stop:
        cnt += (step)
        r.append(cnt)
    return r
check = True
while check == True:
    try:
    
        a = float(input ('starting point-->'))
        check = False
    except ValueError:
        print ('Please enter a number and the number should be less then than b.')
        continue
check = True
while check == True:
    try:
    
        
        b = float(input ('end point-->'))
        if b < a:
            print ('enter a number greater than a.')
        else:
            check = False
    except ValueError:
        print ('Please enter a number and the number should be greater than a.')
        continue
check = True
while check == True:
    try:
    
        vera = float(input('how much toalernce to you want?-->'))
        
        if vera < 0:
            vera = vera * -1
            check = False
        if vera == 0:
            vera = 0.01
            check = False
        else:
            check = False
    except ValueError:
        print ('please enter a number')
        continue
    
splits = 1
exacts = exact(a,b)
ingrate = 0
intgrate(a,b,vera)

diff = exacts - ingrate
print('''Estimated area under x**2 from {} to {} within {} is: {:.8f}
exact amount is {:.8f}, difference = {:.8f}.'''.format(a,b,vera,ingrate,exacts,diff))
