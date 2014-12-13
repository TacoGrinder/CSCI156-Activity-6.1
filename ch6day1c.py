__author__ = 'Sean'

def corners(m, n):
    x = (("+"+"-"*n)*m+"+"+"\n")
    #print(x)
    return x

def vertical(m, n):
    x = (("|"+" "*n)*m+"|"+"\n")
    #print(x)
    return x

def box(m, n, height, width):
    a = (corners(m, n)+vertical(m, n)*height)*width+(corners(m, n))
    print(a)


#corners(3, 5)
#vertical(3, 5)

box(20, 20, 2, 2)