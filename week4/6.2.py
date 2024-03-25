# 사용자로부터 파일 이름을 입력받고, 확장자를 제외한 부분을 화면에 출력 

# 확장자는 파일 이름의 마지막에 ".확장자" 형태로 주어진다고 가정
# 파일 이름에 "."가 없을 수 있음. 확장자가 없다면, 입력된 팡리 이름 전체를 출력 
# 파일 이름에 "." 두개 이상 있을 수 없음
# 확장자의 글자 수는 정해지지 않음

filename=input("파일 이름을 입력하세요: ")
idx=filename.rfind('.')
if idx<0:
    idx=len(filename)
print(filename[:idx])