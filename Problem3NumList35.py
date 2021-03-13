# Nousheen Siddiqui
# 03/11/2021
# Using a while loop, ask the user to enter a number.
# Append each entered number to a list and add them together.
# Continue asking for a number until the sum of the list of numbers is greater than 100
list = []
sum_list = 0
while sum_list<=100:
    user = int(input("Enter a number"))
    list.append(user)
    for i in list:
        sum_list = sum_list + i
        #print(i)
    print(sum_list)
