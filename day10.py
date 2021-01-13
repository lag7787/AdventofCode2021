import os

def open_file():

    try:
        with open("./data/input10.txt", "r") as my_file:

            data = [int(line.rstrip()) for line in my_file.readlines()]

    except OSError as err:

        print(f"OSError: {err}")
        raise

    else:
        my_file.close()

    return data

def enumerate_diff(data):

    #essenially we need to create a linked list structure of adapters, seperated by at most a value of 3
    #we need to link all of the adapters, so in the event that an adapter can link more than one in the list, we should connect that one 
    #how should we link them? because there are not repeat value we can make a set, take the difference from the current value of the adapter of 1 2 and 3
    #we should take the one that appears first and repeat the process. It seems like we can do this recursively or iteratively

    data_set = set(data)
    three_jolt = 1
    one_jolt = 0
    adapter_val = 0


    for index in range(len(data_set)):



        if adapter_val + 1 in data_set:

            adapter_val += 1
            one_jolt += 1
            data_set.remove(adapter_val)

        elif adapter_val + 2 in data_set:

            adapter_val += 2
            data_set.remove(adapter_val)
    
        elif adapter_val + 3 in data_set:

            adapter_val += 3
            three_jolt += 1
            data_set.remove(adapter_val)


    return one_jolt,three_jolt


unique_dict = dict()

def enumerate_unique(data,adapter_val=0):

    """
    @parameters: the data representing the adapters and a reference number.
    This function will enumerate all unique combinations by recuring through all possibilities. 
    """

    #we can still optimize this by removing repeated operations

    count = 0
    child_nodes = []
    data_set = set(data)

    if adapter_val in unique_dict:

        return unique_dict[adapter_val]

    print(adapter_val)

    if adapter_val + 1 in data_set:

        child_nodes.append(adapter_val + 1)

    if adapter_val + 2 in data_set:

        child_nodes.append(adapter_val + 2)

    if adapter_val + 3 in data_set:

        child_nodes.append(adapter_val + 3)


    if len(child_nodes) == 0:

        unique_dict[adapter_val] = 1
        return 1

    else:
        for child in child_nodes:

            count += enumerate_unique(data,child)

        unique_dict[adapter_val] = count
        return count


def main():

    data = open_file()
    one_jolt,three_jolt = enumerate_diff(data)
    print(enumerate_unique(data))


if __name__ == "__main__":
    main()