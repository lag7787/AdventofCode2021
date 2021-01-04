from queue import Queue

def open_file():

    try:
        with open("./data/input9.txt", "r") as my_file:
            data = [int(line.rstrip()) for line in my_file.readlines()]

    except OSError as err:

        print(f"OSError: {err}")
        raise

    else:
        my_file.close()

    return data

def is_valid(s,num):

    #is valid if two numbers in the set sum to it 

    valid = False
    for val in s:

        diff = num - val
        if diff in s and diff != val:
            valid = True
            break


    return valid

def find_encryption(weakness,data):

    lower_index = 0
    upper_index = 0
    sm = data[lower_index]

    while sm != weakness:

        if sm < weakness:
            upper_index += 1
            sm += data[upper_index]
        elif sm > weakness:
            sm -= data[lower_index]
            lower_index += 1

    contig = [data[i] for i in range(lower_index,upper_index+1)]
    return max(contig) + min(contig)


def find_weakness(data):

    #we may not use the same item twice in a calculation,but
    #there may be duplicates in the dataset,which makes the inappropriate
    
    
    q = Queue([data[i] for i in range(25)])
    s = {data[i]:1 for i in range(25)}


    for index in range(25,len(data)):

        num = data[index]
        if is_valid(s,num):
            val = q.dequeue()
            q.enqueue(num)

            #remove item from dict
            if s[val] == 1:
                del s[val]
            else:
                s[val] -= 1

            #add item to the dict
            if num in s:
                s[num] += 1
            else:
                s[num] = 1

        else:
            print(num)
            return num


def main():

    data = open_file()
    target = find_weakness(data)
    print(find_encryption(target,data))

        


if __name__ == "__main__":
    main()