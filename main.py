import pgzero

HEIGHT = 600
WIDTH = 1000

TITLE = "Skibidi Toilet Simulator"
FPS = 60


pane = Actor("pane", (WIDTH / 2, 450))
ciccio = Actor("cicciogamer", (800,  450))
bullets = []

vel = 5
punti = 0

def draw():
    screen.fill((0, 0, 0))
    
    screen.draw.text("Due fette di cazzo", center=(WIDTH / 2, 100), fontsize=50, color="White")
    screen.draw.text("Ciccio incultato X " + str(punti), center=(WIDTH / 2 + 300, 100), fontsize=30, color="White")
    pane.draw()
    ciccio.draw()
    for i in range(len(bullets)):
        bullets[i].draw()
    
def update(dt):
    
    global punti
    if keyboard.left:
        pane.x -= vel
    elif keyboard.right:
        pane.x += vel
        
    for i in reversed(range(len(bullets))):
        
        if ciccio.colliderect(bullets[i]):
            punti += 1
            bullets.pop(i)  
            continue
        
        if bullets[i].x < 1050:
            bullets[i].x += bullets[i].vel
        else:
            bullets.pop(i)

    
def on_key_down(key):

    if keyboard.SPACE:
        pane.y = 200
        animate(pane, tween = "bounce_end", duration=2, y = 450)
    elif keyboard.up:
        panino1 = Actor("panino")
        panino2 = Actor("panino")
        panino1.x = pane.x
        panino2.x = pane.x
        panino1.y = 300
        panino2.y = 450
        panino1.vel = 5
        panino2.vel = 5
        
        bullets.append(panino1)
        bullets.append(panino2)

        
        