import pygame as pg

print('Setup Start')
pg.init()
window = pg.display.set_mode(size=(640, 480))
print('Setup Finish')

print('Loop Start')
while True:
    # check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() # close window
            quit() # end pygame

