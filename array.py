A = []
d = int(input("enter number of elements: "))
sum = 0

for i in range(d):
    a = int(input("number: "))
    sum += a
    A.append(sum)

print(A)