#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:58:28 2019

@author: trinity
"""

print('Please think of a number between 0 and 100!')
high = 100
low = 0
guess = 50
result = None
while result != 'c':
    print('Is your secret number ' + str(guess) + '?')
    result = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if result == 'h':
        high = guess
    elif result == 'l':
        low = guess
    elif result == 'c':
        break
    else: 
        print('Sorry, I did not understand your input.')
    guess = int((high - low)/2) + low
print('Game over. Your secret number was: ' + str(guess))