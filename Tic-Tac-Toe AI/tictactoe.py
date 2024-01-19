import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    countX = 0
    countO = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1

    if countX == countO:
        return X
    else:
        return O

def actions(board):
    possible_actions = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))
    return possible_actions

def result(board, action):
    if action not in actions(board):
        raise Exception("Not a valid move")
    
    i = action[0]
    j = action[1]
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board)

    return board_copy

def winner(board):
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

def terminal(board):
    if winner(board) is not None:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    
    return True

def utility(board):
    res = winner(board)
    if res == X:
        return 1
    elif res == O:
        return -1
    else:
        return 0

def min_value(board):
    if terminal(board):
        return utility(board)
    
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def minimax(board):
    if terminal(board):
        return None
    elif player(board) == X:
        move = []
        for action in actions(board):
            move.append([min_value(result(board,action)), action])
        return sorted(move, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == O:
        move = []
        for action in actions(board):
            move.append([max_value(result(board,action)), action])
        return sorted(move, key=lambda x: x[0])[0][1]