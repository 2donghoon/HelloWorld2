print("1.더하기\n2.빼기\n3.곱하기\n4.나누기")

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    menu = int(input("원하는 계산기 기능을 입력하세요."))
    if(menu <= 4):
        numberA = int(input("첫 번째 숫자를 입력하세요."))
        numberB = int(input("두 번째 숫자를 입력하세요."))
        if(menu == 1):
            result = sum(numberA, numberB)
            print("결과는 %d입니다."%result)
            file = open("계산기.txt", 'w')
            file.write("%d")
            file.close()
        elif(menu == 2):
            result = sub(numberA, numberB)
            print("결과는 %d입니다."%result)
            file = open("계산기.txt", 'a')
            file.write("%d")
            file.close()
        elif(menu == 3):
            result = mul(numberA, numberB)
            print("결과는 %d입니다."%result)
            file = open("계산기.txt", 'a')
            file.write("%d")
            file.close()
        elif(menu == 4):
            result = div(numberA, numberB)
            print("결과는 %d입니다."%result)
            file = open("계산기.txt", 'a')
            file.write("%d")
            file.close()
    elif(menu == 5):
        break
    else:
        print("다시 입력하세요.")



