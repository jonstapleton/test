alien = Actor('alien')
alien2 = Actor('alien')
alien.pos = 100, 56
alien2.pos = 400, 400

WIDTH = 800
HEIGHT = 600



def update():
    
    if keyboard.a == True:
        alien.right -= 2
    if keyboard.d == True:
        alien.right += 2

    if keyboard.w == True:
        alien.top -= 2
    if keyboard.s == True:
        alien.top += 2

    # x coordinate collision
    if alien.left < alien2.left and alien.right > alien2.left or alien2.left < alien.left and alien2.right > alien.left:
        if alien.top < alien2.top and alien.bottom > alien2.top or alien2.top < alien.top and alien2.bottom > alien.top:
            print("Colliding!")

def draw():
    screen.clear()
    alien.draw()
    alien2.draw()