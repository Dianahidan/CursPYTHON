# EX 1
def my_sum(*args):
    result = 0
    for i in args:
        itype = type(i)
        if itype == int or itype(i) == float:
            result = result + i
        else:
            continue
    print(result)

my_sum(1, 5, -3, 'abc', [12, 56, 'cad'])


# EX 2
def recursive_sum(n):
    if n == 0:
        return n    
    return n + recursive_sum(n-1)   
print(recursive_sum(3))

# asa am gandit eu, dar nu merge :(
def n_sum(n):
    n1 = 0
    n2 = 0
    if n == 0:
        return n
    elif n % 2 == 0:
        n1 = n + n_sum(n-1)
    else:
        n2 = n + n_sum(n-1)
        
print(n_sum(7))


# EX 3
def function():
    numar = input("Type the number:")
    try:
        numar = int(numar)
        print(numar)
    except:
        print(0)
    
function()

