# import sys
# print(sys.argv)  # 명령 행에서 인수 전달
# sys.exit()  # 강제로 스크립트 종료
# print(sys.path)  # 모듈의 위치
# sys.path.append("E:\\Python\\GRAM")  # 모듈 불러오기

# import os
# print(os.environ)  # 현재 시스템의 환경 변수값
# os.chdir("C:\\Windows")  # 디렉터리 위치 변경
# print(os.getcwd())  # 디렉터리 위치 받기
# os.system("dir")  # 시스템 명령어 호출
# f = os.popen("dir")  # 실행한 명령어의 결괏값 받기
# print(f.read())  # 실행한 명령어의 결괏값 출력
# # 그 외
# # os.mkdir : 디렉터리 생성
# # os.rmdir : 디렉터리 삭제, 비어있어야 삭제 가능
# # os.unlink : 파일을 지운다
# # os.rename(src, dst) : src 라는 이름의 파일을 dst 라는 이름으로 바꿈

# import shutil
# shutil.copy("src.txt", "dst.txt")  # src 라는 이름의 파일을 dst 로 복사

# import glob
# print(glob.glob("c:\\doit\\mark"))  # c:/doit 디렉터리에 있는 파일 중 이름이 mark로 시작하는 파일 모두 찾음

# import tempfile
# filename = tempfile.mktemp()  # 중복되지 않는 임시 파일 이름 반환
# print(filename)
# f = tempfile.TemporaryFile()  # 임시 저장 공간으로 사용할 파일 객체 반환
# f.close()  # 파일객체 삭제

# import time
# print(time.time())  # 1970년 1월 1일 0시 0분 0초를 기준으로 지난시간을 초단위로 반환
# print(time.localtime(time.time()))  # 연도, 월, 일, 시, 분, 초의 형태로 전환
# print(time.asctime(time.localtime(time.time())))  # 날짜와 시간을 알아보기 쉬운 형태로 전환
# print(time.ctime())  # 35줄과 같음, 항상 현재 시간만 돌려줌
# print(time.strftime('출력할 형식 포멧 코드', time.localtime(time.time())))  # 시간에 관계된 것을 세밀하게 표현
# for i in range(10):
#     print(i)
#     time.sleep(1)  # 1초 간격으로 진행

# import calendar
# print(calendar.calendar(2020))  # 그 해의 전체 달력
# print(calendar.prcal(2020))  # 43줄과 같음
# print(calendar.weekday(2020, 8, 20))  # 그 날짜에 해당하는 요일정보 (월:0, 화:1, 수:2...)
# print(calendar.monthrange(2020, 8))  # 입력 받은 달의 1일이 무슨 요일인지, 그 달이 며칠까지인지 튜플로 반환

# import random
# print(random.random())  # 0.0에서 1.0 사이의 실수 중 하나 반환
# print(random.randint(1, 10))  # 1에서 10 사이의 정수 중 하나 반환
# print(random.choice([1, 2, 3]))  # 리스트에서 무작위로 하나를 선택하여 반환
# data = [1, 2, 3, 4, 5]
# print(random.shuffle(data))  # 리스트의 항목을 무작위로 섞음

import webbrowser
webbrowser.open("http://google.com")  # 기본 웹 브라우저로 URL 로 이동
webbrowser.open_new("http://google.com")  # 새로운 창으로 URL 연다
