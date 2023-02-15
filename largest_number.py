numbers = [7, 93, 2, 45, 100, 32, 77]              # create a list

def larg_number(numbers):                          # this defines what your recursion is going to do
    if len(numbers) == 1:
        return numbers[0]
    else:
        return max(numbers[0], larg_number(numbers[1: ]))


print(f"The highest number on the list is {larg_number(numbers)}")   # print the results