import math
# Back Propagation using chain rule
# initialize weigths
'''
w1 to w12 Weights in the hidden layer w18, w17 and w18 weights to the output layer
'''

w1 = 0.0
w2 = 0.1
w3 = 0.2
w4 = 0.3
w5 = 0.4
w6 = 0.5
w7 = 0.6
w8 = 0.7
w9 = 0.8
w10 = 0.9
w11 = 0.11
w12 = 0.12
w13 = 0.13
w14 = 0.14
w15 = 0.15
w16 = 0.16
w17 = 0.17
w18 = 0.18
w19 = 0.19

#Initialize Inputs
Inputs = [0.9, 1.0, 0.5, 0.4, 0.5]
# Initiale Bias
B1 = 1
B2 = -1

neth1 = (w1*Inputs[0]) + (w4*Inputs[1]) + (w7*Inputs[2]) + (w10*Inputs[3]) + (w13*B1)
print(f"The Net H1 is {neth1}")
Outh1 = 1/(1 + math.exp(-neth1))
print(f"The Out H1 is {Outh1}")

neth2 = (w2*Inputs[0]) + (w5*Inputs[1]) + (w8*Inputs[2]) + (w11*Inputs[3]) + (w14*B1)
print(f"The Net H2 is {neth2}")
Outh2 = 1/(1 + math.exp(-neth2))
print(f"The Out H2 is {Outh2}")
