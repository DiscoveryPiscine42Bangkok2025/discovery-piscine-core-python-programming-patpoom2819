#!/usr/bin/env python3

def checkmate(board):

    # ===== ส่วนที่ 1: เตรียมข้อมูลกระดาน =====
    lines = [line for line in board.strip().split('\n') if line.strip()]
    if not lines:
        return False 

    # ===== ส่วนที่ 2: ตรวจสอบว่ากระดานเป็นรูปสี่เหลี่ยมจัตุรัส =====
    size = len(lines)
    for row in lines:
        if len(row) != size:
            print("Error")
            return False   
    
     # ===== ส่วนที่ 3: ค้นหาตำแหน่ง King และตรวจสอบจำนวน =====
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

    # ===== ส่วนที่ 4: ตรวจสอบการรุก (Threat Detection) =====
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

    # ===== สรุปผล: ถ้าตรวจครบทุกทิศแล้วไม่เจอการรุกเลย =====
    print("Fail")
    return False
