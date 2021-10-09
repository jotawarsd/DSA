#Quick Sort
def partition(A, lb, ub):
    pivot = lb
    i = lb + 1
    j = ub
    while i <= j:

        while i <= ub and A[pivot] >= A[i]:

            i = i + 1

        while A[pivot] < A[j]:

            j = j - 1

        if i < j:

            temp = A[i]

            A[i] = A[j]

            A[j] = temp

    temp = A[pivot]

    A[pivot] = A[j]

    A[j] = temp

    return j


def Quick_Sort(A, lb, ub):

    if lb < ub:

        mid = partition(A, lb, ub)

        Quick_Sort(A, lb, mid - 1)

        Quick_Sort(A, mid + 1, ub)


def Accept_Per(A):

    n = int(input("Enter the total Strength of class :"))

    for i in range(n):

        x = float(input("Enter the percentage of %d student :" % (i + 1)))

        A.append(x)


def Display_Per(A):

    print("Percentage of students are:")

    for i in range(len(A)):

        print("%.2f" % A[i])

def top_5(L):
    print("Top 5 students are:- \n")
    if (len(L) > 5):
        for i in range(len(L)-1, len(L) - 6, -1):
            print(L[i])
    else:
        for i in range(len(L)-1, 0, -1):
            print(L[i])





def main():

    A = []

    while True:

        print("\nPress 1 to accept and display")
        print("\nPress 2 Quick sort")
        print("\nPress 3 to end")

        ch = int(input("\nEnter your choice: "))

        if ch == 3:

            print("End of program")

            quit()

        elif ch == 1:

            Accept_Per(A)

            Display_Per(A)

        elif ch == 2:
            n = len(A)
            Quick_Sort(A, 0, n - 1)
            Display_Per(A)

            x = input("Do you want to display top 5 scores? (y/n): ")
            if(x == 'y' or x == 'Y' or x == 'yes' or x == 'Yes'):
                top_5(A)
            

main()