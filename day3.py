#only for Part 1 of day 3

#open file
forestFile=open(('/home/anjab/PycharmProjects/AdventofCode/venv/numbers.txt'), 'r')
forestList=forestFile.readlines()

treeCount=0

#skip first line
#second line: index 3 check which character, if #, treeCount+1
#next line: index 3+3 check which character
index=0
lineCount=0
for forestString in forestList:

    for i in range(5):
        forestString=forestString.rstrip('\r\n')+forestString.rstrip('\r\n')
    #skip first line
    if(index==0):
        index=1
        continue
    try:
        if(forestString[index]== '#'):
            treeCount=treeCount+1
    except:
        break

    index=index+1
    lineCount=lineCount+1
    if(lineCount==323):
        break

print(treeCount)





# from typing import Tuple
#
# with open('/home/anjab/PycharmProjects/AdventofCode/venv/numbers.txt') as file:
#     input = file.readlines()
#
# puzzle_input = [line.strip() for line in input]
#
# two_d_array = []
# for line in puzzle_input:
#     two_d_array.append([char for char in line])
#
# horizontal_length = len(two_d_array[0])
# vertical_length = len(two_d_array)
#
# slopes = [
#     {"horizontal_shifts": 1, "vertical_shifts": 1},
#     {"horizontal_shifts": 3, "vertical_shifts": 1},
#     {"horizontal_shifts": 5, "vertical_shifts": 1},
#     {"horizontal_shifts": 7, "vertical_shifts": 1},
#     {"horizontal_shifts": 1, "vertical_shifts": 2},
# ]
#
# def over_three_down_one(
#     current_row: int,
#     current_column: int,
#     horizontal_shifts: int,
#     vertical_shifts: int) -> Tuple[int, int]:
#
#     current_row += vertical_shifts
#     current_column += horizontal_shifts
#     if current_column > (horizontal_length - 1):
#         current_column = (current_column%horizontal_length)
#     return current_row, current_column
#
# def traverse_slope(horizontal_shifts: int, vertical_shifts: int) -> int:
#
#     current_row = 0
#     current_column = 0
#     tree_collisions = 0
#
#     while current_row < vertical_length - 1:
#         current_row, current_column = over_three_down_one(
#             current_row,
#             current_column,
#             horizontal_shifts,
#             vertical_shifts)
#         if two_d_array[current_row][current_column] == '#':
#             tree_collisions += 1
#
#     return tree_collisions
#
# answer = 1
# for slope in slopes:
#     print(traverse_slope(slope['horizontal_shifts'], slope['vertical_shifts']))
#     answer *= traverse_slope(slope['horizontal_shifts'], slope['vertical_shifts'])
#
# print(f'Answer: {answer}')
