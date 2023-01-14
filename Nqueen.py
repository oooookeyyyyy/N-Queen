from copy import deepcopy

def add(l, c) :
        for i in range(table) :
            board[l][i] = board[i][c] = 'O'
        board[l][c] = 'X'
        ln, cl = l, c
        while ln > 0 and cl > 0 :
            board[ln-1][cl-1] = 'O'
            ln -= 1
            cl -= 1
        ln, cl = l, c
        while ln < table - 1 and cl < table - 1 :
            board[ln+1][cl+1] = 'O'
            ln += 1
            cl += 1
        ln, cl = l, c
        while ln > 0 and cl < table - 1 :
            board[ln-1][cl+1] = 'O'
            ln -= 1
            cl += 1
        ln, cl = l, c
        while ln < table - 1 and cl > 0 :
            board[ln+1][cl-1] = 'O'
            ln += 1
            cl -= 1

table = int(input('input Side length >>'))
spots = []
result = []
solution = 0
l, c = 0, 0
board = [['0' for _ in range(table)] for _ in range(table)]
stack = [deepcopy(board)]
while l < table :
    while c < table :
        if '0' not in stack[-1][l][c:] :
            try :
                stack.pop()
                board = deepcopy(stack[-1])
                l -= 1
                c = spots.pop()+1
                if c == table:
                    stack.pop()
                    board = deepcopy(stack[-1])
                    l -= 1
                    c = spots.pop()+1
                break
            except :
                print(f'{solution} optimal state : ')
                input('press enter to show boards')
                for r in result :
                    print('-----'*table)
                    for l in r :
                        print(l)
                        print()
                exit()
        elif stack[-1][l][c] == '0' :
            add(l, c)
            stack.append(deepcopy(board))
            spots.append(c)
            c = 0
            l += 1
            if l == table :
                result.append(stack.pop())
                solution += 1
                board = deepcopy(stack[-1])
                l -= 1
                c = spots.pop()+1
                if c == table :
                    stack.pop()
                    board = deepcopy(stack[-1])
                    l -= 1
                    c = spots.pop()+1
            break
        c += 1
