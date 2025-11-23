print("Welcome to my Roman Numeral converter!")
print("To begin, please enter the numeral you wish to convert")

numeral_input = input("Roman Numeral: ")

def roman_to_int(numeral):
    final_answer = 0
    for i in numeral:
        if i == "M":
            final_answer += 1000
        elif i == "D":
            final_answer += 500
        elif i == "C":
            final_answer += 100
        elif i == "L":
            final_answer += 50
        elif i == "X":
            final_answer += 10
        elif i == "V":
            final_answer += 5
        elif i == "I":
            final_answer += 1
        else:
            print("Error: Invalid Roman Numeral")
            return None
        print("The roman numeral you entered translates to: " + str(final_answer) + "!")
