
#
# PuzzleState acts like a linked list to help with getting the path to solution
import time
# result for print function
class PuzzleState:
    def __init__(self, initPuzzle, lastState=None):
        self.puzzle = initPuzzle
        self.lastState = lastState
    
    def isFinished(self):
        return self.puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    def getCopy(self):
        copy = []
        for x in self.puzzle:
            copy.append(x)
        return copy
    
    def boardState(self):
        return str(self.puzzle)
    
    def path(self):
        currentState = self
        path = []
        while (currentState != None):
            path.insert(0, currentState)
            currentState = currentState.lastState
        return path
    
    def makeMove(self, index0, target):
        newBoard = self.getCopy()
        temp = newBoard[target]
        newBoard[target] = 0
        newBoard[index0] = temp
        return newBoard
    
    def expandFrontier(self):
        newBoards = []
        position0 = self.puzzle.index(0)
        
        if position0 == 0:
            newBoards.append(self.makeMove(0,1))
            newBoards.append(self.makeMove(0,3))
        elif position0 == 1:
            newBoards.append(self.makeMove(1,0))
            newBoards.append(self.makeMove(1,2))
            newBoards.append(self.makeMove(1,4))
        elif position0 == 2:
            newBoards.append(self.makeMove(2,1))
            newBoards.append(self.makeMove(2,5))
        elif position0 == 3:
            newBoards.append(self.makeMove(3,0))
            newBoards.append(self.makeMove(3,4))
            newBoards.append(self.makeMove(3,6))
        elif position0 == 4:
            newBoards.append(self.makeMove(4,1))
            newBoards.append(self.makeMove(4,3))
            newBoards.append(self.makeMove(4,5))
            newBoards.append(self.makeMove(4,7))
        elif position0 == 5:
            newBoards.append(self.makeMove(5,2))
            newBoards.append(self.makeMove(5,4))
            newBoards.append(self.makeMove(5,8))
        elif position0 == 6:
            newBoards.append(self.makeMove(6,3))
            newBoards.append(self.makeMove(6,7))
        elif position0 == 7:
            newBoards.append(self.makeMove(7,4))
            newBoards.append(self.makeMove(7,6))
            newBoards.append(self.makeMove(7,8))
        elif position0 == 8:
            newBoards.append(self.makeMove(8,5))
            newBoards.append(self.makeMove(8,7))
        return newBoards
    
    def printout(self):
        count = 0
        for x in self.puzzle:
            if count == 2 or count == 5:
                print(x)
            else:
                print(str(x) + " ", end=" ")
            count+=1
        print("\n")