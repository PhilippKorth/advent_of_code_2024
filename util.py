from itertools import groupby

def read_file(file_path):
    """Gets the content from the given file"""
    with open(file_path, 'r') as input_file:
        return input_file.read()


def read_sperated_file(file_path, split_on_seperator=''):
    """
    If the input itself is seperated by something, split int into sets of inputs
    """
    content = read_file(file_path)
    return [list(v) for k, v in groupby(content.splitlines() , key=split_on_seperator.__eq__) if not k]
    
