from PuzzleClass import PuzzleState

#implementation of function "Iterative_deepening_DFS"
# ~ 4-5 minutes to do all 100 puzzle cases
class iddfs:
    def __init__(self, p):
        self.puzzle = p
    
    def solve(self):
        for depth in range(100):
            explored = set()                            # reset explored set
            current = self.puzzle                       # reset root node
            explored.add(current.boardState())          # add root node to explored set
            result = self.dfs(current, explored, depth) # call dfs(node, explored, depth)
            if result != None:                          # check if result is solved, else continue looping
                if result.isFinished():
                    return result.path()
        if result == None:
            print("no solutions found")
        return self.puzzle.path()
        
    def dfs(self, current, explored, depth):
        if current.isFinished():                          # return if current node is 
            return current
        if depth == 0:                                    # return None if depth is 0
            return None
        if depth > 0:                                     # if depth > 0
            substack = []                                 # create a substack
            stack = current.expandFrontier()              # put adjacent nodes into stack
            for board in stack:                           # loop through stack
                newState = PuzzleState(board, current)
                if newState.boardState() not in explored: # if node not in explored set
                    explored.add(newState.boardState())   # add to explored set
                    if newState.isFinished():             # if node is solved, return node
                        return newState 
                    substack.append(newState)             # add node to substack
            for state in substack:                        # loop through substack
                result = self.dfs(state, explored, depth-1) # recursive call to dfs(adjacent node, explored, depth-1)
                if result != None:                        # if result is solved, return result, else continue
                    if result.isFinished():
                        return result
            return None
 