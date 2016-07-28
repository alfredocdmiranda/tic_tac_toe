class Table(object):
    def __init__(self, size):
        self.width = size
        self.heigth = size
        self.size = size
        self.state = [[None for j in range(size)] for i in range(size)]

    def full(self):
        for x in self.state:
            for p in x:
                if p is None:
                    return False

        return True

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

    #Vertical
    if result == 0:
        for i in range(table.size):
            l = []
            for x in table.state:
                l.append(x[i])

            s = set(l)
            if len(s) == 1 and s.pop() is not None:
                result = 1
                break

    #Horizontal
    if result == 0:
        for x in table.state:
            s = set(x)
            if len(s) == 1 and s.pop() is not None:
                result = 1
                break

    #Diagonal 1
    if result == 0:
        l = []
        for i in range(table.size):
            l.append(table.state[i][i])

        s = set(l)
        if len(s) == 1 and s.pop() is not None:
            result = 1

    #Diagonal 2
    if result == 0:
        l = []
        for i in range(table.size):
            l.append(table.state[i][table.size-1-i])

        s = set(l)
        if len(s) == 1 and s.pop() is not None:
            result = 1

    #Draw
    if result == 0:
        if table.full():
            result = 2

    return result

if __name__ == '__main__':
    t = Table(3)
    players = [Player('P1', 'x'), Player('P2', 'o')]
    turn = 0
    while True:
        x = int(input('X: '))
        y = int(input('Y: '))
        if not t.play(x,y,players[turn].sym):
            #Invalid
            continue
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
