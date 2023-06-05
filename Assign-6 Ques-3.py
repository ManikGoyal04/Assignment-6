def pascal_triangle(n):
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(' '.join(map(str, trow)).center(n*2))
        trow = [l+r for l,r in zip(trow+y, y+trow)]
    return n>=1

pascal_triangle(5)
