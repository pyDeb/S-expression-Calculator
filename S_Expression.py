from sys import argv


def parse(string_input):
   
    while '(' in string_input:
        #finds the first close parantheses's position
        closed_parentheses = string_input.index(')')
        #finds the open parantheses
        open_parentheses = string_input[:closed_parentheses].rindex('(')

        #calculates the expression between parantheses
        result = calculate(string_input[open_parentheses + 1: closed_parentheses])

        #replaces the parantheses with the result
        string_input = string_input[:open_parentheses] + result + string_input[closed_parentheses + 1:]
    
    return string_input

def calculate(string_input):
    first_operand = ""
    second_operand = ""
    is_add = False
    if string_input[0:3] == "add":
        i = 4
        is_add = True
    else:
        i = 9
        
        
    while string_input[i] != " ":
        first_operand += string_input[i]
        i = i + 1

 
    i = i + 1   
    while i < len(string_input):
        second_operand += string_input[i]
        i = i + 1

    if is_add:
        return str(int(first_operand) + int(second_operand))
    else:
        return str(int(first_operand) * int(second_operand))



def main():
    print(parse(argv[1]))


if __name__ == '__main__':
    main()