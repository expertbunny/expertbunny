x = 10
y = 10
z = 20
print(x + y + z)


size = 40
if size == 40:
    print('Yes the size is 40')
else:
    print('this is not the size')

lenght = int(input("Lenght: "))
unit = input('(C)m or (M)')
if unit.upper() == "C":
    converted = lenght / 1000
    print(f"The Lenth is {converted} M")
else:
    converted = lenght * 1000
    print(f"Lenght is {converted} CM")

print('hi i am ')
