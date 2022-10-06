from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('dog.png')

x = 0
frame = 0
while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 85, 0, 85, 65, x, 80)
    update_canvas()
    frame = (frame + 1) % 6 +1
    x +=5
    delay(0.05)
    get_events()

while(x>0):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 85, 65, 85, 65, x, 80)
    update_canvas()
    frame = (frame + 1) % 6 + 1
    x -= 5
    delay(0.05)
    get_events()
