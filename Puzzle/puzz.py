puzzle_number = 0 
input_file  =  open( r"C:\Users\mounika\Desktop\puzzle\puzz.txt", 'r') # Reading input file
puzzle_list = []

for row in range(5):
    input_line = input_file.readline()
    input_line = input_line.rstrip('\n')
    if len(input_line)!=5:
        input_line = input_line + ' '
    puzzle_list.append(input_line)

while puzzle_list[0] != 'Z':

    puzzle_number += 1
    splitted_puzzle = []
    for each_string in puzzle_list:
        for character in each_string:
            splitted_puzzle.append(character)
    blank = splitted_puzzle.index(' ')
    moves = input_file.readline()

    while 'O' not in list(moves):
        moves = moves + input_file.readline()

    count = 0 
    for move in moves:
       

        def above(splitted_puzzle,blank):
            if blank >= 4:
                new_blank = blank - 5
                splitted_puzzle[blank],splitted_puzzle[new_blank] = splitted_puzzle[new_blank],splitted_puzzle[blank]
                return splitted_puzzle,new_blank,0
            else:
                return splitted_puzzle,blank ,1
       

        def Below(splitted_puzzle , blank):
            if blank <= 20:      
                new_blank = blank + 5
                splitted_puzzle[blank],splitted_puzzle[new_blank] = splitted_puzzle[new_blank],splitted_puzzle[blank]
                return splitted_puzzle,new_blank,0
            else:
                return splitted_puzzle,blank ,1


        def Left(splitted_puzzle, blank):
            if (blank != 0 and blank != 5 and blank != 10 and blank != 15 and blank != 20):
                new_blank = blank - 1
                splitted_puzzle[blank],splitted_puzzle[new_blank] = splitted_puzzle[new_blank],splitted_puzzle[blank]
                return splitted_puzzle,new_blank,0
            else:
                return splitted_puzzle,blank ,1


        def Right(splitted_puzzle,blank):
            if (blank != 4 and blank != 9 and blank != 14 and blank != 19 and blank != 24):
                new_blank = blank + 1
                splitted_puzzle[blank],splitted_puzzle[new_blank] = splitted_puzzle[new_blank],splitted_puzzle[blank]
                return splitted_puzzle,new_blank,0
            else:
                return splitted_puzzle,blank ,1


        if (move == 'A'):   
            splitted_puzzle,blank,invalid = above(splitted_puzzle,blank)
            count += invalid
        if (move == 'B'):
            splitted_puzzle,blank,invalid = Below(splitted_puzzle,blank)
            count += invalid
        if (move == 'L'):
            splitted_puzzle,blank,invalid = Left(splitted_puzzle,blank)
            count += invalid
        if (move == 'R'):
            splitted_puzzle,blank,invalid = Right(splitted_puzzle,blank)
            count += invalid

    if count != 0:# for invalid moves
        print('\n')
        print(f'Puzzle #{puzzle_number}:')
        print("This puzzle has no final configuration")
    else:
        print('\n')
        print(f'Puzzle #{puzzle_number}:')
        for position in range(25):
            print(splitted_puzzle[position],sep='',end=" ")
            if (position == 4 or position == 9 or position == 14 or position == 19):
                print("\n")
    puzzle_list = []
    for row in range(5):
        each_line = input_file.readline()
        each_line = each_line.rstrip('\n')
        if len(each_line)!=5:
            each_line = each_line + ' '
        puzzle_list.append(each_line)
input_file.close()