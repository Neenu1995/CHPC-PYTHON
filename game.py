###Python Game
#   Game ends when any player dies.

from random import randint
import sys
class environment:
    def __init__(self):

        self.matrix = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

user = []
opponent = []

class player():

    def __init__(self,x1,y1,i):
        self.x = x1
        self.y = y1
        self.life = 5
        self.name = i
        self.status = 1

    def move(self):
        print 'Input direction(u,d,r,l) for player ',self.name,' : '
        direction = raw_input()
        if direction == 'u':
            if self.x>0 :
                e.matrix[self.x][self.y] = 0
                self.x = self.x-1
                e.matrix[self.x][self.y] = 1
            else:
                print 'Cannot move in that direction!!'
        elif direction == 'd':
            if self.x<7 :
                e.matrix[self.x][self.y] = 0
                self.x = self.x+1
                e.matrix[self.x][self.y] = 1
            else:
                print 'Cannot move in that direction!!'
        elif direction == 'r':
            if self.y<7 :
                e.matrix[self.x][self.y] = 0
                self.y = self.y+1
                e.matrix[self.x][self.y] = 1
            else:
                print 'Cannot move in that direction!!'
        elif direction == 'l':
            if self.y>0 :
                e.matrix[self.x][self.y] = 0
                self.y = self.y-1
                e.matrix[self.x][self.y] = 1
            else:
                print 'Cannot move in that direction!!'
        else:
            print 'Invalid direction!!'

    def life_manage(self,xp,yp):
        if self.life == 0:
            print 'Player died. Game over!! '
            sys.exit()
        else:
            self.move()
            if e.matrix[xp][yp] == 1:
                self.life = self.life-1
                print 'Encountered enemy. ',self.life,' remaining.'

class enemy():
    def __init__(self,x1,y1):
        self.x = x1
        self.y = y1
        self.type = 0
        self.life = 5
        self.status = 1


number = input('How many players do u want?')
i = 0
e = environment()
while i< number:
    print 'Enter x-coordinate of player ',i,' : '
    a1 = input()
    print 'Enter y-coordinate of player ',i,' : '
    b1 = input()
    user.append(player(a1,b1,i))
    e.matrix[a1][b1] = 1
    a2 = randint(0,7)
    b2 = randint(0,7)
    if e.matrix[a2][b2] == 0:
        opponent.append(enemy(a2,b2))
        e.matrix[a2][b2] = 1
    i = i+1
j=0
while j in range(0,7):
    print e.matrix[j]
    j= j +1
user_status = i
while(True):
    for i in user:
        if i.status == 0:
            user_status = user_status-1
    for i in user:
        i.life_manage(i.x,i.y)

    if user_status == 0:
        print 'End game'
        sys.exit()
