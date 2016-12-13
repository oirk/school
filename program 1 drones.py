def basic  (number):
         global Rotor
         global Motor
         global wire
         Rotor += 4     *number
         Motor += 2     *number
         wire  += 4.2   *number
def Good   (number):
         global Rotor
         global Motor
         global wire
         global camera
         Rotor += 4     *number
         Motor += 4     *number
         wire  += 9     *number
         camera+= 1     *number
def ridic  (number):
         global Rotor
         global Motor
         global wire
         global camera
         Rotor += 8     *number
         Motor += 12    *number
         wire  += 22.4  *number
         camera+= 5     *number



Rotor  = 0
Motor  = 0
wire   = 0
camera = 0

basic(int(input('How many basic drones do you want?-->')))
Good(int(input('How many good drones do you want?-->')))
ridic(int(input('How many Ridiculous drones do you want?-->')))

order =  '''


you will need to order
{0} rotors
{1} motors
{2} cameras
{3} Feet of wire'''

print(order.format(Rotor,Motor,camera,wire))

