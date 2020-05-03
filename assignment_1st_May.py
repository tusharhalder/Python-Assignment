#  Task 1 - Assignment 2

for x in range(2000,3200):
    if x%7 == 0 and x%5!= 0:
        print(x,end=',')

print("end")

#  Task 1 - Assignment 3

first_name =input("Please enter first name ")
last_name = input("Please enter Last Name ")
print(last_name +' ' + first_name)

 # Task 1 - Assignment 4

Formula=(4/3)*(22/7)
r=6
Volume = Formula * r*r*r

print(Volume)

#  Task 2 - Assignment 1

seq_input = input("Please provide a sequence of numbers seperated by comma")
str_split = seq_input.split(",")

list1 = []
for i in range(0,len(str_split)):
    list1.append(str_split[i])
print(list1)

#  Task 2 - Assignment 3
s = 'Y'
while s == 'Y' or s == 'y':
    s = input("You want to reverse word ")
    if s == 'Y' or s == 'y':
        str = input("please enter a word ")
        rev = ""
        for i in range(len(str) -1, -1, -1):
            rev = rev + str[i]
    else:
        break
    print(rev)

#  Task 2 - Assignment 2

for i in range(0, 11):
    if (i <= 5):
        for j in range(0, i):
            print('*', end =' ')
    else:

        for k in range(i,10):
            print('*', end=' ')

    print("\n")

# Task 2 Assignment No 4

Str = "WE,THE PEOPLE OF INDIA,\n having solemnly resolved to constitute India into a " \
"SOVEREIGN, !\n SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n and to secure to all" \
" its citizens"

print(Str)


