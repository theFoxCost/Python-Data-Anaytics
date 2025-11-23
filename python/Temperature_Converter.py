

print("1. C --> F\n 2.F --> C"  )
choice = input("choose your option: ")
if choice == "1":
    c = int(input('C: '))
    f = (9/5)*c +32
    print(f)
elif choice == "2":
    f = int(input('F: '))
    c = (f - 32) / 18
    print(c)
else:
    print("option unavailable")


