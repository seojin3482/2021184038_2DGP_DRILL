from pico2d import *


def handle_events():
    global running
    global dir
    global dir2
    global k
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                k=1
            elif event.key == SDLK_LEFT:
                dir -= 1
                k=0
            elif event.key == SDLK_UP:
                dir2 += 1
            elif event.key == SDLK_DOWN:
                dir2 -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir2 -= 1
            elif event.key == SDLK_DOWN:
                dir2 += 1




open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir=0
y=0
dir2=0
k=1

while running:
    clear_canvas()
    grass.draw(400, 90)
    character.clip_draw(frame * 100, 100 * k, 100, 100, x, y)
   
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    y+= dir2*5
    if x<0 or x>800 or y<0 or y>600:
        running=False
    delay(0.01)

close_canvas()

