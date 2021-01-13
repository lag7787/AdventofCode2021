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

def is_fillable(data,i,j):

    fillable = False

    if i == 0 and j == 0:

        if data[i][j+1] != "#" and \
            data[i+1][j] != "#" and \
                data[i+1][j+1] != "#":
                fillable = True
        
    elif i == 0 and j == len(data[i]) - 1:

        if data[i][j-1] != "#" and \
            data[i+1][j] != "#" and \
                data[i+1][j-1] != "#":
                fillable = True
        
    elif i == len(data) - 1 and j == 0:

        if data[i-1][j] != "#" and \
            data[i-1][j+1] != "#" and \
                data[i][j+1] != "#":
                fillable = True

    elif i == len(data) - 1 and j == len(data[i]) - 1:

        if data[i-1][j] != "#" and \
            data[i-1][j-1] != "#" and \
                data[i][j-1] != "#":
                fillable = True

    elif i == 0:
        
        if data[i][j-1] != "#" and \
            data[i][j+1] != "#" and \
                data[i+1][j] != "#" and \
                    data[i+1][j+1] != "#" and \
                        data[i+1][j-1] != "#":
                        fillable = True

    elif i == len(data) - 1:

        if data[i][j-1] != "#" and \
            data[i][j+1] != "#" and \
                data[i-1][j] != "#" and \
                    data[i-1][j+1] != "#" and \
                        data[i-1][j-1] != "#":
                        fillable = True

    elif j == 0:

        if data[i-1][j] != "#" and \
            data[i-1][j+1] != "#" and \
                data[i][j+1] != "#" and \
                    data[i+1][j+1] != "#" and \
                        data[i+1][j] != "#":
                        fillable = True

    elif j == len(data[i]) - 1:

        if data[i-1][j] != "#" and \
            data[i-1][j-1] != "#" and \
                data[i][j-1] != "#" and \
                    data[i+1][j-1] != "#" and \
                        data[i+1][j] != "#":
                        fillable = True

    else:
        if data[i-1][j] != "#" and \
            data[i-1][j-1] != "#" and \
                data[i][j-1] != "#" and \
                    data[i+1][j-1] != "#" and \
                        data[i+1][j] != "#" and \
                            data[i+1][j+1] != "#" and \
                                data[i][j+1] != "#" and \
                                    data[i-1][j+1] != "#":
                                    fillable = True

    return fillable

def is_emptyable(data,i,j):

    fill_count = 0
    valid_seats = None

    if i == 0 and j == 0:

        valid_seats = [data[i][j+1],data[i+1][j],data[i+1][j+1]]

    elif i == 0 and j == len(data[i]) - 1:

        valid_seats = [data[i][j-1],data[i+1][j],data[i+1][j-1]]

    elif i == len(data) - 1 and j == 0:

        valid_seats = [data[i-1][j],data[i-1][j+1],data[i][j+1]]

    elif i == len(data) - 1 and j == len(data[i]) - 1:

        valid_seats = [data[i-1][j],data[i-1][j-1],data[i][j-1]]

    elif i == 0:

        valid_seats = [data[i][j-1],data[i][j+1],data[i+1][j],data[i+1][j+1],data[i+1][j-1]]

    elif i == len(data) - 1:

        valid_seats = [data[i][j-1],data[i][j+1],data[i-1][j],data[i-1][j+1],data[i-1][j-1]]

    elif j == 0:

        valid_seats = [data[i-1][j],data[i-1][j+1],data[i][j+1],data[i+1][j+1],data[i+1][j]]

    elif j == len(data[i]) - 1:

        valid_seats = [data[i-1][j],data[i-1][j-1],data[i][j-1],data[i+1][j-1],data[i+1][j]]

    else:
        valid_seats = [data[i-1][j],data[i-1][j-1],data[i][j-1],data[i+1][j-1],data[i+1][j],data[i+1][j+1],data[i][j+1],data[i-1][j+1]]

    for seat in valid_seats:
        if seat == "#":
            fill_count += 1

    return fill_count >= 4
    

def model(data):

    adjustments = 0
    new_data = [[None] * len(data[0]) for index in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data[i])):

            if data[i][j] == "L":
                if is_fillable(data,i,j):
                    new_data[i][j] = "#"
                    adjustments += 1
                else:
                    new_data[i][j] = data[i][j]

            elif data[i][j] == "#":
                if is_emptyable(data,i,j):
                    new_data[i][j] = "L"
                    adjustments += 1
                else:
                    new_data[i][j] = data[i][j]
            else:
                new_data[i][j] = data[i][j]

    return new_data,adjustments

def pr(board):

    for row in board:
        for elem in row:
            print(elem,end = " ")
        print()

def main():

    data = get_data()
    num = find_occupied(data)
    print(num)

if __name__ == "__main__":
    main()