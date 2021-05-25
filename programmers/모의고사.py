def solution(answers):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            cnt1 += 1
        if answers[i] == two[i % len(two)]:
            cnt2 += 1
        if answers[i] == three[i % len(three)]:
            cnt3 += 1

    ret = []
    lst = [cnt1, cnt2, cnt3]
    for i in range(len(lst)):
        if lst[i] == max(cnt1, cnt2, cnt3):
            ret.append(i + 1)
    return sorted(ret)