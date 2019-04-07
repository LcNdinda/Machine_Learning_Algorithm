

import random

w1 = random.random()
w2 = random.random()
w3 = random.random()
print(f"Weight one is {w1}, Weight two is {w2} and weight three is {w3}")

Weights = [w1, w2, w3]
t= 0.5 # Threshold value
n = 0.1
#Epoch label[I1,I2,I3,Output]
Epoch_input = [[-1,0,0,0],[-1,0,1,0], [-1,1,0,0], [-1,1,1,1]]

for input in Epoch_input:
    summation = (Weights[0] * input[0]) + (Weights[1] * input[1]) + (Weights[2] * input[2])

    print(f"Total summation is {summation}")
    #Activation Function
    if summation > t:
        y = 1
    else:
        y = 0
    error = input[3] - y
    print(f"The error is {error}")

    if error >= 1:
        new_w1 = Weights[0] + (n*t*input[0])
        new_w2 = Weights[1] + (n*t*input[1])
        new_w3 = Weights[0] + (n*t*input[0])
        print(new_w1)
    else:
        Weights = Weights
        print(Weights)
