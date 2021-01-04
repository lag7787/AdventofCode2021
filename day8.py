from enum import Enum

E = Enum("E","SUCCESS FAILURE")

def open_file():

    try:
        with open("./data/input8.txt",'r') as my_file:

            data = [line.strip() for line in my_file.readlines()]

    except FileNotFoundError:
        print("Error!")

    my_file.close()

    return data

#parse the data into commands and arguments
#well use a list of tuples

def fix(commands):

    for index in range(len(commands)):

        if commands[index][0] == "jmp":
            commands[index][0] = "nop"
            accumulator = accumulate(commands)
            if accumulator[1] == E.SUCCESS:
                return accumulator[0]
            else:
                commands[index][0] = "jmp"

        elif commands[index][0] == "nop":
            commands[index][0] = "jmp"
            accumulator = accumulate(commands)
            if accumulator[1] == E.SUCCESS:
                return accumulator[0]
            else:
                commands[index][0] = "nop"

def parser(data):

    commands = []

    for command in data:

        tmp = command.split()
        tmp[1] = int(tmp[1])
        commands.append(tmp)

    return commands

def accumulate(commands):

    accumulator = 0
    position = 0
    completion = E.FAILURE
    positions = set()
    flag = False

    def execute_command(command):

        instruction = command[0]
        argument = command[1]
        nonlocal position 
        nonlocal accumulator

        if instruction == "acc":

            position += 1
            accumulator += argument

        elif instruction == "jmp":

            position += argument

        else:
            position += 1


    while not flag:

        if position in positions:
            flag = True
            completion = E.FAILURE
        elif position == len(commands):
            flag = True
            completion = E.SUCCESS
        else:
            positions.add(position)
            execute_command(commands[position])

    return [accumulator,completion]

def main():

    data = open_file()
    commands = parser(data)
    accumulator = fix(commands)
    print(accumulator)

if __name__ == "__main__":
    main()