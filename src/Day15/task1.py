import random

# number of trials
trials = 1000

count_sum_7 = 0

# simulate rolling two dice
for i in range(trials):
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    total = dice1 + dice2
    
    if total == 7:
        count_sum_7 += 1

# experimental probability
probability = count_sum_7 / trials

print("Number of trials:", trials)
print("Number of times sum = 7:", count_sum_7)
print("Experimental Probability:", probability)
