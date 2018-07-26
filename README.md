# N-Queens & N-Rooks
A python based implementation for the N-Queens & N-Rooks problem.  
Principle - Backtracking

#### Input - 4 parameters (2 optional)
#### Output - All possible solutions printed to the primary display channel (id=0)

## Instructions
To run the program, simply enter the dimensions of the board with the mode in which you'd like to run the program as command line arguments. For editors/IDEs with integrated build + run systems, you only need to enter the paramters in bold.

_Windows or Linux_ = python a0.py __\<mode>__ __\<dimension>__ __\<blockedX>__ __\<blockedY>__  
_mac OSX_          = python3 a0.py __\<mode>__ __\<dimension>__ __\<blockedX>__ __\<blockedY>__
  
where,
* dimension = an integer value
* mode = nrooks or nqueens
* blockedX = x-coordinate of the blocked/occupied cell in the catesian coordinate system
* blockedY = y-coordinate of the blocked/occupied cell in the catesian coordinate system

_Note = the shebang on line 1 of the program handles the case of selecting python3 when you have both python2 and python3 installed_

## Requirements:
* Python 3.6.5 or above

## Sample Run Times (N-Queens):
* Board Size = 4
  Wall-clock Time = 0.593s
  Process Time = 0.483s
* Board Size = 8
  Wall-clock Time = 0.662s 
  Process Time = 0.587s
* Board Size = 16
  Wall-clock Time = Indeterminate
  Process Time = Indeterminate
