#  5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 D2
for tc in range(1, int(input())+1):
    val = float(input())  # 10진수 소수를 입력받아야하니 float
    ret = [] # 2진수로 변환, 각자리를 문자열로 
    S=['9','9'] # S[0] 앞자리, S[1] 뒤자리 일단, 임의의 수로 넣음
   
    # 소숫점 뒷자리가 0이고 2진수된 길이가 12까지
    while( S[1] != '0' and len(ret)<=12):
        # 2를 곱해서 
        val = val * 2
        # print(val)
        # 소숫점 앞 뒤로 쪼개 분리하기
        S = str(val).split('.')
        # 소숫점 앞 모으기(순서대로 2진수)    
        ret.append(S[0]) # 문자형태로 소숫점 앞 배열에 쌓기
        # 소숫점 뒤 0이 될때까지 다시 반복
        val = float('0.'+S[1])
        # print(len(ret))
    if len(ret) >= 13:
        # 13자리 이상이 필요한 경우에는 ‘overflow’를 출력
        print('#{} overflow'.format(tc))
    else:
        # 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력
        print("#{}".format(tc),''.join(ret))  