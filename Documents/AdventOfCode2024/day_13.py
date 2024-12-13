import numpy as np

f = open('day_13_input.txt','r')
lines = f.readlines()
lines = [ x.strip() for x in lines]

def parsing(var, symbol, scale):
    if symbol == '=':
        return int(var[0].split(symbol)[1])+scale, int(var[1].split(symbol)[1])+scale
    return int(var[0].split(symbol)[1]), int(var[1].split(symbol)[1])

def main(scale):
    tokens = 0
    Ax, Ay, Bx, By, X, Y = 0,0,0,0,0,0
    for line in lines+['']:
        if line == '':
            M = np.array([[Ax, Bx], [Ay, By]])
            C = np.array([X, Y])
            if np.linalg.det(M) != 0:
                solution = np.linalg.solve(M, C)
                a, b = solution
                if abs(a - round(a)) < 1e-3 and abs(b - round(b)) < 1e-3:
                    tokens += round(a)*3+round(b)
            continue
        else:
            data = line.split(':')[1].split(',')
            if 'Prize' in line:
                X, Y = parsing(data, '=', scale)
            if 'A:' in line:
                Ax, Ay = parsing(data, '+', scale)
            if 'B:' in line:
                Bx, By = parsing(data, '+', scale)
    print(tokens)
#-----------part 1--------------------------------------
main(0)
#-----------part 2--------------------------------------
main(10000000000000)