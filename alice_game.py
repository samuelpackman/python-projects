import cmath as cm
import numpy as np
import random as rd

probs = [3/4,13/16,1/2,1/4]#(np.array([11,11,11,11,11,11,0,0,0,0,0,0]) + np.array([0,1,2,3,4,5,6,5,4,3,2,1]))/36

def roll_dice():
    list1 = [rd.randint(1,2),rd.randint(1,2)]
    return list1 + [sum(list1)]


cards = [0 for i in range(4)]

def turn():
    roll = roll_dice()
    max_choice = probs.index(max([probs[i-1] for i in roll]))
    for i in range(3):
        if cards[roll[i]-1] == 1:
            roll[i] = 0
    if roll == [0,0,0]:
        choice = max_choice
    else:
        choice = probs.index(min([probs[i-1] for i in roll if i]))
    cards[choice] = 1 - cards[choice]

def play_game():
    global cards, have_won, number_turns
    cards, have_won, number_turns = [0 for i in range(4)], False, 0
    while not have_won:
        turn()
        #print(cards)
        number_turns += 1
        if cards == [1 for i in range(4)]:
            have_won = True
    return number_turns

#print(play_game())
average = 0

for i in range(10**4):
    average += play_game()

print(average/10**4)
