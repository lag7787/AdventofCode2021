import re

#parse through file data and make sure it has all 4 required fields
#i could make a regex for each block of text. tokens can be entries? 
#preferably i want lists of lists? 
#can split the data again so i have lists of lists corresponding to each data field


def get_data(file_name):

    with open("./data/" + file_name, 'r') as data:

        my_lst = data.read().split('\n\n')
        my_lst = [sorted(elem.split()) for elem in my_lst]
        my_lst = [" ".join(elem) for elem in my_lst]

    return my_lst

def count_passports(data):

    count = 0

    for entry in data:

        if isValid(entry):
            count += 1

    return count

def isValid(entry):


    is_valid = True

    pattern_obj = re.compile(r"""

    byr:(?P<b_year>19[2-9][0-9]|200[0-2])\s #matches birth year
    (?:cid:.+\s)? #matches country code
    ecl:(?P<eye_color>amb|blu|brn|gry|grn|hzl|oth)\s #matches eye color
    eyr:(?P<exp_year>202[0-9]|2030)\s #matches expiration year
    hcl:(?P<hair_color>\#[0-9a-f]{6})\s #matches hair color
    hgt:(?P<height>1(?:[5-8][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in)\s #matches height
    iyr:(?P<issue_year>201[0-9]|2020)\s #matches issue year
    pid:(?P<PID>\d{9}) #matches pid
    
    """,re.VERBOSE)

    match_obj = pattern_obj.search(entry)

    if not match_obj:
        is_valid = False

    else:
        print(match_obj.group(0))


    return is_valid




    #manual verification of all other fields




def main():

    data = get_data("input4.txt")
    print(count_passports(data))


if __name__ == "__main__":
    main()