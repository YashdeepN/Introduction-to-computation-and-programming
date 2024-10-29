sum = 0
prime_num = 0
for number in range(3,1000, 2):
    is_prime = True
    for odd_number in range(3, number//2, 2):
        if number % odd_number == 0:
            is_prime = False
            break
    if is_prime: 
        sum += number
        
print(sum)

