import numpy as np

input1 = 123 #3141592653589793238462643383279502884197169399375105820974944593

input2 = 120 #2718281828459045235360287471352662497757247093699959574966967623

def get_number_length(number):
    return len(str(number))

def get_each_half_of_number(number):
    length = get_number_length(number) // 2
    # length = length // 2 + 1 if length % 2 != 0 else length // 2
    # a = int(str(number)[:length])
    # b = int(str(number)[length:])
    a = number // 10**length
    b = number % 10**length

    return a, b

def recursive_multiplication(x, y):
    number_length = get_number_length(x)
    if number_length > 1:
        a, b = get_each_half_of_number(x)
        c, d = get_each_half_of_number(y)
        ac = recursive_multiplication(a, c)
        bd = recursive_multiplication(b, d)
        step3 = recursive_multiplication(a + b, c + d)
        gauss_trick = step3 - ac - bd
        if number_length % 2 != 0:
            final_number_length1 = len(str(a))
            final_number_length2 = number_length - final_number_length1
        else:
            final_number_length1 = number_length
            final_number_length2 = number_length // 2
        output = (10**final_number_length1) * ac + 10**final_number_length2 * gauss_trick + bd
        return output
    return x * y

result = recursive_multiplication(input1, input2)
print(result)




