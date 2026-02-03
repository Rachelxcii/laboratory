# Date: 2022-03-10
# Problem: Check Sudoku (LeetCode)
# Insight: Check if grid provided is a sudoku solution
# Complexity: Time O(n²), Space O(n²)


def check_sudoku_solution(grid: list) -> bool:

    dictionary = {}
    
    for row in range(len(grid)):
        for column in range(len(grid)):
            
            name_row = 'r' + str(row)
            name_column = 'c' + str(column)
            name_subgrid = 'sg' + str(row//3) + str(column//3)
            
            if name_row not in dictionary: dictionary[name_row] = []
            if name_column not in dictionary: dictionary[name_column] = []
            if name_subgrid not in dictionary: dictionary[name_subgrid] = []
            
            if grid[row][column] not in dictionary[name_row]:
                dictionary[name_row].append(grid[row][column])
            else:
                return False
            
            if grid[row][column] not in dictionary[name_column]:
                dictionary[name_column].append(grid[row][column])
            else:
                return False
                
            if grid[row][column] not in dictionary[name_subgrid]:
                dictionary[name_subgrid].append(grid[row][column])
            else:
                return False
    
    return True
