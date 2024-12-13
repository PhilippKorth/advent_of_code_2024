
def read_file(file_path):
    """Gets the content from the given file"""
    with open(file_path, 'r') as input_file:
        return input_file.read()