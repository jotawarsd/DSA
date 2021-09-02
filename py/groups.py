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

def intersection2(A, B, sA, sB):
    R = []
    for i in range(len(A)):
        x = A[i]
        if (x in B):
            R.append(x)
        else:
            pass
    Display(R, ("%s and %s"%(sA,sB)) )

intersection2(C, B, "Cricket", "Badminton")
intersection2(B, F, "Badminton", "Football")
intersection2(F, C, "Football", "Cricket")

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

intersection(C, B, F)


