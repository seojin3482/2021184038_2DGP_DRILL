class Star:
    name='Star' #클래스 변수
    x=100 #클래스 변수

    def change():
        x=200
        print('x is',x)


print('x is',Star.x) # 클래스 변수 액세스
Star.change() #클래스 함수
# 클래스는 객체를 생성하는 틀이 아닌 변수와 함수를 묶는 역할을 할 때도 있다.

star=Star() #생성자가 없는데 생성이 된다. (객체의 초깃값이 존재하지 않음)
print(type(star))
print(star.x) #비록 객체 변수로 액세스했으나, 같은 이름의 클래스 변수가 우선.


star.change() #Star.change(star)와 동일 -> 실행되지 않음 self 가 존재하지 않는 클래스