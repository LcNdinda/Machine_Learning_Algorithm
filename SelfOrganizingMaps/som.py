import random
import math
#input vector of nine nodes
#InputVector = [[3, 1.0, 1.0], [2, 0.0, 0.0], [3, 0.0, 2.0]]
InputVector = [3, 1.0, 1.0]
w1 = random.random()
w2 = random.random()
w3 = random.random()
w4 = random.random()
w5 = random.random()
w6 = random.random()

#calculate the Euclidean Distance

Dist1 = ((InputVector[0] -  w1)**2) + ((InputVector[1] -  w2)**2) + ((InputVector[2] -  w1)**2)
Dist1 = math.sqrt(Dist1)
print(f"Distance One is {Dist1}")

Dist2 = ((InputVector[0] -  w4)**2) + ((InputVector[1] -  w5)**2) + ((InputVector[2] -  w6)**2)
Dist2 = math.sqrt(Dist2)
print(f"Distance One is {Dist2}")

# Finding the BMU

if Dist1 < Dist2:
    BMU = Dist1
    print(f"The BMU is {BMU}")
else:
    BMU = Dist2
    print(f"The BMU is {BMU}")

# Determine the radius of the BMU using the decay function
t= 1
R0 = 2
learning_rate = 0.1
l = 0.5
R_decay = R0 * math.exp(-(t/l))
print(f"The new Radius after the decay function is {R_decay}")

#bell curve
bell_curve = math.exp(-((BMU **2)/(2* (R_decay ** 2))))
print(f"The Bell curve equation is {bell_curve}")

#Adjust the weights
newWeight1 = w1 + (bell_curve * learning_rate * (InputVector[0] - w1))
newWeight2 = w2 + (bell_curve * learning_rate * (InputVector[1] - w2))
newWeight3 = w3 + (bell_curve * learning_rate * (InputVector[2] - w3))
newWeight4 = w4 + (bell_curve * learning_rate * (InputVector[0] - w4))
newWeight5 = w5 + (bell_curve * learning_rate * (InputVector[1] - w5))
newWeight6 = w6 + (bell_curve * learning_rate * (InputVector[2] - w6))

print(f"The new weights are {newWeight1}, {newWeight2}, {newWeight3}, {newWeight4}, {newWeight5}, {newWeight6}")

#Adjust Learning learning_rate
Lr1 = learning_rate * math.exp((-t)/l)
print(f"The new learning rate is {Lr1}")
