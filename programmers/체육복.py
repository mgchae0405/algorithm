def solution(n, lost, reserve):
    remove_lst = []

    for i in lost:
        if i in reserve:
            remove_lst.append(i)
            reserve.remove(i)

    for j in remove_lst:
        lost.remove(j)

    remove_lst = []

    for i in lost:
        if i - 1 in reserve:
            remove_lst.append(i)
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            remove_lst.append(i)
            reserve.remove(i + 1)

    for j in remove_lst:
        lost.remove(j)

    return n - len(lost)