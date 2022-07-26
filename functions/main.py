# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
# 1
def greet(name):
    return(f'Hello, {name}!')
greet('Bob')

# 2
def add(a, b, c):
    sum = (a + b + c)
    return sum
add(5, 3, 2)

# 3
def positive(x):
    if x > 0:
        return True
    else :
        return False
positive(5)

# 4
def negative(y):
    if y >= 0:
        return False
    else :
        return True
negative(0)