# Defining h
h1 = 1 #yes
h2 = 0 #no

# Learning phase - Calculating probabilities
#outlook
sunny = [2/9,3/5]
overcast = [4/9,0/5]
rain = [3/9, 2/5]

#Temperature
hot = [2/9, 2/5]
mild = [4/9, 2/5]
cool = [3/9, 1/5]

#Humidity
high = [3/9, 4/5]
normal = [6/9, 1,5]

#wind
strong = [3/9, 3/5]
Weak = [6/9, 2/5]

# Test phase
#instance(outlook = sunny, Temperature = cool, Humidity = High, Wind = Strong)

P(sunny|yes) = sunny[0]
P(sunny|no) = sunny[1]
P(cool|yes) = cool[0]
P(cool|no) = cool[1]
P(high|yes) = high[0]
P(high|no) = high[1]
P(strong|yes) = strong[0]
P(strong|no) = strong[1]




def MaximumPosterior:
    #p(h|D) = p(D|h).p(h)
    pass

def MaximumLikelihood:
    #p(h|D) = p(D|h)
    pass
