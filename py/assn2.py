n = int(input("Enter total number of students: "))
marks = []

print("Enter marks = -1 for absent students")
for i in range(n):
    k = int(input("Enter marks of student %d: " %(i+1)))
    marks.append(k)

t = 0
abs = 0

for i in marks:
    if(i == -1):
        abs += 1
    else:
        t += i

avg = t/n
max = marks[0]
min = marks[0]
most = 0


for i in range(len(marks)):
    if(marks[i] > max):
        max = marks[i]

for i in range(1, len(marks)):
    if(marks[i] < min and marks[i] != -1):
        min = marks[i]


def frequent(l):
    c = 0
    most = l[0]

    for i in l:
        f = l.count(i)
        if(f > c):
            c = f
            most = i
    
    return most

print("Average marks: ", avg)
print("Most Frequent marks obtained are: ", frequent(marks))
print("Maximum marks: ", max)
print("Minimum marks: ", min)
print("Number of absentees: ", abs)
