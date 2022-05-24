#For question 1

def function1(n):
    if n == 1:
        return 1
    return n + function1(n-1)




#For question 2

def function2(n):
    if n < 1:
        return 1
    return  n * function2(n-1)





#For question 3

def function3(n):
    if n < 1:
        return 0
    return n + function3(n-2)



#For question 4

def function4(n):
    if n < 1:
        return 0
    return pow(n,2) + function3(pow(n-1,2))



#For question 5

def function5(n):
   if n <= 1:
       return n
   else:
       return(function5(n-1) + function5(n-2))


#For question 6
def function6(n):
    if n < 1:
        return 0
    print(n)
    return function5(n-1)


#For question 7
def function7(n):
    if n < 1:
        return 0
    function6(n-1)
    print(n)



#For question 8
def function8(n):
    if n < 1:
        return 0
    azeret = n
    for i in range(1, n):
        azeret *= i
    print(azeret)
    return function8(n-1)



#For question 9
def function9(n, first = 0, second = 1):
    print(first)
    if n == 0:
        return first
    return function9(n - 1, second, first + second)
function9(7)


#For question 10
def function10(n):
    if n < 1 :
        return 0

    c = n
    for j in range(1,n+1):
        c = j + n
    print(c)
