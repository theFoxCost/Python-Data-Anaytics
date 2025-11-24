import os
# make a fucntion to verfy if the file exist
def veriy():
    isExist = os.path.exists("tasks.txt")
    return isExist

veriy()

# make a function that input the thing
task = input('Enter Your Task: \n')
task = task + "\n"


# make function that make changes
def change():
    with open("task.txt", 'a') as f:
        f.write(task)


change()

