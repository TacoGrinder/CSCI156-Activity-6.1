__author__ = 'Sean'

def corners(m, n):
    x = 0
    for i in range(1, m):
        x += i
    print(("+"+"-"*n)*x+"+")

def vertical(m, n):
    x = 0
    for i in range(1, m):
        x += i
    print(("|"+" "*n)*x+"|")

corners(3, 5)
vertical(3, 5)