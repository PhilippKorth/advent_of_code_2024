import re
from util import read_file

input = "inputs/day3.txt"
mul_regex = r"mul\(([1-9][0-9]*),([1-9][0-9]*)\)"
modified_mul_regex = r"mul\(([1-9][0-9]*),([1-9][0-9]*)\)|(don't\(\))|(do\(\))"

def calculate_mul_results(programm):
    """ Calculate mul results"""
    # Remove all code between dont and do as it does not matter

    sum = 0
    enabled = True
    for fakt1, fakt2, off, on in re.findall(pattern=modified_mul_regex, string=programm, flags=re.MULTILINE):
    
        if off:
            enabled = False

        elif on:
            enabled = True
        else:
            sum += int(fakt1) * int(fakt2) * (1 if enabled else 0)
    return sum

if __name__ == '__main__':

    programm = read_file(input)
    print(f"Multiplication Sum:{calculate_mul_results(programm)}")
