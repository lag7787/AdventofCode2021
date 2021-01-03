def open_file():

    with open("./data/input7.txt",'r') as my_file:

        data = [line.split("contain") for line in my_file.readlines()]
        data_dict = {}
        
        for element in data:
            element[0] = element[0].strip().rstrip("s")
            element[1] = [elem.strip().rstrip(".").rstrip("s") for elem in element[1].split(",")]
          #  for index in range(len(element[1])):
          #      element[1][index] = "".join(filter(lambda x: not x.isdigit(), element[1][index])).strip()

        for element in data:
            data_dict[element[0]] = element[1]

    return data_dict



def count_bags(data):

    unique_bags = set()

    def search_bag(bag):

        for parent in data:
            contents = data[parent]
            if bag in contents: #guarentees that well find all bags that contian the bag in question
                search_bag(parent)
                unique_bags.add(parent)

        return

    search_bag("shiny gold bag")
    return len(unique_bags)

def count_contained(data):

    lst = []

    def search_bag(bag,multiplier):

        if bag in data:

            for child in data[bag]:

                occurances = 1

                if child[0].isdigit():
                    occurances = int(child[0])
                    child = "".join(filter(lambda x: not x.isdigit(), child)).strip()

                lst.append(multiplier * occurances)
                search_bag(child,multiplier * occurances)

        return

    search_bag("shiny gold bag", 1)
    return sum(lst)

def main():

    data = open_file()
    print(count_contained(data))

if __name__ == "__main__":
    main()

    


