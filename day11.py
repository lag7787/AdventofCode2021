#were predicting how the people will sit in the next round.
#we havea gameboard that represetns the current state.
#and well build a second gameboard that will display the waiting area
#after the poeple sit, keep track of changes and wait until we have none.
import os

def get_data():

    try:

        with open("./data/input11.txt",'r') as my_file:

            data = [list(line.rstrip()) for line in my_file.readlines()]

    except OSError as err:
        print(f"OSError: {err}")
        raise

    else:
        my_file.close()

    return data

def find_occupied(data):

    data,adjustments = model(data)

    while adjustments != 0:

        data,adjustments = model(data)

    count = 0
    for row in data:
        for space in row:
            if space == "#":
                count += 1

    return count

def find_occupied2(data):
    data,change = model2(data)

    while change:

        data,change = model2(data)

    count = 0
    for row in data:
        for space in row:
            if space == "#":
                count += 1

    return count

def count_filled(data,i,j):

    nocc = 0
    R = len(data)
    C = len(data[0])

    #iterate around the element in question by offsetting the idicies.

    for di in [-1,0,1]:
        for dj in [-1,0,1]:
            if not (di == 0 and dj == 0):
                ii = i + di
                jj = j + dj
                #after offset, make sure that the new indicies are within the bounds,
                #such that we want have an out of bounds error
                

                if 0<=ii<R and 0<=jj<C and data[ii][jj] == "#":
                    nocc += 1


    return nocc


def model(data):

    adjustments = 0
    new_data = [["?" for i in range(len(data[0]))] for j in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data[i])):

            if data[i][j] == "L":
                if count_filled(data,i,j) == 0:
                    new_data[i][j] = "#"
                    adjustments += 1
                else:
                    new_data[i][j] = data[i][j]

            elif data[i][j] == "#":
                if count_filled(data,i,j) >= 4:
                    new_data[i][j] = "L"
                    adjustments += 1
                else:
                    new_data[i][j] = data[i][j]
            else:
                new_data[i][j] = data[i][j]

    return new_data,adjustments

def count_filled2(data,i,j):

    R = len(data)
    C = len(data[0])
    nocc = 0

    #check each of the directions for a filled seat
    #how do we check? each of the directions has specific way that it travels
    #offset from the current position in a valid direction and check whether or not its
    #a seat. when we find our first seat or we can no longer iterate, end the traversal
    #these are just multipliers in the other directions

    for di in [-1,0,1]:
        for dj in [-1,0,1]:
            #we can think of each of these unique combinations as direction orientations
            if not (di == 0 and dj == 0):

                ii = i + di
                jj = j + dj

                while 0<=ii<R and 0<=jj<C and data[ii][jj] == ".":
                    ii = ii + di
                    jj = jj + dj

                if 0<=ii<R and 0<=jj<C and data[ii][jj] == "#":
                    nocc+=1

    return nocc


def model2(data):
    
    change = False
    new_data = [["?" for i in range(len(data[0]))] for j in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data[i])):

            if data[i][j] == "L":
                if count_filled2(data,i,j) == 0:
                    new_data[i][j] = "#"
                    change = True
                else:
                    new_data[i][j] = data[i][j]

            elif data[i][j] == "#":
                if count_filled2(data,i,j) >= 5:
                    new_data[i][j] = "L"
                    change = True
                else:
                    new_data[i][j] = data[i][j]
            else:
                new_data[i][j] = data[i][j]

    return new_data,change



def pr(board):

    for row in board:
        for elem in row:
            print(elem,end = "")
        print()

def main():

    data = get_data()
    count = find_occupied2(data)
    print(count)

if __name__ == "__main__":
    main()