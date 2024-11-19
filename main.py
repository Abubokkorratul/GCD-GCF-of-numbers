numbers = list(map(int, input("Enter numbers separated by space (2 to 4 numbers): ").split()))
if len(numbers) < 2 or len(numbers) > 4:
    print("Error: Please enter between 2 to 4 numbers.")
else:
    gcd = numbers[0]
    for num in numbers[1:]:
        while num:
            gcd, num = num, gcd % num
    print("GCD/GCF of the given numbers:", gcd)
