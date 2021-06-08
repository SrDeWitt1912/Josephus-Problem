user = int(input("Set the number of persons in the circle: "))

def JosephusProblem(number):
    binary_int = int(bin(number)[2:])
    binary_string = str(binary_int)

    list = []
    list[:0] = binary_string
    
    answer_list = list.copy()
    first_element = answer_list[0]
    answer_list.pop(0)
    answer_list.append(first_element)

    strings_base = "".join(answer_list)
    
    decimal_answer = int(strings_base, 2)
    print ("The winner is: ", decimal_answer)
    print("The binary number of the people in the circle is: ", binary_int)
    print("The binary number of the winner position is: ", strings_base)

JosephusProblem(user)