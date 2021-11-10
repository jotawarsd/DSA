info_dict = {}
fib = []

def accept(name, phno):
    name = input("Enter student's name: ")
    phno = input("Enter student's phone number: \n")
    info_dict.update({name : phno})

def display(d):
    k = list(d.keys())
    v = list(d.values())
    for i in range(len(k)):
        print(k[i], ": ", v[i])

def bin_r(min, max, lst, x):
    if (max >= min):
        mid = max + min // 2

        if(x == lst[mid]):
            return x
        
        elif(x > lst[mid]):
            bin_r(mid+1, max, lst, x)

        else:
            bin_r(min, mid-1, lst, x)
    
    else:
        return -1

def bin_i(lst, x):
    min, mid = 0
    max = len(lst) - 1
    while(min <= max):
        mid = min + max // 2
        if (x < lst[mid]):
            max = mid - 1        
        elif (x > lst[mid]):
            min = mid + 1
        else:
            return x
    
    return -1

def fibo(lst, x):
    n = len(lst) - 1
    fm2 = 0
    fm1 = 1
    f = 0
    
    while(f < n):
        fm2 = fm1
        fm1 = f
        f = fm2 + fm1

    k = -1

    while(f > 1):

        i = min(k + f, n-1)

        if(x > lst[i]):
            f = fm1
            fm1 = fm2
            fm2 = f - fm1
            k = i
        elif(x < lst[i]):
            f = fm1

