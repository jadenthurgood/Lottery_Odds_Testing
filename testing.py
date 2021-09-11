import numpy as np

number_of_test = 5
wins_constant_guess = np.zeros(number_of_test)
number_of_iters_constant_guess = np.zeros(number_of_test)
wins_changing_guess = np.zeros(number_of_test)
number_of_iters_changing_guess = np.zeros(number_of_test)


for i in range(0,number_of_test):
    wins_constant_guess[i] = i
    continue

print(wins_constant_guess)