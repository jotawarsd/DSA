def Accept(S, Str):
    n = int(input("Enter number of students playing %s: " %Str))
    for i in range(n):
        x = int(input("Enter roll number of student %d who plays %s: " %((i+1), Str)))
        S.append(x)
    print ("Added successfully!")

def Display(S, *Str):
    n = len(S)
    if(n == 0):
        print("No students like %s" %Str)
    else:
        print("Students playing %s are: " %Str)
        print(S)  

def intersection(A, B, C):
    T = []
    for i in range(len(A)):
        x = A[i]
        if (x in B):
            if (x in C):
                T.append(x)
            else:
                pass
    print("Students playing all three sports are:", T) 

def intersection2(A, B):
    R = []
    for i in range(len(A)):
        x = A[i]
        if (x in B):
            R.append(x)
        else:
            pass
    return R

def diff(A, B):
    D = []
    for i in range(len(A)):
        x = A[i]
        if(x not in B):
            D.append(x)
        else:
            continue
    return D

def union(A, B):
    for i in range(len(A)):
        x = A[i]
        if(x in B):
            B.append(x)
    return B
        

C = []
B = []
F = []

I = []

Accept(C, "Cricket")
Accept(B, "Badminton")
Accept(F, "Football")

Display(C, "Cricket")
Display(B, "Badminton")
Display(F, "Football")

print("Students that play both Cricket and Badminton are: %s" %())
print("Students that play either Cricket or badminton but not both are: %s" %())
print("Number of students that play neither cricket nor Badminton are: %s" %())
print("Number of students that play Cricket and Football but not Badminton are: %s" %())
