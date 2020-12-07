
def report_repair():

    try:
        in_file = open("./data/input.txt", 'r')
    except FileNotFoundError:
        print("Incorrect file name!")


    data = [int(line.strip('\n')) for line in in_file]
    vals_dict = {}

    for val in data:
        #we need to index the vals_dict with the value were looking for
        if val in vals_dict:
            return val * vals_dict[val]
        else:
            diff = 2020 - val
            vals_dict[diff] = val

def report_repair2():

    try:
        in_file = open("./data/input.txt", 'r')
    except FileNotFoundError:
        print("Incorrect file name!")

    data = [int(line.strip('\n')) for line in in_file]
    
    length = len(data)
    data.sort()

    #three sum two pointer method
    
    for i in range(0,length-2):

        if i > 0 and data[i] == data[i - 1]:
            pass
            continue

        j,k = i+1, length - 1

        while j < k:

            three_sum = data[i] + data[j] + data[k]

            if three_sum == 2020:
                print(data[i], data[j], data[k])
                return (data[i] * data[j] * data[k])

            else:

                if three_sum < 2020:
                    j += 1
                else:
                    k -= 1

def main():
    print(report_repair())
    print(report_repair2())

if __name__ == "__main__":
    main()
