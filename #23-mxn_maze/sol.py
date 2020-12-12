from collections import deque

# Given a row and column, returns whether that tile is walkable.
def walkable(board, row, col):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False
    # print('walkable', not board[row][col])
    return not board[row][col]  # returns True or False

# Gets walkable neighbouring tiles.
def get_walkable_neighbours(board, row, col):
    # returns all neighbors that are walkable (row, col)
    return [(r, c) for r, c in [
        (row, col - 1),
        (row - 1, col),
        (row + 1, col),
        (row, col + 1)]
        if walkable(board, r, c)
    ]

def shortest_path(board, start, end):
    seen = set()
    queue = deque([(start, 0)])
    while queue:
        coords, count = queue.popleft()
        if coords == end:
            return count
        seen.add(coords)
        neighbours = get_walkable_neighbours(board, coords[0], coords[1])
        print('neigh: ', neighbours)
        queue.extend((neighbour, count + 1) for neighbour in neighbours
                if neighbour not in seen)

board = [[False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]]

print(shortest_path(board, (3, 0), (0, 0)))