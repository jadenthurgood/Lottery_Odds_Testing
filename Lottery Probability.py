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

number_of_test = 30
wins_constant_guess = np.zeros(number_of_test)
number_of_iters_constant_guess = np.zeros(number_of_test)
wins_changing_guess = np.zeros(number_of_test)
number_of_iters_changing_guess = np.zeros(number_of_test)


for i in range(0,number_of_test):

    print("Starting test number: ",i)
    #select the winners at random
    winners = random.sample(list_numbers, 5)
    #convert to an array for sorting
    winners_array = np.array(winners)
    #Sort the winners from least to greatest
    sorted_winners = np.sort(winners_array)
    #make an array of the sorted winners for the changing guess section
    sorted_winners_changing = sorted_winners

    #####Using the same guess each time#######
    print("\n***Starting Constant Guess:")
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
        print("\nIterations: ", iteration)
        wins_constant_guess[i] = 1
    number_of_iters_constant_guess[i] = iteration
    print("The final sorted winners from constant guess are: ",sorted_winners)
    print("The sorted guess from constant guess is still: ",sorted_guess)

    print("\n***Starting Random Guess:")
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
        print("\nIterations: ", iteration_changing)
        wins_changing_guess[i] = 1
    number_of_iters_changing_guess[i] = iteration_changing
    print("The final sorted winners from random changing guess are: ",sorted_winners_changing)
    print("The final guess from random changing guess is: ",sorted_guess_changing)

#Compute the probabilities
number_of_wins_constant = np.sum(wins_constant_guess)
number_of_wins_changing = np.sum(wins_changing_guess)
number_of_losses_constant = number_of_test - number_of_wins_constant
number_of_losses_changing = number_of_test - number_of_wins_changing

win_freq_constant = number_of_wins_constant/number_of_test
win_freq_changing = number_of_wins_changing/number_of_test

#Smaller number means a better probability
win_metric_constant = ((np.sum(number_of_iters_constant_guess) - (number_of_losses_constant*max_iter))/(max_iter*number_of_test))
win_metric_changing = ((np.sum(number_of_iters_changing_guess) - (number_of_losses_changing*max_iter))/(max_iter*number_of_test))

#Probaility
win_prob_constant = (number_of_wins_constant/(max_iter*number_of_test))*100
win_prob_changing = (number_of_wins_changing/(max_iter*number_of_test))*100

#save the results to a text file
np.savetxt("results.txt",[wins_constant_guess,wins_changing_guess,number_of_iters_constant_guess,number_of_iters_changing_guess])
np.savetxt("probabilities.txt",[win_freq_constant,win_freq_changing,win_metric_constant,win_metric_changing,win_prob_constant,win_prob_changing])

print("\n\nWin Frequencies (constant, changing): ",[win_freq_constant,win_freq_changing])
print("Win Metric (constant, changing): ",[win_metric_constant,win_metric_changing])
print("Win Percentages (constant, changing): ",[win_prob_constant,win_prob_changing])