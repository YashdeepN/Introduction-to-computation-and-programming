index = 0
max = 0

while index < 10:
    x = int(input(f"Number {index + 1}: "))
    if x  % 2 != 0 and x > max:
        max = x
    index += 1

if max: 
    print(max)
else:
    print("No odd number.")