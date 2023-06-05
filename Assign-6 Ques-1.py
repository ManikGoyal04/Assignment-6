def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

number = int(input("Enter a number: "))
if is_perfect(number):
    print(number, "is a perfect number")
else:
    print(number, "is not a perfect number")
