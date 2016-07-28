class Table(object):
    def __init__(self, width, heigth):
        self.state = [[None for j in range(width)] for i in range(heigth)]

    def play(self, x, y, sym):
        if self.state[x][y] is None:
            self.state[x][y] = sym
            return True

        return False

    def __repr__(self):
        s = ''
        for m,i in enumerate(self.state):
            for n,j in enumerate(i):
                if j is None:
                    s += " "
                else:
                    s += j

                if n+1 < len(i):
                    s += "|"
            s += '\n'
            if m+1 < len(self.state):
                s += ("-"*len(i)*2)
                s += '\n'

        return s

class Player(object):
    def __init__(self, name, sym):
        self.name = name
        self.sym = sym

def judge(table):
    pass

if __name__ == '__main__':
    t = Table(3,3)
    players = [Player('P1', 'x'), Player('P2', 'o')]
    turn = 0
    while not judge(t):
        x = int(input('X: '))
        y = int(input('Y: '))
        t.play(x,y,players[turn])
        
