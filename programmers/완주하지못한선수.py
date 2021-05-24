from collections import Counter
def solution(participant, completion):
    return [i for i in (Counter(participant) - Counter(completion)).keys()][0]


# 다른풀이
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if completion[i] != participant[i]:
#             return participant[i]
# 
#     return participant[-1]