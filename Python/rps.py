#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:00:20 2019

@author: abdi

"""

import random

list1 = ['p','r','s']

player1 = random.choice(list1)

player2 = random.choice(list1)

print("Player 1 chose " + player1 + "!")
print("Player 2 chose " + player2 + "!")


if player1 == player2:
    print("Tie!")
    
elif ((player1 == "p" and player2 == "r")
    or(player1 == 's' and player2 == 'p')
    or(player1 == 'r' and player2 == 's')):
     print("Player 1 Wins!")

else: 
     print("Player 2 Wins!")
     
        
    

    
    

 