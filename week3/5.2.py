#10 이상, 5 이상 10 미만, 5 미만의 정수를 입력 받을 때 적절한 내용을 화면에 출력
# 입력 받은 숫자가 num 변수에 저장되어 있다고 가정

# 사용자가 오류 없이 정수만을 입력할 것이라고 가정

num=int(input("정수를 입력하세요: "))
if num>=10:
    print("10보다 크거나 같습니다")
else:
    if 5<=num:
        print("5보다 크거나 같지만 10보다 작습니다")
    else: 
        print("5보다 작습니다")