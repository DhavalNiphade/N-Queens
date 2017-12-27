#!/usr/bin/env python3
#N-queens and N-rooks problem
#Created September 9, 2017 by Dhaval R Niphade

# The N-rooks / N-queens problem is: Given an empty NxN chessboard, place N rooks / queens on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

import sys,gc

#Check validity of Rook placement
def isValidRook(board,row,col):
    for i in range(0,row):  #Found a Rook in the same col.
        if(board[i][col])==1:
            return False
    return True

#Check validity of Queen placement
def isValidQueen(board,row,col,N):
    for i in range(0,row):  #Checking the same column
        if(board[i][col]==1):
            return False

    for (i,j) in zip(range(row-1,-1,-1),range(col-1,-1,-1)):    #First Diagonal
        if(board[i][j])==1:
            return False

    for (i,j) in zip(range(row-1,-1,-1),range(col+1,N)):        #Second Diagonal
        if(board[i][j]==1):
            return False

    return True

def solveNRooks(board,row,N):
    if(row==N):
        print("\n".join([" ".join(["X" if col == -1 else ("R" if col else "_") for col in row]) for row in board]))
        exit(0)
    for col in range(0,N):
        if(isValidRook(board,row,col)):
            if (board[row][col]):
                continue
            board[row][col]=1
            solveNRooks(board,row+1,N)
            board[row][col]=0

def solveNQueens(board,row,N):
    if(row==N):
        print("\n".join([" ".join(["X" if col == -1 else ("Q" if col else "_") for col in row]) for row in board]))
        exit(0)
    for col in range(0,N):
        if(isValidQueen(board,row,col,N)):
            if(board[row][col]):
                continue
            board[row][col]=1
            solveNQueens(board,row+1,N)
            board[row][col]=0

def driver(args):
    mode = args[1]  #Parse arguments and build the program
    N = int(args[2])
    x = int(args[3])-1
    y = int(args[4])-1
    #board = [[0] * N] * N #Initialize board
    board = [[0 for temp in range(N)] for temp in range(N)]
    board[x][y]=-1
    if(mode=="nrook"):
        solveNRooks(board,0,N)
        print("No solution found")
    elif(mode=="nqueen"):
        solveNQueens(board,0,N)
        print("No solution found")
    else:
        gc.collect(board)
        print("Incorrect mode entered.\nPlease check your arguments again. Description below:\nFor N-rooks enter 'nrook'\nFor N-queens enter nqueen")
    return

if __name__ == "__main__":
    driver(sys.argv)

