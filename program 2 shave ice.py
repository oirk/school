########################################################################
##
## CS 101
## Program #2
## Name: Colby Chandler
## Email: crcn96@mail.umkc.edu
##
## PROBLEM : selling snow cones for 10 days
##
## ALGORITHM : 
##      1. get number of cones to sell
##      2. get price of each cone
##      3. find how many sold
##      4. add profit or loss to bank amount
##      5. do for 10 days or when out of money
## 
## 
##
## 
########################################################################

import random
import math 

def weather():
         global raining
         raining = random.randint(1,10)
         if raining == 1:
                  raining = 'raining'
         else :
                  raining = 'clear'
def temperature():
         global temp
         temp = random.randint(70,110)
         
def cone():
         global max_cones
         global cones
         number_cones = False
         while number_cones == False:
                  
                  cones = int(input('How many cones do you want to make->'))
                  if cones <= 0:
                           print ('Please enter a number higher then 0')
                           continue
                  if cones > max_cones:
                           print ('Please enter a number less then or equal to',int(max_cones),'.')
                           continue
                  else :
                           number_cones = True
def price():
         global prices
         number = False
         while number == False:
                  prices = float(input('How much do you want to sell your cones for?'))
                  if prices <= 0:
                           print ('Please enter a number higher then 0')
                           continue
                  else:
                           number = True

def max_customers(raining,temp,prices):
         global MaxCustomers
         MaxCustomers = int((temp - 70) * 0.5 / prices)
         
         if raining == 'yes':
                  MaxCustomers = int(MaxCustomers/2)
def sold (cones,MaxCustomers):
         if cones < MaxCustomers:
                  return cones
         else :
                  return MaxCustomers
def play ():
         
         ytup = ('Y','YES')
         ntup = ('N','NO')
         tup = ('N','NO','Y','YES')
         while True:
                  playing = input('Do you want to play agian->').upper()
                  
                  if playing not in tup:
                           print ('Please enter Y/YES/N/NO')
                           continue
                  
                  if playing in ytup:
                           return True
                  if playing in ntup:
                           return False
         
         
play_agian   = True        

header       = '''

it is day {2} and you have ${3:.2f} in the bank.
It is {0} and the temperature is {1} degress'''
footer       = '''
You made {0} cones of shaved ice costing ${1:.2f}.
you sold {2} taking in ${3:.2f} and for the daily profit/loss is ${4:.2f}'''
while play_agian == True:
         days         = 0        
         bankroll     = 5
         raining      = ''
         temp         = 0
         cones        = 0
         prices       = 0
         MaxCustomers = 0
         while bankroll >= 0.5 and days < 10:
                  days += 1
                  weather()
                  temperature()
                  print (header.format(raining,temp,days,bankroll))
                  max_cones    = int(bankroll / 0.5)
                  cone()
                  price()
                  max_customers(raining,temp,prices)
                  
                  cones_sold   = sold(cones,MaxCustomers)
                  cost         = cones * .5
                  taking       = cones_sold * prices
                  profit_loss  = taking - cost//1
                  print (footer.format(cones,cost,cones_sold,taking,profit_loss))
                  bankroll += profit_loss
                  if bankroll < 0.5 :
                           print ('you do not have enough in the bank to make anymore shaved ice. Thanks for playing')
                           
                  
         print ('you played',days,'days of the simulatiation and ended with $',bankroll,'.')
         play_agian = play() 
print ('Thanks for playing')
