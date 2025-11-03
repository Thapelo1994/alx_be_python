number = ""
def Table(number):
    number = int(input("Enter a number:"))
    for i in range(1, 11):
        print(f"{number} x {i} = {number*i}")
Table(number)