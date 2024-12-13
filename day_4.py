from util import read_file

input = "inputs/day4_test.txt"

def count_xmas(matrix, cell):
    """ Checks each direction of the given cell and counts valid XMAS words"""
    row, coloumn = cell
    words = []
    # N
    words.append(matrix[row][coloumn] + matrix[row-1][coloumn] + matrix[row-2][coloumn] + matrix[row-3][coloumn])

    # NE
    words.append(matrix[row][coloumn] + matrix[row-1][coloumn+1] + matrix[row-2][coloumn+2] + matrix[row-3][coloumn+3])

    # E
    words.append(matrix[row][coloumn] + matrix[row][coloumn + 1] + matrix[row][coloumn + 2] + matrix[row][coloumn + 3])
    
    # SE
    words.append(matrix[row][coloumn] + matrix[row+1][coloumn+1] + matrix[row+2][coloumn+2] + matrix[row+3][coloumn+3])
    
    # S
    words.append(matrix[row][coloumn] + matrix[row+1][coloumn] + matrix[row+2][coloumn] + matrix[row+3][coloumn])

    # SW
    words.append(matrix[row][coloumn] + matrix[row+1 ][coloumn-1] + matrix[row+2][coloumn-2] + matrix[row+3][coloumn-3])

    # W
    words.append(matrix[row][coloumn] + matrix[row][coloumn - 1] + matrix[row][coloumn - 2] + matrix[row][coloumn - 3])

    # NW
    words.append(matrix[row][coloumn] + matrix[row-1][coloumn-1] + matrix[row-2][coloumn-2] + matrix[row-3][coloumn-3])

    return words.count("XMAS")


def count_cross_mas(matrix, cell):
    row, coloumn = cell
    
    # Write down the cells in the following order and check for viable options
    # 1   2
    #   A
    # 4   3
    
    structure = matrix[row-1][coloumn-1] + matrix[row-1][coloumn+1]  + matrix[row+1][coloumn+1] + matrix[row+1][coloumn-1]

    if structure in ['MSSM', 'MMSS', 'SSMM', 'SMMS']:
        return 1
    
    return 0

def build_matrix(words):
    """
     Creates a matrix holding the words
     Encapsulates the matrix in enough cells to check each direction without
     the need to check index constraints
    """
    
    matrix = []
    header_footer = ['*'] * (len(words) + 6)
    for _ in range(3):
        matrix.append(header_footer)

    for line in words:
        filler = ['*', '*', '*']
        matrix.append(filler + list(line) + filler)

    for _ in range(3):
        matrix.append(header_footer)

    return matrix

def print_matrix(matrix):
    for line in matrix:
        print(line)


if __name__ == '__main__':

    words = read_file(input).split("\n")
    xmas_matrix = build_matrix(words)
    print_matrix(xmas_matrix)

    xmas_count = 0
    cross_mas_count = 0
    for i in range(len(xmas_matrix)):
        for j in range(len(xmas_matrix)):
            
            if(xmas_matrix[i][j] == 'X'):
                xmas_count += count_xmas(xmas_matrix, (i,j))
            elif(xmas_matrix[i][j] == 'A'):
                cross_mas_count += count_cross_mas(xmas_matrix, (i,j))

    print(cross_mas_count)


    
