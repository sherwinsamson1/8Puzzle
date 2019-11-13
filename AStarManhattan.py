from PuzzleClass import PuzzleState
import heapq

#implementation of function "A Star Manhattan Distance"


class A_star_Manhattan:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.tileDistanceMatrix = [
            [0, 1, 2, 1, 2, 3, 2, 3, 4],
            [1, 0, 1, 2, 1, 2, 3, 2, 3],
            [2, 1, 0, 3, 2, 1, 4, 3, 2],
            [1, 2, 3, 0, 1, 2, 1, 2, 3],
            [2, 1, 2, 1, 0, 1, 2, 1, 2],
            [3, 2, 1, 2, 1, 0, 3, 2, 1],
            [2, 3, 4, 1, 2, 3, 0, 1, 2],
            [3, 2, 3, 2, 1, 2, 1, 0, 1],
            [4, 3, 2, 3, 2, 1, 2, 1, 0]
        ]
          
    def solve(self):
        pqueue = []
        explored = set()
        currentState = self.puzzle
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
                fn = self.ManhattanHelper(frontierState) + gn
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
                print("Puzzle is unsolvable")
                break           
        return currentState.path()
    
    
    def ManhattanHelper(self, puzzle):
        hn = 0
        for tile in puzzle:
            hn += self.tileDistanceMatrix[tile][puzzle.index(tile)]
        return hn