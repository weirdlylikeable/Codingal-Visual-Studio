def guess_number():
    print("Think of a number between 1 and 100, and I will try to guess it!")
    low, high = 1, 100

    while True:
        guess = (low + high) // 2
        print("My guess is:", guess)
        response = input("Is it (h)igh, (l)ow, or (c)orrect?:").lower()

        if response == 'c':
            print("Yay! I guessed your number:", guess)
            break
        elif response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess + 1
        else:
            print("Please respond with 'h', 'l', or 'c'.")

guess_number()