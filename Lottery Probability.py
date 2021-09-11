# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:11:30 2021

@author: jaden
"""

import numpy as np
import random

#max # of iterations
max_iter = 10000000

#create the list of 1-69
array = np.linspace(1,69,69)

#convert to a list
list_numbers = array.tolist()

number_of_test = 5
wins_constant_guess = np.zeros(number_of_test)
number_of_iters_constant_guess = np.zeros(number_of_test)
wins_changing_guess = np.zeros(number_of_test)
number_of_iters_changing_guess = np.zeros(number_of_test)


for i in range(0,number_of_test):

    #select the winners at random
    winners = random.sample(list_numbers, 5)
    #convert to an array for sorting
    winners_array = np.array(winners)
    #Sort the winners from least to greatest
    sorted_winners = np.sort(winners_array)
    #make an array of the sorted winners for the changing guess section
    sorted_winners_changing = sorted_winners

    #####Using the same guess each time#######

    ##create a random guess of numbers that is used for each draw

    #make guess at random
    guess = random.sample(list_numbers, 5)
    #convert to an array for sorting
    guess_array = np.array(guess)
    #Sort the guess from least to greatest
    sorted_guess = np.sort(guess_array)
    #make and array of the sorted guess for the changing guess section
    sorted_guess_changing = sorted_guess
    print("The sorted winners are: ",sorted_winners)
    print("The sorted guess is: ",sorted_guess)


    iteration = 1
    while (not (np.array_equal(sorted_guess,sorted_winners)) and iteration < max_iter):
        #select the winners at random
        winners = random.sample(list_numbers, 5)
        #convert to an array for sorting
        winners_array = np.array(winners)
        #Sort the winners from least to greatest
        sorted_winners = np.sort(winners_array)
        iteration+=1
        if iteration == max_iter:
            max_iter_bool = True
        else:
            max_iter_bool = False

    if max_iter_bool:
        print("\nMaximum iterations reached!")
        wins_constant_guess[i] = 0
    else:
        print("Iterations: ", iteration)
        wins_constant_guess[i] = 1
    number_of_iters_constant_guess[i] = iteration
    print("The final sorted winners from constant guess are: ",sorted_winners)
    print("The sorted guess from constant guess is still: ",sorted_guess)


    #####Random Guess with each draw#####
    iteration_changing = 1
    while (not (np.array_equal(sorted_guess_changing,sorted_winners_changing)) and iteration_changing < max_iter):

        #select the winners at random
        winners_changing = random.sample(list_numbers, 5)
        #convert to an array for sorting
        winners_array_changing = np.array(winners_changing)
        #Sort the winners from least to greatest
        sorted_winners_changing = np.sort(winners_array_changing)

        #####Using the same guess each time#######

        ##create a random guess of numbers that is used for each draw

        #make guess at random
        guess_changing = random.sample(list_numbers, 5)
        #convert to an array for sorting
        guess_array_changing = np.array(guess_changing)
        #Sort the guess from least to greatest
        sorted_guess_changing = np.sort(guess_array_changing)
        iteration_changing+=1

        if iteration_changing == max_iter:
            max_iter_bool_changing = True
        else:
            max_iter_bool_changing = False

    if max_iter_bool_changing:
        print("\nMaximum iterations reached!")
        wins_changing_guess[i] = 0
    else:
        print("Iterations: ", iteration_changing)
        wins_changing_guess[i] = 1
    number_of_iters_changing_guess = iteration_changing
    print("The final sorted winners from random changing guess are: ",sorted_winners_changing)
    print("The final guess from random changing guess is: ",sorted_guess_changing)   