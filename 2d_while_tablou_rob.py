# while robot

num_col= int(input("Enter number of columns: "))
num_lin= int(input("Enter number of lines: "))
robotx = int(input("Enter robot ax X: "))
roboty = int(input("Enter robot ax Y: "))

l = 1
while l <= num_lin:
    c = 1
    while c <= num_col:
        if c == robotx and l == roboty:
            print("R", end =" ")
        else:
            print("*", end =" ")
        c += 1
    print()
    l += 1

