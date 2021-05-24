def solution(board, moves):

    cnt = 0
    lst = []

    for k in moves:
        for j in range(len(board)):
            if board[j][k-1]:
                lst.append(board[j][k-1])
                board[j][k - 1] = 0
                break


        if len(lst)>1:
            if lst[-1] == lst[-2]:
                lst = lst[:-2]
                cnt += 2
    return cnt