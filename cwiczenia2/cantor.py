WIDTH = 81
HEIGHT = 5
lines = []


def cantor(start, len, index):
    seg = int(len / 3)
    if seg == 0:
        return None
    for i in range(HEIGHT - index):
        i = index + i
        for j in range(seg):
            j = start + seg + j
            pos = i * WIDTH + j
            lines[pos] = ''
        cantor(start, seg, index + 1)
        cantor(start + seg * 2, seg, index + 1)
        return None


lines = ['*'] * (WIDTH*HEIGHT)
cantor(0, WIDTH, 1)
for i in range(HEIGHT):
    beg = WIDTH * i
    #print ''.join(lines[beg: beg + WIDTH])
