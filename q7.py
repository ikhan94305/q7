def solution(arr):
    answer = [arr[0]]
    curr = arr[0]
    for i in range(1,len(arr)):
        if arr[i] == curr:
            continue
        else:
            curr = arr[i]
            answer.append(arr[i])
    return answer

arr = [1,1,0,0,2,2,3,3,1,1,0,0,2,0,2,1]
#arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)
