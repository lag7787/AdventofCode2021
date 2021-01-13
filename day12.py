import os
from ship import Ship

def get_data():

    try:
        with open("./data/input12.txt","r") as my_file:
            data = [[line[0],int(line[1:])] for line in my_file.readlines()]

    except OSError as err:
        print(f"OSError: {err}")
        raise 

    else:
        my_file.close()

    return data

def compute_man(data):

    glob = ["E","N","S","W"]
    loc = ["L","R"]

    ship = Ship()
    for dire in data:

        if dire[0] in glob:
            ship.alter_global(dire[0],dire[1])

        elif dire[0] in loc:
            ship.alter_orientation(dire[0],dire[1])

        elif dire[0] == "F":
            ship.forward(dire[1])

    print(ship.compute_man())


def main():

    data = get_data()
    compute_man(data)

if __name__ == "__main__":
    main()