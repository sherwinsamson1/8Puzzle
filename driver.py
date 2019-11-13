from PuzzleClass import PuzzleState
from iddfs import iddfs
from bfs import bfs
from AStarMisplaced import A_star_Misplaced
from AStarManhattan import A_star_Manhattan
import time

def do_the_rest_Manhattan(PuzzleFile, timelist, moveslist):
    counter = 0
    for line in PuzzleFile:
        state = PuzzleState(createPuzzle(line))
        ready = A_star_Manhattan(state)
        start = time.time()
        solved = ready.solve()
        end = time.time()
        timespent = end - start
        timelist.append(timespent)
        moveslist.append(len(solved))
        counter += 1
        #printPuzzleSolution(solved)
        #break
        print(str(counter))

def do_the_rest_misplaced(PuzzleFile, timelist, moveslist):
    counter = 1
    for line in PuzzleFile:
        state = PuzzleState(createPuzzle(line))
        ready = A_star_Misplaced(state)
        start = time.time()
        solved = ready.solve()
        end = time.time()
        timespent = end - start
        timelist.append(timespent)
        moveslist.append(len(solved))
        counter += 1
        print(str(counter))
    
def do_the_rest_iddfs(PuzzleFile, timelist, moveslist):
    counter = 1
    for line in PuzzleFile:
        state = PuzzleState(createPuzzle(line))
        ready = iddfs(state)
        start = time.time()
        solved = ready.solve()
        end = time.time()
        timespent = end - start
        timelist.append(timespent)
        moveslist.append(len(solved))
        counter += 1
        print(str(counter))

def createPuzzle(line):
    puzzle = []
    for x in line:
        if x.isdigit():
            puzzle.append(int(x))
    return puzzle

def printPuzzleSolution(seq):
    first = True
    for puzzle in seq:
        if first:
            first = False
        else:
            print("to\n")
        puzzle.printout()

def do_the_rest_bfs(PuzzleFile, timelist, moveslist):
    counter = 0
    for line in PuzzleFile:
        state = PuzzleState(createPuzzle(line))
        ready = bfs(state)
        start = time.time()
        solved = ready.solve()
        end = time.time()
        timespent = end - start
        timelist.append(timespent)
        moveslist.append(len(solved))
        counter += 1
        if (counter == 1):
            printPuzzleSolution(solved)
        print(str(counter))





##################################################################################         
print("Starting IDDFS...\n\n")
PuzzleFile = open('Input8PuzzleCases.txt')
startingPuzzle = createPuzzle(PuzzleFile.readline())
state = PuzzleState(startingPuzzle)
firstPuzzle = iddfs(state)

iddfsTimeList = []
iddfsMovesList = []
result=[]

# solving the first puzzle
start = time.time()
solvedFirst = firstPuzzle.solve()
end = time.time()
timespent = end - start
iddfsTimeList.append(timespent)
iddfsMovesList.append(len(solvedFirst))
# result for print function
result.append(solvedFirst)
printPuzzleSolution(solvedFirst)

# solve the rest of the puzzles with iddfs
do_the_rest_iddfs(PuzzleFile, iddfsTimeList, iddfsMovesList)

# calculate average time and steps for iddfs
totaltime = 0
totalmoves = 0
for times in iddfsTimeList:
    totaltime += times
for moves in iddfsMovesList:
    totalmoves += moves
iddfsavgtime = int(totaltime)/int(len(iddfsTimeList))
iddfsavgmoves = float(totalmoves)/float(len(iddfsMovesList))

# result for print function
result.append(iddfsavgtime)
result.append(iddfsavgmoves)

print("Average Steps for IDDFS: " + str(iddfsavgmoves))
print("Average Time for IDDFS: %.2f" % iddfsavgtime + " seconds")
PuzzleFile.close()
print("\n\nEnd of IDDFS\n")

##################################################################################
print("Starting BFS..\n\n")
PuzzleFile = open("Input8PuzzleCases.txt")

bfsTimeList = []
bfsMovesList = []

do_the_rest_bfs(PuzzleFile, bfsTimeList, bfsMovesList)

totaltime = 0
totalmoves = 0
for times in bfsTimeList:
    totaltime += times
for moves in bfsMovesList:
    totalmoves += moves
bfsavgtime = int(totaltime)/int(len(bfsTimeList))
bfsavgmoves = float(totalmoves)/float(len(bfsMovesList))

result.append(bfsavgtime)
result.append(bfsavgmoves)

print("Average Steps for BFS: " + str(bfsavgmoves))
print("Average Time for BFS: %.2f" % bfsavgtime + " seconds")

PuzzleFile.close()
print("\n\nEnd of BFS.\n")


##################################################################################        
print("Starting A* Misplaced Tile Heuristic...\n\n")
PuzzleFile = open("Input8PuzzleCases.txt")
startingPuzzle = createPuzzle(PuzzleFile.readline())
#startingPuzzle = [3, 1, 2, 0, 4, 5, 6, 7, 8]
state = PuzzleState(startingPuzzle)
firstPuzzle = A_star_Misplaced(state)

misplace_TimeList = []
misplace_MovesList = []

# solving the first puzzle
start = time.time()
solvedFirst = firstPuzzle.solve()
end = time.time()
timespent = end - start
misplace_TimeList.append(timespent)
misplace_MovesList.append(len(solvedFirst))
# result for print function
result.append(solvedFirst)
printPuzzleSolution(solvedFirst)

# solve the rest of the puzzles with iddfs
do_the_rest_misplaced(PuzzleFile, misplace_TimeList, misplace_MovesList)

# calculate average time and steps for iddfs
totaltime = 0
totalmoves = -1
for times in misplace_TimeList:
    totaltime += times
for moves in misplace_MovesList:
    totalmoves += moves
misplace_avgtime = int(totaltime)/int(len(misplace_TimeList))
misplace_avgmoves = float(totalmoves)/float(len(misplace_MovesList))

# result for print function
result.append(misplace_avgtime)
result.append(misplace_avgmoves)

print("Average Steps for Miss Placed: " + str(misplace_avgmoves))
print("Average Time for Miss Placed: %.2f" % misplace_avgtime + " seconds")
PuzzleFile.close()
print("\n\nEnd of Miss Placed\n")


##################################################################################   
print("Starting A* Manhattan Distance..\n\n")
PuzzleFile = open("Input8PuzzleCases.txt")

Manhattan_TimeList = []
Manhattan_MovesList = []

do_the_rest_Manhattan(PuzzleFile, Manhattan_TimeList, Manhattan_MovesList)

totaltime = 0
totalmoves = -1
for times in Manhattan_TimeList:
    totaltime += times
for moves in Manhattan_MovesList:
    totalmoves += moves
Manhattan_avgtime = int(totaltime)/int(len(Manhattan_TimeList))
Manhattan_avgmoves = float(totalmoves)/float(len(Manhattan_MovesList))

result.append(Manhattan_avgtime)
result.append(Manhattan_avgmoves)

print("Average Steps for Manhattan Distance: " + str(Manhattan_avgmoves))
print("Average Time for Manhattan Distance: %.2f" % Manhattan_avgtime + " seconds")

PuzzleFile.close()
print("\n\nEnd of Manhattan Distance.\n")