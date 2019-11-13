from PuzzleClass import PuzzleState

#implementation of function "breadthFirstSearch" (for graduate students)
# ~15 minutes to finish 100 puzzle cases
class bfs:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        
    def solve(self):
        queue = []
        explored = set()
        currentState = self.puzzle
        first = True
        #counter = 0
        while first or queue:
            if first:
                first = False
            for frontierState in currentState.expandFrontier():
                newState = PuzzleState(frontierState, currentState)
                if newState.boardState() not in explored:
                    explored.add(newState.boardState())
                    queue.append(newState)
                    if newState.isFinished():
                        return newState.path()
            currentState = queue[0]
            queue = queue[1:]
        return currentState.path()