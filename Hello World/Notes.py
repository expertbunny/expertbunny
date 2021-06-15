#Basic of the python:
print("@Bunny.io")
print('o----')
print(' ||||')
print('*' * 10)

# Variables of the python prgrams and that help to store data in the memory
price = 10
price = 20
rating = 4.9
name_1 = 'Abhishek'
is_published = True or False
print(price)

#Exicese no.1
name_2 = 'jhon smith'
age = 20
is_new = True

name_3 = input('What is your name? ')
print('hi ' + name_3)

#Exicese no.2
name_4 = input('what is your name?')
color = input('what is your favourite color? ')
print(name_4 + ' loves ' + color + ' colors')

# Str and the Int Test
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))
print(age)

# Exicese no.2
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs)  * 0.45
print(weight_kg)

# Strings
Self_Intro = '''
Hi i am Expert Bunny
'''
print(Self_Intro[0:9])

First = 'Smart'
Last = 'bunny'
message = First + '[' + Last + '] is a Expert'
msg = f'{First} [{Last}] is a coder'
print(msg)

Time = 'The time is 12 right now'

len(Time)
Time.upper()
Time.lower()
Time.find(12)
Time.title(Time)
Time.replace()




x = 10
x = x + 3
x += 3
print(x)
x = 10 + 3 * 2
y = 11 + 2 * 3
print(y)
All_is_well = True or False

x = (2 + 3) * 10 - 3
print(x)

import math

print(math.floor(2.9))

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("Wear warm clothes")
else:
    print("It is a lovely day")
print("Enjoy your day")


price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down_payment: ${down_payment}")


has_high_income = True
has_good_credits = True

if has_high_income and has_good_credits:
    print("Eligiable for loan")


has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligiable for loan")



Temperature = 10

if Temperature < 10:
    print("It's a cold day")
if Temperature > 30:
    print("It's a hot day")
else:
    print("it's not a hot day")


name = "smart"

if len(name) < 3:
    print('name must be at the least 3 characters')
elif len(name) > 50:
    print('name can be maximum of 50 characters')
else:
    print('name looks good!')


weigth = int(input("Weight: "))
unit = input('(L)bs or (k)g')
if unit.upper() == "L":
    coverted = weigth * 0.45
    print(f"You are {coverted} kilos abhishek")
else:
    coverted = weigth / 0.45
    print(f"You are {coverted} pounds abhishek")


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count <guess_limit:
     guess = int(input('Guess: '))
     guess_count += 1
     if guess == secret_number:
         print("You Won!")
         break
else:
    print("Sorry, you failed!")


