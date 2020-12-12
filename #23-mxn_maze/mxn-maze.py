from collections import deque;

board = [[False, False, False, False], 
        [True, True, False, True], 
        [False, False, False, False], 
        [False, False, False, False], 
        [True, True, True, True]]

start = [3, 0]
end = [0, 0]

reached = False
path = [0]

def getWalkableNeighbors(board, row, col):
  m, n = len(board), len(board[0])
  up = down = left = right = True
  walkable = []
  if (row > 0) and (board[row-1][col] == False):  # not at top of board
    walkable.append((row-1, col))
  if (row < m - 1) and (board[row+1][col] == False):  # not at bottom of board
    down = board[row+1][col]
    walkable.append((row+1, col))
  if (col > 0) and (board[row][col-1] == False):  # not at left side
    left = board[row][col-1]
    walkable.append((row, col-1))
  if (col < n - 1) and (board[row][col+1] == False):  # not at right side
    right = board[row][col + 1]
    walkable.append((row, col-1))

  print('walk: ', walkable)
  
  # result = []
  # for each in [up, right, down, left]:
  #   print('each', each)
  #   if 

  return [up, right, down, left]

def walkable(neighbors):
  res = []
  for each in neighbors:
    if each == False:
      res.append(each)
  return res

  

# print(result)

def shortest_path(board, start, end):
  visited = set()  # keep track of visited spots on board
  queue = deque([(start), 0])
  print('init: ', queue)
  while queue:
    coords = queue.popleft()
    count = queue.popleft()
    # if we are at the end, return number of steps
    if coords == end:
      return count
    
    visited.add(coords)
    neighbors = getWalkableNeighbors(board, coords[0], coords[1])
    print('neigh: ', neighbors)
    for neighbor in neighbors:
      if neighbor not in visited:
        queue.extend((neighbor, count+1))
    print('here: ', coords, count)


(shortest_path(board, (3,0), (0,0)))