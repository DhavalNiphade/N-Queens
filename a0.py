#!/usr/bin/env python3

# N-queens and N-rooks problem
# Created September 9, 2017 by Dhaval R Niphade

# The N-rooks / N-queens problem is: Given an empty NxN chessboard, place N rooks / queens on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

# Please note that this is a very rudimentary implementation of the solution to the problem and can be optimized in a large number of ways
# For a much optimized version that uses a bitboard and has just 22 lines of code (including the driver) please leave a message.


import sys
from copy import deepcopy

#---------------------------- Utility functions -----------------------------#

'''Print function for all solutions that were found'''
def printSolutions(allSolutions,mode):

    if allSolutions:
        if mode == "nrooks":
            for board in allSolutions:
                print("\n".join([" ".join(["X" if col == -1 else ("R" if col else "_") for col in row]) for row in board]),"\n")


        if mode=="nqueens":
            for board in allSolutions:
                print("\n".join([" ".join(["X" if col == -1 else ("Q" if col else "_") for col in row]) for row in board]),"\n")


        return

    print("Something went wrong")
    return


#---------------------------- Validity functions -----------------------------#


'''Check validity of Rook placement'''
def isValidRook(board,row,col):
    for i in range(0,row):  #Found a Rook in the same col.
        if(board[i][col])==1:
            return False
    return True

''' Check validity of Queen placement '''
def isValidQueen(board,row,col,N):
    for i in range(0,row):                            # Checking the same column
        if(board[i][col]==1):
            return False

    for (i,j) in zip(range(row-1,-1,-1),range(col-1,-1,-1)):    # First Diagonal
        if(board[i][j])==1:
            return False

    for (i,j) in zip(range(row-1,-1,-1),range(col+1,N)):       # Second Diagonal
        if(board[i][j]==1):
            return False

    return True

#----------------------------- Backtracking functions ------------------------#

'''N-Rooks solver
# board = NxN dimension board represented as a 2 dimensional array (for higher speeds convert to either numpy array or one dimensional array and work with the % operator)
# row = current row in which to place the queen
# N = dimension of the board
# numSolutions = number of solutions found so far
# allSolutions = a set containing all unique solutions found so far. For higher speed, use with numpy array and run np.unique(allSolutions,axis=0) once all possiblesolutions are found'''
def solveNRooks(board,row,N,numSolutions,allSolutions):
    if(row==N):
        allSolutions.append(deepcopy(board))
        numSolutions+=1
        return
    for col in range(0,N):
        if(isValidRook(board,row,col)):
            if (board[row][col]):
                continue
            board[row][col]=1
            solveNRooks(board,row+1,N,numSolutions,allSolutions)
            board[row][col]=0

'''N-Queens solver
# board = NxN dimension board represented as a 2 dimensional array (for higher speeds convert to either numpy array or one dimensional array and work with the % operator)
# row = current row in which to place the queen
# N = dimension of the board
# numSolutions = number of solutions found so far
# allSolutions = a set containing all unique solutions found so far. For higher speed, use with numpy array and run np.unique(allSolutions,axis=0) once all possiblesolutions are found'''
def solveNQueens(board,row,N,numSolutions,allSolutions):
    if(row==N):
        allSolutions.append(deepcopy(board))
        numSolutions+=1
        return
    for col in range(0,N):
        if(isValidQueen(board,row,col,N)):
            if(board[row][col]):
                continue
            board[row][col]=1
            solveNQueens(board,row+1,N,numSolutions,allSolutions)
            board[row][col]=0

''' Main() function for the program '''
def driver(args):
    mode = args[1].lower()  # Parse arguments and build the program
    N = int(args[2])   # Dimensions of the board
    x = int(args[3])-1 if args[3] else -1 # x-coordinate of the blocked cell
    y = int(args[4])-1 if args[4] else -1 # y-coordinate of the blocked cell

    # Intialize the board and the solutions container
    board = [[0 for temp in range(N)] for temp in range(N)]
    allSolutions = list()

    # For placing the blank piece
    if (0<x<N and 0<y<N):
        board[x][y]=-1


    # Control for mode
    if(mode=="nrooks"):
        solveNRooks(board,0,N,0,allSolutions)
        printSolutions(allSolutions,mode)
    elif(mode=="nqueens"):
        solveNQueens(board,0,N,0,allSolutions)
        printSolutions(allSolutions,mode)
    else:
        print("Incorrect mode entered.\nPlease check your arguments again. Description below:\nFor N-rooks enter 'nrook'\nFor N-queens enter nqueen")

    if allSolutions:
        print(len(allSolutions)," solutions found")
        return

    print("No solutions found")
    return

if __name__ == "__main__":
    driver(sys.argv)
