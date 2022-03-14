"""
Project created to work on examples before first project.
main.py contains:
-range

"""
# Range summary

a = range(10)
print(a)
print(list(a))

b = range(3, 9)
print(list(b))

c = range(1, 22, 2)
print(list(c))

##################
# while

COUNTER = 0

while COUNTER<10:
    print(COUNTER)
    COUNTER += 1

##################
# print and formatted strings
course_name = "Pycamp"
print(f'Hello {course_name}')

salary = 2363.56
hours = 160
print(f'{salary/hours:.2f}')

print('-' * 30)

total_salary = salary * 12 * 36
print(f'{total_salary:,}')

###################
# set
my_set = set()
my_set2 = {1, 2, 3}
my_set_false = {} #list

my_list = [1, 3, 2]
new_list = [1, 2, 3]

if my_list == new_list:
    print("ok")
else:
    print("not ok")

my_set = {1, 2, 3}
new_set = {1, 3, 2}

print(type(my_set))
print(my_set)


if my_set == new_set:
    print("ok")
else:
    print("not ok")

###################
# list

my_list = [1, 2, 3, 'Adam']

my_list.append('Kacper')

print(my_list)

for x in my_list:
    print(x)

###################
# functions

def sum_numbers(a, b):
    print('Suma wynosi:', a + b)


def calculate_brutto(netto, vat=0.23):
    return netto + vat * netto


sum_numbers(3, 5)
print(calculate_brutto(100))

###################
# pylint
#in terminal use python -m pylint file_name.py
#global variable should be uppercase


###################
#pytest

def my_sum(a, b):
    return a + b

###################
#function as parameter

def do_something(numbers, function):
    return function(numbers)

def to_negative(number):
    return number * -1

def change_to_negative(numbers):
    
    # new_list = []
    # for number in numbers:
    #     new_list.append(number * -1)

    # return new_list
    return list(map(to_negative, numbers))

print(do_something([1, 2, 3, 4, 5], sum))

print(do_something([1, 2, 3, 4, 5], change_to_negative))

######################################
#List comprehension
my_list = [1, 2, 3]

#new_list = [2, 4, 6]

#new_list = []
#for x in my_list:
#    new_list.append(x*2)

new_list = [x * 2 for x in my_list]

######################################
#Walrus
choice = None

def do_job():
    print(choice)

while choice != 0:
    choice = int(input())
    if choice != 0:
        do_job()

while choice !=0:
    if (choice := int(input())) != 0:
        do_job()





