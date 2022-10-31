from pico2d import *

RD, LD, RU, LU,TIMER,A = range(6)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN,SDLK_a):A
    }



class Boy:
    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
    def update(self):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)
    def draw(self):
        self.cur_state.draw(self)
    def add_event(self, event):
        self.event_que.insert(0, event)
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        self.dir=0
        self.timer=1000
    @staticmethod
    def exit(self):
        print('EXIT IDLE')
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer-=1
        if self.timer==0:
            self.add_event(TIMER)
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

class RUN:
    def enter(self, event):

        print('ENTER RUN')
#어떤 이벤트 떄문에 어떤 상태에 돌아왔는지
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self):
        print('EXIT RUN')
        #현 상태를 나갈 때, 현재 방향을 저장해놓음.

        self.face_dir = self.dir

    def do(self):
        # 달리게 만들어준다.
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x=clamp(0,self.x,800)

    def draw(self):
        print('DRAW RUN')

        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0
    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        print('DRAW SLEEP')

        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)


class AUTO_RUN:
    def enter(self, event):

        print('ENTER AUTO_RUN')
        # 어떤 이벤트 떄문에 어떤 상태에 돌아왔는지
        self.dir=1

    def exit(self):
        print('EXIT AUTO_RUN')
        # 현 상태를 나갈 때, 현재 방향을 저장해놓음.



    def do(self):
        # 달리게 만들어준다.
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x==800:
            self.dir=-1
        elif self.x==0:
            self.dir=1



    def draw(self):
        print('DRAW AUTO_RUN')

        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y+30,200,200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y+30,200,200)
    pass



next_state = {
    SLEEP:{RU:RUN,LU:RUN,RD:RUN,LD:RUN,TIMER:SLEEP},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN,TIMER:SLEEP,A:AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE,TIMER:RUN,A:AUTO_RUN},
    AUTO_RUN:{A:IDLE,RU:RUN,LU:RUN}

}

