def factorial_itrative(n):
    '''
    :param n: Integer
    :return: n * n-1 * n-2 * n-3...... till it reaches 1
    '''
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac

def factorial_recursive(n):
    '''
    :param n: Integer
    :return: n * n-1 * n-2 * n-3...... till it reaches 1
    '''
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

number = int(input('Enter a number\n'))
print(factorial_itrative(number))
print(factorial_recursive(number))
# n! = n * n-1 * n-2 * n-3...... till it reaches 1
# n! = n * (n-1)!
#! is the sign of factorial