import random

# COLLATZ CONJECTURE ALGORITHM

# We take a number. We're going to do one of two things to this number, depending on whether it's odd or even.

# If the number is even, divide by 2
# if the number is odd, x3 + 1.
# count how many times it takes for input number to reach one.

# The Collatz Conjecture argues all positive integers must reach one eventually


def collatz(num):
    count = 0
    while num > 1:
        count += 1
        if num % 2 == 0: # if number is even
            num //= 2 # divide it by 2
            print(num)
        else:
            num = (num * 3) + 1 # multiply by 3 and add one
            print(num)


    print("It took {} iterations for {} to get to 1.".format(count, input_num))


num = int(input("Please enter any number larger than 1: "))
input_num = num
collatz(num)







# Find how many steps it takes for each random # to get to one.