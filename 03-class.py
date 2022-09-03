# ============================ Class 생성 ======================================
# class는 반복되며 하나의 집단에서 '행위'와 '상태(속성)'를 나눌 수 있다고 판단될 때 사용!
class Cal:

    # [생성자] : class가 instance화되어 메모리에 올라오는 순간 즉시 실행되는 함수
    # [self] : class로 생성된 instance -> 가장 먼저 생성자에 매개변수로 넣어줌!
    def __init__(self, a, b):
        # instance 안의 namespace에서 변수 a를 외부에서 받아온 a로 정의함!
        self.a = a
        # instance 안의 namespace에서 변수 b를 외부에서 받아온 b로 정의함!
        self.b = b

    # [INSTANCE METHOD]
    # instnace method들은 필수적으로 맨 앞에 인자(self)가 필요하고, 그 인자는 instance를 가리킴
    # 함수마다 'self'를 넣어줌으로써 instance안의 namespace에서 접근(.)할 수 있도록 만들어줌!
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


# ======================== Class의 Instance화 ==================================
# 인자를 넘겨준 순간 메모리에 올라감 : 생성자 (__init__) 호출
# 1) self가 cal1을 가리키게 됨
# 2) a가 1을 가리키게 됨
# 3) b가 2를 가리키게 됨
cal1 = Cal(1, 2)
# => 인스턴스 cal1에는 namespace가 생겼는데 그 공간 안에는 a, b, add, sub, mul, div가 존재하게 됨!
print(cal1.a)  # 1
print(cal1.b)  # 2
print(cal1.add())  # 3

cal2 = Cal(3, 4)
print(cal2.a)  # 3
print(cal2.b)  # 4

# ==================== instance 변수를 외부에서 수정 ==================================
cal1.a = 7

print(cal1.a)  # 7
print(cal1.b)  # 2
print(cal1.add())  # 9

# ======================= 기존 함수 정의 및 호출 방식 ===================================
# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     return a / b

# print(add(1, 2))
# print(sub(1, 2))
# print(mul(1, 2))
