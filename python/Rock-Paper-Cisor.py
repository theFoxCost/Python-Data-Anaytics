import random

#make function that make random random  

listOfEmoji = ("📃​", "✂️​", "​🗿​​")
print(listOfEmoji)
choice = int(input('Enter Your Choice: '))


def PCRandomEmoji() :
    number = int(random.randrange(1,4))
    imo = listOfEmoji[number]
    return print(imo)

def MyEmoji():
    print("1. 📃 \n 2.✂️​ \n 3.​🗿​​ ")
    if choice == 1:
        imo = "📃"
        print(imo)
    elif choice == 2:
        imo = "✂️"
        print(imo)
    elif choice == 3:
        imo = "🗿"
        print(imo)
    else:
        print("fuck you")
    
MyEmoji()