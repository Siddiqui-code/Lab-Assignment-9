# Nousheen Siddiqui
# 03/11/2021
# Create a while loop that initializes a counter at 0 and will run until the counter reaches 50.
# If the value of the counter is divisible by 10, append the value to the list called tens.
# Confirm the list results using a print statement.

#while x < 5:
    #x += 1
    #print(x)

counter = 0
tens = []

while counter <=50:
    if counter % 10 == 0:
        tens.append(counter)
        print(tens)
    counter += 1


