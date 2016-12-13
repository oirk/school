import math

def deflatlong(lat1,long1,lat2,long2):
         deltaLong = math.radians(long2) - math.radians(long1)
         deltaLat  = math.radians(lat2)  - math.radians(lat1)
         a         = (math.sin((deltaLat/2))**2) + (math.cos(math.radians(lat1))) * (math.cos(math.radians(lat2))) * (math.sin((deltaLong/2))**2)
         c         = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a)) 
         d         = 3961 * c #3961 is the radius of the earth in miles.
         return d
start = True
while start == True :
    try:
        stop_block = 0
        if stop_block == 0 :
            lat_long_1=((input('what is your frist lat? ')),(input('what is your frist long? ')))
            radius      = float(input('what is the radius you want to use?'))
            if float(lat_long_1[0])< -90 or float(lat_long_1[0])>90:
                print('enter a number between -90 and 90 for your lat.')
            if float(lat_long_1[1])< -180 or float(lat_long_1[1])>180:
                print('enter a number between -180 and 180 for your long.')
            stop_block = 1
        if stop_block == 1:
            Start = False
    except ValueError:
        print('please enter a number')
    except TypeError:
        print('type error')
        continue
    
while True:
    try:
        stop_block = 0
        if stop_block == 0 :
            source_file = open(input('what is the source file do you want to use?' ) + '.txt')
            stop_block = 1
    except FileNotFoundError:
        stop_block = 0
        print('Please enter a vaild file name.')
    if stop_block == 1:
        False





write_file  = open((input('what file do you want to write to?' ) + '.txt'),'w',encoding = 'utf-8')
lat_long_2 = []
check_loop = True
source_file.readline()
while check_loop == True:
    try:
        for line in source_file:
            lat_long_2 = []
            lat_long_2.append(line[135:149])
            lat_long_2.append(line[150:165])
            
            defra      = deflatlong(float(lat_long_1[0]),float(lat_long_1[1]),float(lat_long_2[0]),float(lat_long_2[1]))
            
            if  defra <= radius:
                write_file.write(line)
    except ValueError:
        continue
    check_loop = False                   
                       
source_file.close()
write_file.close()
