import random

low_number = input("Enter the lowest number in the range")
high_number = input("Enter the highest number in the range")

list_of_number = []

for i in range(int(low_number), int(high_number)+1):
    list_of_number.append(i)


#enter the amount of numbers to be chosen

amount_of_numbers = input("How many numbers do you want to chose? ")
amount_of_numbers = int(amount_of_numbers)


#select first number from list and add to a new list
new_list = []

def pick():
    global amount_of_numbers
    while amount_of_numbers > 0:
        picked = random.choice(list_of_number)
        new_list.append(picked)
        list_of_number.remove(picked)
        amount_of_numbers = amount_of_numbers - 1
pick()
print(new_list)

# remove this number from original list

#repeat for the amount of numbers chosen