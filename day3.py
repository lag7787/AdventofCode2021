from typing import List

#traversing a mountain of slops
#accpeted slopes or traversals are ratios between whole numbers.
#travel 3 right and down one 
#givent that the ratio of the rectangel isnt't 3:1 (width:lenght), were going
#to need a way to extend or repeat the battern of the list, not reusing rows that 
#we've traversed down from, but reusing the pattern itself. i think a simple solution is
#essentially the tobbagen loops on itself. each string element is a 
#indiator of depth  

#structure:
    # while were not at the end: -> for loop
    #   check if there was a collision -> function
    #   traverse, using our heuristic -> function
    #   if there was, add one to the collisions 
    #   if not, do nothing
    #   how are we checking if were at the end? who should handle it


#criteria for the end:
    # were at the end when we've exceeded the bottom most row, meaning after we compute
    # traverse on the lsit row, so we simply need to iterate over each row,
    # no need to check an end condition.

#how are we keeping track of position.
#  1) my inital idea is to hold a refernce to
#  the index of the col where we just landed^
#  because we always have a refernce to the row 
#   2) sol 1 isn't very python because it utilizes indexing
#   #we need to instant lookups to check for collisions

def open_file():
    try:
        my_file = open("./data/input3.txt", 'r')
    except FileNotFoundError:
        print("Sorry, invalid path name.") 

    gameboard = [line.strip('\n') for line in my_file.readlines()]

    return gameboard

def tobaggen_trip(displacements: List[tuple]):

    gameboard = open_file()
    collision_lst = []
    product = 1

    #could comput them in parallel because we know the numper of displacements
    for displacement in displacements:

        right = displacement[0]
        down = displacement[1]
        pos = 0
        collisions = 0

        for row_index in range(0,len(gameboard),down):

            row = gameboard[row_index]
            collisions = (collisions + 1) if collision(row,pos) else collisions
            pos = traverse(row,pos,right)

        collision_lst.append(collisions)

    for elem in collision_lst:
        product *= elem
    
    return product

def collision(row,pos):

    return row[pos] == '#'

#parameterize the traverse function so that it will work for different inputs.
def traverse(row,pos,right):
    #there are two cases for the traversal:
    #   1) we overextend the number of columns or 
    #   2) we don't overextend the number of columns

    cols = len(row)

    if pos + right >= cols:
        #we've overextend the columns:
        #we need to calculate the column position after repetiton
        #simply subtrack the number of columns to find the correct position
        pos = pos + right - cols

    else:
        pos = pos + right

    return pos

def main():
    collisions = [(3,1),(1,1),(5,1),(7,1),(1,2)]
    print(tobaggen_trip(collisions))

if __name__ == "__main__":
    main()