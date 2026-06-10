def solution(my_string):
    answer = ''
    
    for ms in my_string:
        if ms.isupper():
            answer += ms.lower()
        else:
            answer += ms.upper()
        
    return answer