move_foward = [5, 10, 15]
move_back = [7, 13, 20]

def applyEvents(position):
    if position in move_foward:
        print(">> Avanço! +3 casas", flush=True)
        position += 3

    elif position in move_back:
        print(">> Recuo! -2 casas", flush=True)
        position -= 2
        if position < 0:
            position = 0

    return position