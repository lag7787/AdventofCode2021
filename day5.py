def row_decoder(enc_str):

    final_str =""
    
    for char in enc_str:

        F = ord('F')
        char = ord(char)
        char = char ^ F
        char = char >> 2
        final_str += str(char)

    return int(final_str,2)

def col_decoder(enc_str):

    final_str = ""
    #R corresponds to 1, L corresponds to 0

    for char in enc_str:
        L = ord('L')
        char = ord(char)
        char = char ^ L
        char = char >> 4
        final_str += str(char)

    return int(final_str,2)


def id_decoder(enc_str):

    row_enc = enc_str[:7]
    col_enc = enc_str[7:]

    return (row_decoder(row_enc) * 8 + col_decoder(col_enc))


def get_data():

    with open("./data/input5.txt", 'r') as my_file:

        data = [line.strip('\n') for line in my_file.readlines()]

    return data


def main():

    id_lst = []
    data = get_data()

    for encoding in data:
        id_lst.append(id_decoder(encoding))

    #sort the list and keep track of the previous. if the differece is ever greater than 1, we know that we've found our spot, which will be in between the two numbres
    # differnce shold be equal to 2

    id_lst.sort()

    prev = id_lst[0]

    for index in range(1,len(id_lst)):

        cur = id_lst[index]

        if cur - prev > 1:
            print((prev + cur) / 2)
            break

        prev = cur

        







if __name__ == "__main__":

    main()


    


