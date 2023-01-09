
def new(num1, num2):
    num1, x = num1

    if x == '+':
        return int(num1 + num2)
    if x == '-':
        return int(num2 - num1)
    if x == '/':
        return int(num2 / num1)
    if x == '*':
        return int(num1 * num2)

def zero(num=-1): #your code here
    if num == -1:
        return 0
    return new(num, 0)

def one(num=-1): #your code here
    if num == -1:
        return 1
    return new(num, 1)

def two(num=-1): #your code here
    if num == -1:
        return 2
    return new(num, 2)

def three(num=-1): #your code here
    if num == -1:
        return 3
    return new(num, 3)

def four(num=-1): #your code here
    if num == -1:
        return 4
    return new(num, 4)

def five(num=-1): #your code here
    if num == -1:
        return 5
    return new(num, 5)

def six(num=-1): #your code here
    if num == -1:
        return 6
    return new(num, 6)

def seven(num=-1): #your code here
    if num == -1:
        return 7
    return new(num, 7)

def eight(num=-1): #your code here
    if num == -1:
        return 8
    return new(num, 8)

def nine(num=-1): #your code here
    if num == -1:
        return 9
    return new(num, 9)

def plus(num): #your code here
    return (num, '+')
def minus(num): #your code here
    return (num, '-')
def times(num): #your code here
    return (num, '*')
def divided_by(num): #your code here
    return (num, '/')

one(plus(five()))