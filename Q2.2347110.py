l = []
n = int(input("Enter length of list "))
for i in range(0, n):
    x = int(input())
    l.append(x)
print(l)
# Finding if list is divisible by 3
flag = 1
for i in l:
    if i % 3 != 0:
        flag = 0
if flag == 0:
    print("List is not divisible by 3")
else:
    print("List is divisible by 3")
s = 0
# Square of all event numbers are
print("Square of all even numbers are ")
for i in l:
    if i % 2 == 0:
        print(i*i)
        x = i
        # sum of digits of even numbers
        while (x > 0):
            s = s+(x % 10)
            x = x/10
print("Sum of all digits of even numbers are ", s)
# Removing duplicates from the list
l1 = []
c = 0
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        c += 1
if c == 0:
    print("There are no duplicates in this list ")
else:
    print("New list is ", l1)


# Finding birthdate from list
dict = {"Avik Mallick": "14 November 2002",
        "Pronoy Chakroboty": "14 july 2002", "Rishab Sinha": "6 March 2002"}


def birthDate(b):

    for i in dict:
        if b == i:
            print(dict[i])


birthDate("Pronoy Chakroboty")
