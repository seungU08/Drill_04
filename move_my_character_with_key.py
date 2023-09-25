from pico2d import*

TUK_WIDTH , TUK_HEIGHT = 1280 , 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image("TUK_GROUND.png")
character = load_image('character_sheet.png')

def handle_events():
    global running
    global dir
    global i

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                i = 1
                dir -= 1
            elif event.key == SDLK_RIGHT:
                i = 2
                dir += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_RIGHT:
                dir -= 1





running = True
x , y = TUK_WIDTH//2 , TUK_HEIGHT//2
frame = 0
i = 3
dir = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2 , TUK_HEIGHT//2)
    character.clip_draw(frame*200 , 275*i , 200,275,x,y)
    update_canvas()

    handle_events()

    frame = (frame + 1)%4
    x += dir * 5
    delay(0.05)

close_canvas()

