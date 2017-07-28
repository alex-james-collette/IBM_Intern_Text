import curses
import random
from time import sleep
dimx = 80
dimy = 24
lives = 2
score = 0

def updateBall(stdscr, ball, paddle):
    global score
    stdscr.addstr(0, curses.COLS // 2 - 20,
        "Lives: " + str(lives + 1) + "  Your Score: " + str(score))
    stdscr.addstr(1, 1,
                  '-' * (dimx - 2))
    stdscr.addstr(22, 1,
        "-" * (dimx - 2))
    for col in range(2, dimy - 2):
        stdscr.addstr(col, dimx - 2,
            '|' )

    stdscr.addstr(ball['y'], ball['x'], ' ')
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']

    if (ball['y'] == 1 or ball['y'] == dimy - 2):
        ball['dy'] = -ball['dy']
    if (ball['x'] == dimx - 3):
        ball['dx'] = -ball['dx']
    if (ball['x'] == 1):
        if (ball['y'] in paddle['y']):
            ball['dx'] = -ball['dx']
            score += 1
    if (ball['x'] == 0):
            ball['inPlay'] = 0
    if (ball['inPlay'] != 0):
        stdscr.addstr(ball['y'], ball['x'], 'O')
    
    return ball


def updatePaddle(stdscr, paddle):
    oldPaddleY = paddle['y'][:]
    global ball
    
    try:
        move = stdscr.getch()
        if (move == ord('j') and paddle['y'][0] < dimy - 2):
            for i in range(len(paddle['y'])):
                paddle['y'][i] += 1
        elif (move == ord('k') and paddle['y'][2] > 1):
            for i in range(len(paddle['y'])):
                paddle['y'][i] -= 1
        else:
            pass    
    except curses.error:
        pass
    
    for i in range(len(oldPaddleY)):
        stdscr.addstr(oldPaddleY[i], paddle['x'], " ")
    
    for i in range(len(paddle['y'])):
        stdscr.addstr(paddle['y'][i], paddle['x'], '#')


def main(stdscr):
    stdscr.clear()
    curses.halfdelay(1)
    curses.curs_set(False) # Turn off the cursor, we won't be needing it.

    ball = {'x':0, 'y':0,                # A dict of attributes about the ball
            'dx':0, 'dy':0,
            'inPlay':0, 'score': 0}
    ball['x'] = dimx // 2         # Ball's initial X position.
    ball['y'] = dimy // 2         # Starts at screen center.
    ball['dx'] = random.choice([-1, 1])  # The ball's slope components
    ball['dy'] = random.choice([-1, 1])
    ball['inPlay'] = 1                   # Status of game
    
    paddle = {'x':0, 'y':[0, 0, 0]}      # a dict of attributes about paddle
    paddle['x'] = 0                      # Starting x and y of the paddle
    paddle['y'] = [dimy // 2 + i for i in (1, 0, -1)]
                                         # lowest to highest, visually
    stdscr.addch(ball['y'], ball['x'], 'O')
    updatePaddle(stdscr, paddle)
    stdscr.refresh()

    while ball['inPlay']:
        ball = updateBall(stdscr, ball, paddle)
        updatePaddle(stdscr, paddle)
        stdscr.refresh() 

    stdscr.clear()
    curses.cbreak(True) 
    curses.flushinp()
    curses.curs_set(True)
    


def pong():
    global lives
    global score
    score = 0
    lives = 2 
    while lives >= 0:
        curses.wrapper(main)
        lives -= 1
    else:
        return score
