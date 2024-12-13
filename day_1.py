from collections import Counter
from util import read_file


input = read_file("inputs/day1.txt")

def get_lists(input):
    """ Gets left and right list from the input"""
    left_values, right_values = [], []
    for line in input.split("\n"):
        left, right = line.split("   ")
        left_values.append(left)
        right_values.append(right)
    
    return left_values, right_values

def calculate_distance(left_list, right_list):
    """ Gets the distance of the given lists"""
    distance = 0
    for left, right in zip(sorted(left_list), sorted(right_list)):
        distance += abs(int(left) - int(right))

    return distance


def calculate_similarity(left_list, right_list):
    """ Gets the similarity of both lists"""
    similarity = 0
    counted_list = Counter(right_list)
    
    for left_element in left_list:
        similarity += int(left_element) * counted_list[left_element]
    
    return similarity

if __name__ == '__main__':
    left_list, right_list = get_lists(input)

    print(f"Distance: {calculate_distance(left_list, right_list)}")
    print(f"Similarity: {calculate_similarity(left_list, right_list)}")
