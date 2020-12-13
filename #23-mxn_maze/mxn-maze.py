from collections import deque;

board = [[False, False, False, False], 
        [True, True, False, True], 
        [False, False, False, False], 
        [False, False, False, False], 
        [True, True, True, True]]

def getWalkableNeighbors(board, row, col):
  m, n = len(board), len(board[0])
  walkable = []

  # determine if neighbors are walkable (not "t")
  if (row > 0) and (board[row-1][col] == False):  # not at top of board
    walkable.append((row-1, col))
  if (row < m - 1) and (board[row+1][col] == False):  # not at bottom of board
    walkable.append((row+1, col))
  if (col > 0) and (board[row][col-1] == False):  # not at left side
    walkable.append((row, col-1))
  if (col < n - 1) and (board[row][col+1] == False):  # not at right side
    walkable.append((row, col+1))

  return walkable  

def shortest_path(board, start, end):
  visited = set()  # keep track of visited spots on board
  queue = deque([(start), 0])  # add starting location, and count = 0 to queue

  while queue:
    coords = queue.popleft()
    count = queue.popleft()
    # if at the end, return number of steps
    if coords == end:
      return count

    visited.add(coords)
    neighbors = getWalkableNeighbors(board, coords[0], coords[1])
    for neighbor in neighbors:
      if neighbor not in visited:
        queue.extend((neighbor, count+1))


print("shortest path = ", shortest_path(board, (3,0), (0,0)))