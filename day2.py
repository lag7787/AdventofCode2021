from LookAHeadChain import lookaheadchain

def passwordDetector():

    try:
        my_file = open("./data/input2.txt",'r')

    except FileNotFoundError:
        print("Invalid path name")

    file_lst = [i.strip("\n") for i in my_file]

    #algorithm:
    #for each line of text, create an iterator from the iterable and use
    #it to tokenenize the strig, using helper functions to pull out certain values

    count = 0

    for line in file_lst:
        #print(line)
        tmp_iter = lookaheadchain(line)
        minVal = takeNum(tmp_iter)
        next(tmp_iter)
        maxVal = takeNum(tmp_iter)
        next(tmp_iter)
        char = next(tmp_iter)
        next(tmp_iter)
        next(tmp_iter)
        password = takePassword(tmp_iter)
      #  print(f"minValue: {minVal}\n"+
      #        f"maxValue: {maxVal}\n"+
      #        f"Char: {char}\n"+
      #        f"Password: {password}")

        if isValid1(int(maxVal),int(minVal),char,password):
            count += 1

    return count


def isValid1(maxVal, minVal, char, string):

    occurances = string.count(char)

    return occurances <= maxVal and occurances >= minVal


def takeNum(line_iter):

    num_str = ""

    while line_iter.peek().isnumeric():
        num_str += next(line_iter)

    return num_str


def takePassword(line_iter):

    password = ""
    while line_iter.peek() and line_iter.peek().isalpha():
        password += next(line_iter)

    return password


def main():

    print(passwordDetector())


if __name__ == "__main__":

    main()
    