from PuzzleClass import PuzzleState
import heapq

#implementation of function "A Star Misplaced"


class A_star_Misplaced:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        
    def solve(self):
        pqueue = []
        explored = set()
        currentState = self.puzzle
        explored.add(currentState.boardState())
        first = True
        gn = 0
        counter = 0
        while first or pqueue:
            if first:
                first = False
            if currentState.isFinished():
                return currentState.path()
            gn += 1
            for frontierState in currentState.expandFrontier():
                fn = self.misplacedHelper(frontierState) + gn
                newState = PuzzleState(frontierState, currentState)
                if newState.boardState() not in explored:
                    explored.add(newState.boardState())
                    if newState.isFinished():
                        return newState.path()
                    heapq.heappush(pqueue, (fn, gn, frontierState, newState))                   
            heapItem = heapq.heappop(pqueue)
            gn = heapItem[1]
            currentState = heapItem[3]
            counter += 1
            #To stop in case of unsolvable puzzle
            if counter == 100000000:
                print("Puzzle is unsolvable.")
                break              
        return currentState.path()
 
    def misplacedHelper(self, puzzle):
        misplaced = 0
        for tile in puzzle:
            if tile != puzzle.index(tile):
                misplaced +=1
        return misplaced