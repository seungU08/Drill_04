from pico2d import*

TUK_WIDTH , TUK_HEIGHT = 1280 , 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image("TUK_GROUND.png")
character = load_image('character_sheet.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False



running = True
x , y = TUK_WIDTH//2 , TUK_HEIGHT//2
frame = 0
i = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2 , TUK_HEIGHT//2)
    character.clip_draw(frame*200 , 275*i , 200,275,x,y)
    update_canvas()

    handle_events()

    frame = (frame + 1)%4
    delay(0.05)

close_canvas()

