# Task 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == b:
    print("Numbers are equal")
else:
    print("Numbers are not equal")
    if a > b:
        print("First Number is greater than second")
    else:
        print("Second number is greater than first")
    if a >= 0 and b >= 0:
        print("Both Numbers are positive")
    elif a >= 0 and b < 0:
        print("First number is positive, second number is negative")
    elif a < 0 and b >= 0:
        print("First number is negative, second number is positive")
    else:
        print("Both numbers are negative")
if a % 2 == 0:
        print("First is an Even number")
else:
        print("First is an Odd number")
if b % 2 == 0:
        print("Second is an Even number")
else:
        print("Second is an Odd number")
# Had to put the following here because if was breaking if after the digit count functions below. No idea why
if a <= 1:
    is_prime = False
else:
    is_prime = True
    for x in range(2, int(a ** 0.5) + 1):
        if a % x == 0:
            is_prime = False
            break
if is_prime:
    print("First is a prime number.")
else:
    print("First is not a prime number.")
if b <= 1:
    is_prime2 = False
else:
    is_prime2 = True
    for y in range(2, int(b ** 0.5) + 1):
        if b % y == 0:
            is_prime2 = False
            break
if is_prime2:
    print("Second is a prime number.")
else:
    print("Second is not a prime number.")
# Had to add the following abs because it was breaking with negative numbers
if a < 0:
    a = int(abs(a))
if b < 0:
    b = int(abs(b))
count1 = 0
while a != 0:
    a //= 10
    count1 += 1
print("First number has", int(count1), "digits.")
count2 = 0
while b != 0:
    b //= 10
    count2 += 1
print("Second number has", int(count2), "digits.")
# Big number when it has more than 2 digits
if count1 > 2:
    print("First number is a 'big' number")
else:
    print("First number is a 'small' number")
if count2 > 2:
    print("Second number is a 'big' number")
else:
    print("Second number is a 'small' number")







