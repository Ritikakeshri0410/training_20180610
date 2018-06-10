"""
this file cover following topics
1)Tuples,set boolean data type
2)conditional statements
3)looping statement
4)break and continue



# tuples
my_tuple = ('a', 'b', 'c')

my_list = ['a', 'b', 'c']
my_set = set(['a', 'b', 'x'])
print(my_set)

print(type(set(my_list)), set(my_list))
unique_char = list()

for item in my_list:
    if item in unique_char:
        continue
    unique_char.append(item)

print(unique_char)

if type(my_list) is list:
     print("this is list")


looping

first = int(input("enter first number"))
second = int(input("enter second number"))

for item in range(first, second, 1):
    print(item)


while loop

x = 0
while True:
    if x == 11:
        break

        print(x)
        x += 1

Assignment
1) print maximum value from 2 variables
2)print minimum value from 2 variables
3)print maximum value from 10 variables without using built in functions
4)print minimum value from 10 variables  without using built in functions




 To print maximum between between 2 numbers
"""
"""
first = int(input("enter first number"))
second = int(input("enter second number"))
if first > second:
 print("first number is greater")
else :
 print("second number is greater")
 """

""" to find the minimum between two numbers"""
"""
first = int(input("enter first number"))
second = int(input("enter second number"))
if first < second:
 print("first number is smaller")
else:
 print("second number is smaller")
 """

"""
to find the maximum number among 10 numbers
"""
"""

for item in range(1, 5, 1):
 value = int(input("enter the number"))
 print(item)
if (item )> (item+1):
 print(item)
 print("this is the largest number")
 """


 







