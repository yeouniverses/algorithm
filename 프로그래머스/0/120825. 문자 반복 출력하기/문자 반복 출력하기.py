def solution(my_string, n):

    answer = ''
    
    for ms in my_string:
        answer += ms * n
        
    return answer