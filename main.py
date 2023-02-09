def hopeless_func():
    for i in range(10):
        for j in range(20):
            if i % 2 == 0 and j < i or j == 11:
                i += 1
    return 'Done'



def add_numbers(a, b):
    result = a + b
    return result

def add_numbers_bad(a, b):
    result = a + b
    print(result)

add_numbers_bad(5, 10)
def complex_function(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 3
    elif n == 5:
        return 5
    elif n == 6:
        return 8
    elif n == 7:
        return 13
    elif n == 8:
        return 21
    elif n == 9:
        return 34
    elif n == 10:
        return 55
    else:
        return complex_function(n - 1) + complex_function(n - 2)
