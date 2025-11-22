# calc



print('1. Addition \n2.Subtraction \n3.Multiplication \n4.Division')

choice = input('Enter Your Choice : ')
x = int(input("Enter X : "))
y = int(input("Enter Y : "))


if choice == "1" :
    print(x + y)
elif choice == "2":
    print(x - y)
elif choice == "3":
    print(x * y)
elif choice == "4":
    print(x / y)
else:
    print("fuck u")