print("solid square")
num = int(input("Enter the size of the pattern: "))
while num <= 0:
 for i in range(num ):
    for j in range(num):
        print("*", end="")
    print()