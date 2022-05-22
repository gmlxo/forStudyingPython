# 자동정렬 Ctrl + alt + i

nInt = [0, 6, -5]
nString = ['o', 'n']

numberEx = 10
numberEx_1 = 20

text = "HELLO WORD!"  # (1)
textEx = "Hello Word!"
textEx_1 = "   Hello Word   "

print("gitHub commit test\n")
#   ** int **

#  사칙연산
print(numberEx_1 // numberEx)  # 소수점 X
print(numberEx_1 / numberEx)  # 소수점 O

# ** Strint **

#  문자열
print('''\ntextEx''' + "\t textEx\n")  # """ """ or ''' ''' 까지 ㄱㄴ

#  문자열 내용 변경
text = text.replace('!', '?')  # '!' 를 '?'로 변경 (1)
textEx = textEx.replace('!', '')  # '!' 를 삭제

#  문자열 찾기
print("textEx의 n번째 자리 : " + textEx[nInt[0]] +  # n 번째 자리 찾기
      "\ntextEx 의 n번째까지 : " + textEx[:nInt[1]] +  # n 번째 자리까지 찾기
      "\ntextEx 의 -n번째부터 : " + textEx[nInt[2]:] + "\n")  # -n 번째 자리부터 찾기

#  문자열 나누기
print(textEx.split())  # 공백이 있을 시 문자열을 나눔
print(textEx.split(nString[0]))  # n 이 있을 시 문자열을 나눔

#  문자열 기타 함수
print("\n" + text.lower())  # 전부 소문자
print(textEx.upper())  # 전부 대분자

print(len(textEx))  # textEx 문자열 길이

print("." + textEx_1.rstrip() + ".")  # 우측 공백 제거
print("." + textEx_1.lstrip() + ".")  # 좌측 공백 제거
print("." + textEx_1.strip() + ".")  # 양쪽 공백 제거
