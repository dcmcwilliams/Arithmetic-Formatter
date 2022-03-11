arithmetic_formatter.py


def arithmetic_arranger(problems, solve=True):
    # check problem list
    first = ''
    second = ''
    sumx = ''
    lines = ''
    # maximal problems is 5
    if len(problems) >= 6:
        return 'Error: Too many problems.'
    # split problem to separate components
    for i in problems:
        a = i.split()
        firsts = a[0]
        seconds = a[2]
        operands = a[1]
        # check the length of the number, max 4 digits
        if (len(firsts) > 4 or len(seconds) > 4):
            return "Error: Numbers cannot be more than four digits."

        # check the input as valid digits
        if not firsts.isnumeric() or not seconds.isnumeric():
            return "Error: Numbers must only contain digits."

        if (operands == '+' or operands == '-'):
            if operands == "+":
                sums = str(int(firsts) + int(seconds))
            else:
                sums = str(int(firsts) - int(seconds))
            # set length of sum and top, bottom and line values
            length = max(len(firsts), len(seconds)) + 2
            top = str(firsts).rjust(length)
            bottom = operands + str(seconds).rjust(length - 1)
            line = ''
            res = str(sums).rjust(length)
            for s in range(length):
                line += '-'
            # add to the overall string
            if i != problems[-1]:
              first += top + '    '
              second += bottom + '    '
              lines += line + '    '
              sumx += res + '    '
            else:
              first += top
              second += bottom
              lines += line
              sumx += res
        else:
            return "Error: Operator must be '+' or '-'."
    # strip out spaces to the right of the string
    if solve:
        arranged_problems = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        arranged_problems = first + '\n' + second + '\n' + lines
    return arranged_problems



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']))
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['3 + 855', '988 + 40']))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']))
