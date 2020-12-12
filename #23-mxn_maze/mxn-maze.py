board = [['f', 'f', 'f', 'f'], ['t', 't', 'f', 't'], ['f', 'f', 'f', 'f'], ['f', 'f', 'f', 'f'], ['t', 't', 't', 't']]

start = [3, 0]
end = [0, 0]

reached = False
path = [0]

def getNeighbors(board, row, col):
  m, n = len(board), len(board[0])
  up = down = left = right = None
  if row > 0:
    up = board[row-1][col]
  if row < m - 1:
    down = board[row+1][col]
  if col > 0 :
    left = board[row][col-1]
  if col < n - 1:
    right = board[row][col + 1]

  return [up, right, down, left]

# [u, r, d, l] = getNeighbors(board, 4,3)
# print(u, d, r, l)

current = start
# pick starting direction
if start[0] > end[0]:
  direction = "n"


while not reached:
  print('not reached', current[0], current[1])

  if (current[0] == end[0]) and (current[1] == end[0]):
    print("End reached, path length=", len(path))
    break
  # reached = not reached

  # return a list of directions [up, right, down, left]
  neighbors = getNeighbors(board, current[0], current[1])
  print('neighbors: ', neighbors)
  
  if "f" not in neighbors:
    shortest = "No solution"
    break

  if current[0] > end[0]:
    current = [current[0]-1,current[1]]
  elif current[0] < end[0]:
    current = [current[0]+1, current[1]]
  else:
    current = [current[]]

  

# print(result)