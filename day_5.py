from functools import cmp_to_key
from util import read_sperated_file


input = "inputs/day5.txt"

def create_compare_function(ruleset):
    """
    Creates a compare function that will take the order given by the 
    rules and uses it in a prefered way to the natural order of the values
    """
    
    def compare_pages(page_a, page_b):
        if page_a == page_b:
            return 0

        elif f"{page_a}|{page_b}" in ruleset:
            return 1

        elif f"{page_b}|{page_a}" in ruleset:
            return -1

        else:
            return 1 if page_a > page_b else -1

    return compare_pages



if __name__ == '__main__':

    rules, updates = read_sperated_file(input)
   
    compare_pages = create_compare_function(rules)

    valid_update_sum = 0
    invalid_update_sum = 0
    for update in [update.split(',') for update in updates]:
        
        correct_update = sorted(update,key=cmp_to_key(compare_pages), reverse=True)
        middle_index = int(len(update)/2)
        if update == correct_update:
            # Since len is always odd
            valid_update_sum += int(update[middle_index])

        else:
            invalid_update_sum += int(correct_update[middle_index])

    print(valid_update_sum)
    print(invalid_update_sum)