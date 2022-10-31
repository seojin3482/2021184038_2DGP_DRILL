class Player:
    name='Player'


    def __init__(my):
        my.x=100

    def where(my):
        print(my.x)

# self 는 객체 생성용일 뿐 어떠한 것도 가능하다. self 는 객체 자기자신일 뿐이다.

player=Player()
player.where()


print(Player.name)
print(player.name) #위와 결과가 동일 클래스 변수는 다 가지고 있음.

Player.where(player)