class Table(object):
    def __init__(self, size):
        self.width = size
        self.heigth = size
        self.state = [[None for j in range(size)] for i in range(size)]

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
    result = 0

    return result

if __name__ == '__main__':
    t = Table(3)
    players = [Player('P1', 'x'), Player('P2', 'o')]
    turn = 0
    while True:
        x = int(input('X: '))
        y = int(input('Y: '))
        t.play(x,y,players[turn].sym)
        result = judge(t)
        if result > 0:
            break
        print(t)
        print("-----------------------------")
        turn = 1 if turn == 0 else 0

    if result == 1: #WIN
        print("{} WINS!".format(players[turn].name))
    elif result == 2: #DRAW
        print("DRAW")
