from itertools import combinations
from functools import reduce

def fitness(board):
	return numCombinations(board) - attackingQueens(board)
	
def attackingQueens(rowString):
	board = getBoard(rowString)
	diagCount = countDiags(board)
	rowCount = countRows(board)
	return rowCount + diagCount
	
def countRows(board):
	newBoard = board
	boardSize = len(newBoard)
	
	if boardSize == 0:
		return 0
		
	else:
		elem = newBoard.pop()
		return reduce(lambda x, y: x + 1 if y[0] == elem[0] else x, newBoard,
                0) + countRows(newBoard)

def countDiags(board):
    return len(list(filter(isDiag, genPairs(board))))

def genPairs(board):
    return list(combinations(board, 2))

def isDiag(pair):
    A, B = pair
    slope = (A[0] - B[0]) / (A[1] - B[1])
    if abs(slope) == 1:
        return True
    else:
        return False
    
def getBoard(rowString):
    return [(int(r), c+1) for (c,r) in enumerate(rowString)]

def numCombinations(board):
    return len(genPairs(board))