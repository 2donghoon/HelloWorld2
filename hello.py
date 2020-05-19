print("1.더하기\n2.빼기\n3.곱하기\n4.나누기\n5.다시 입력하기\n6.종료")

while True:
    start = int(input("원하는 계산기 기능을 입력하세요. "))
    if(start <= 4):
        numberA = int(input("첫번째 숫자를 입력하세요. "))
        numberB = int(input("두번째 숫자를 입력하세요. "))
        if(start == 1):
            print("결과는 %d 입니다."%(numberA+numberB))
        elif(start == 2):
            print("결과는 %d 입니다."%(numberA-numberB))
        elif(start == 3):
            print("결과는 %d 입니다."%(numberA*numberB))
        elif(start == 4):
            print("결과는 %d 입니다."%(numberA/numberB))
    elif(start == 5):
        print("다시 입력하세요.")
    elif(start == 6):
        break