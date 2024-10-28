x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

"""
if x > y and x > z:
    first_number = x
elif y > z:
    first_number = y
else: 
    first_number = z

if first_number == x:
    if y > z:
        second_number, third_number = y, z
    else:
        second_number, third_number = z, y
elif first_number == y:
    if x > z:
        second_number, third_number = x, z
    else:
        second_number, third_number = z, x
else:
    if x > y:
        second_number, third_number = x, y
    else:
        second_number, third_number = y, x

if first_number % 2 != 0:
    print(first_number)
elif second_number % 2 != 0:
    print(second_number)
else:
    print(third_number) """


answer = min(x, y, z)
if x % 2 != 0:
    answer = x
if y > answer and y % 2 != 0:
    answer = y
if z > answer and z % 2 != 0:
    answer = z
print(answer)