# 재사용을 위한 함수 생성
def copyright(func):
    def new_func():
        print("copyright ajslkfjlqwkejrlkwjelkjfslkj")  # copyright 출력 후
        func()  # 매개변수로 입력받은 함수 실행

    return new_func


# 방법2) decorator 사용하여 재정의 -> 훨씬 간단하고 간편함
@copyright
def smile():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("🌝")


@copyright
def angry():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("🤬")


@copyright
def love():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("😍")


@copyright
def sad():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("😥")


@copyright
def dizzy():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("😵")


@copyright
def sick():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("🤒")


@copyright
def huggingface():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("🤗")


@copyright
def fancy():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("😎")


@copyright
def sleepy():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("😴")


@copyright
def hungry():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("🤤")


@copyright
def drunken():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("🥴")


@copyright
def hbd():
    # print("copyright ajslkfjlqwkejrlkwjelkjfslkj")
    print("🥳")


# 방법1) 함수 재정의 후 함수 재할당 -> 번거로움
# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)
# sad = copyright(sad)
# dizzy = copyright(dizzy)
# sick = copyright(sick)
# huggingface = copyright(huggingface)
# fancy = copyright(fancy)
# sleepy = copyright(sleepy)
# hungry = copyright(hungry)
# drunken = copyright(drunken)
# hbd = copyright(hbd)

smile()
angry()
love()
sad()
dizzy()
sick()
huggingface()
fancy()
sleepy()
hungry()
drunken()
hbd()
