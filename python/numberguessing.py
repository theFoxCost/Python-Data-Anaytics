import random

# make a function to generate a renadom  numb BOTnum
# make a function to input the num  numb USERnum
# make a functions to substracte the two number if USERnum - BOTnum < 5 (really close) 



# make a fucniton to let the user knwo th e bot num nd if it close or really close or far or really far

BOTnum = int(random.randrange(1, 100)) # double check
USERnum = int(input("Enter Your Number (1 to 100): "))

if USERnum > 100 and USERnum < 0 :
    print('are you stupid (read the question)')


def subtract():
    result = BOTnum - USERnum    
    return result

def compare():
    result = subtract()
    if result < 5:
        print("TOOOOOOOOOOOOOOOOOOOOO CLOSE")
        print(BOTnum)
    elif result > 5:
        print("FAR")
        print(BOTnum)
    elif result < 10:
        print("CLOSE")
        print(BOTnum)
    elif result > 10:
        print("TOOOOOOOOOOOOOOOOOOOOO FAR")
        print(BOTnum)
    elif result == 0:
        print("exactly it is")
        print("my number is: ", BOTnum)


compare()
