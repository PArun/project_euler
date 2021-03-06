'''
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
'''

MAX_INT = 4000000

def compute_fibonocci(number=MAX_INT):
    a = 1
    b = 2
    fibs = [a, b]
    while b < MAX_INT:
        sum = a + b
        a = b
        b = sum
        fibs.append(sum)
    return fibs

if __name__ == '__main__':
    print reduce(lambda x,y: x+y, filter(lambda x: x%2 == 0, compute_fibonocci()))
