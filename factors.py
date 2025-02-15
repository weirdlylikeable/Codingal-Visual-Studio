def print_factors(number):
    print("The factors of the number ", number, "are:")
    for i in range(1,number+1):
        if number % i == 0:
            print(i)

print_factors(6)