#seperate the data into groups and count the number of unique charcters in each group
#store the data in a set 


def get_data():

    with open("./data/input6.txt",'r') as my_file:

        data = [group.split("\n") for group in my_file.read().split("\n\n")]

    return data

def sum_groups(groups):

    char_sum = 0

    for group in groups:
        char_sum += count(group)

    return char_sum


def count(group):


    #count the number of characters for which each member in the group has answered yes.
    #each member in the group has to have that character for it to be counted
    #we create a set, and each element in that set has to be found on the next member. if its not, remove it from the list.
    #we would have to check the elements in the set with elements in the current member, which would be O(n) time 
    #can only be added once for each member

    chars_dict = {}
    count = 0

    for member in group:
        uniques = set()
        for char in member:

            if char not in uniques:

                if char not in chars_dict:
                    chars_dict[char] = 1
                else:
                    chars_dict[char] += 1

                uniques.add(char)


    for char in chars_dict:
        if chars_dict[char] == len(group):
            count += 1
    
    print(group,chars_dict)

    return count
    
def main():

    data = get_data()
    print(sum_groups(data))

if __name__ == "__main__":
    main()