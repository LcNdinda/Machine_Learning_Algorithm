import csv

Play_Tennis_Yes = 0
Play_Tennis_No = 0
Sunny_Yes = 0
Sunny_No = 0
Rain_Yes =  0
Rain_No = 0
Overcast_Yes = 0
Overcast_No =0
Hot_Yes = 0
Hot_No = 0
Cool_Yes = 0
Cool_No = 0
Mild_Yes = 0
Mild_No = 0
High_Yes = 0
High_No = 0
Normal_Yes = 0
Normal_No = 0
Strong_Yes = 0
Strong_No = 0
Weak_No = 0
Weak_Yes = 0
count = 0
with open('naive.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    if csv.Sniffer().has_header:
        next(csv_reader)
    for line in csv_reader:
        print(line)
        count +=1
        print(count)
# Calculating the probability of Yes and No
        if line[5] == 'Yes':
            Play_Tennis_Yes +=1
            if line[1] == 'Sunny':
                Sunny_Yes += 1
            if line[1] == 'Overcast':
                Overcast_Yes += 1
            if line[1] == 'Rain':
                Rain_Yes += 1
            if line[2] == 'Hot':
                Hot_Yes += 1
            if line[2] == 'Mild':
                Mild_Yes += 1
            if line[2] == 'Cool':
                Cool_Yes += 1
            if line[3] == 'High':
                High_Yes += 1
            if line[3] == 'Normal':
                Normal_Yes += 1
            if line[4] == 'Strong':
                Strong_Yes += 1
            if line[4] == 'Weak':
                Weak_Yes += 1
        elif line[5] == 'No':
            Play_Tennis_No += 1
            if line[1] == 'Sunny':
                Sunny_No += 1
            if line[1] == 'Overcast':
                Overcast_No += 1
            if line[1] == 'Rain':
                Rain_No += 1
            if line[2] == 'Hot':
                Hot_No += 1
            if line[2] == 'Mild':
                Mild_No += 1
            if line[2] == 'Cool':
                Cool_No += 1
            if line[3] == 'High':
                High_No += 1
            if line[3] == 'Normal':
                Normal_No += 1
            if line[4] == 'Strong':
                Strong_No += 1
            if line[4] == 'Weak':
                Weak_No += 1
        else:
            print("Error")
print(f"The probability of Yes is {Play_Tennis_Yes}/{count}")
print(f"The probability of No is {Play_Tennis_No}/{count}")

print("Enter Your Recorded Weather")
print("Select Outlook: 1.Sunny 2.Overcast 3.Rain")
Input_Outlook = input()
print("Select Temperature: 1.Hot 2.Cool 3.Mild")
Input_Temperature = input()
print("Select Humidity: 1.High 2.Normal")
Input_Humidity = input()
print("Select Wind: 1.Strong 2.Weak")
Input_Wind = input()


if Input_Outlook == 1:
    Outlook = Sunny
elif Input_Outlook == 2:
    Outlook = 'Overcast'
else:
    Outlook = 'Rain'

if Input_Temperature == 1:
    Temperature = 'Hot'
elif Input_Temperature == 2:
    Temperature = 'Cool'
else:
    Temperature = 'Mild'

{
 Temperature: 45
}
if Input_Humidity == 1:
    Humidity = 'High'
else:
    Humidity = 'Normal'

if Input_Wind == 1:
    Wind = 'Strong'
else:
    Wind = 'Weak'

x1 = Outlook +_Yes

print(x1)
print(x1*2)
#MAP_Yes = ((int(Outlook)_Yes)/Play_Tennis_Yes) * (Cool_Yes/Play_Tennis_Yes) * (High_Yes/Play_Tennis_Yes) * (Strong_Yes/Play_Tennis_Yes)) * (Play_Tennis_Yes/count)










# Calculating Probability using MAP
MAP_Yes = ((Sunny_Yes/Play_Tennis_Yes) * (Cool_Yes/Play_Tennis_Yes) * (High_Yes/Play_Tennis_Yes) * (Strong_Yes/Play_Tennis_Yes)) * (Play_Tennis_Yes/count)
MAP_No = ((Sunny_No/Play_Tennis_No) * (Cool_No/Play_Tennis_No) * (High_No/Play_Tennis_No) * (Strong_No/Play_Tennis_No)) * (Play_Tennis_No/count)
print(f"Probability of yes using MAP {MAP_Yes}")
print(f"Probability of No using MAP {MAP_No}")


#Calculating Probability using ML
ML_Yes = ((Sunny_Yes/Play_Tennis_Yes) * (Cool_Yes/Play_Tennis_Yes) * (High_Yes/Play_Tennis_Yes) * (Strong_Yes/Play_Tennis_Yes))
ML_No = ((Sunny_No/Play_Tennis_No) * (Cool_No/Play_Tennis_No) * (High_No/Play_Tennis_No) * (Strong_No/Play_Tennis_No))
print(f"Probability of yes using ML {ML_Yes}")
print(f"Probability of No using ML {ML_No}")
