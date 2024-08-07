def solution(rank, attendance):
    arr = sorted([(val, idx) for idx, val in enumerate(rank) if attendance[idx]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]