#!/usr/bin/env python3

def checkmate(board):

    lines = [line for line in board.strip().split('\n') if line.strip()]
    if not lines:
        return False 

    size = len(lines)
    for row in lines:
        if len(row) != size:
            print("Error")
            return False   
    
    king_pos = None 
    king_count = 0 
    pieces_type = ('K', 'Q', 'R', 'B', 'P') 

    for i in range(size):
        for j in range(size):
            cell = lines[i][j]
            if cell == 'K':
                king_pos = (i, j)
                king_count += 1

    if king_count != 1:
        print("Error")
        return False

    king_i, king_j = king_pos
    directions = {
        'straight': [(0, 1), (0, -1),(1, 0), (-1, 0)], 
        'diagonal': [(-1, -1), (-1, 1), (1, -1), (1, 1)], 
        'pawn': [(1, -1), (1, 1)] 
    }

    for dr, dc in directions['straight']: 
        nr, nc = king_i + dr, king_j + dc
        while 0 <= nr < size and 0 <= nc < size:
            piece = lines[nr][nc] 
            if piece in pieces_type: 
                if piece == 'R': 
                    print("Success")
                    return True
                break 
            nr += dr 
            nc += dc

    for dr, dc in directions['diagonal']: 
        nr, nc = king_i + dr, king_j + dc
        while 0 <= nr < size and 0 <= nc < size:
            piece = lines[nr][nc]
            if piece in pieces_type:
                if piece == 'B': 
                    print("Success")
                    return True
                break 
            nr += dr
            nc += dc

    for dr, dc in directions['pawn']: 
        nr, nc = king_i + dr, king_j + dc
        if 0 <= nr < size and 0 <= nc < size:
            piece = lines[nr][nc]
            if piece == 'P': 
                print("Success")
                return True

    for dr, dc in directions['straight'] + directions['diagonal']: 
        nr, nc = king_i + dr, king_j + dc
        while 0 <= nr < size and 0 <= nc < size:
            piece = lines[nr][nc]
            if piece in pieces_type:
                if piece == 'Q': 
                    print("Success")
                    return True
                break 
            nr += dr
            nc += dc

    print("Fail")
    return False
