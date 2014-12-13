__author__ = 'Sean'


def formatname(m):
    p = ""
    o = m.split()
    for i in range(len(o)):
        q = o[i]
        o[i].lstrip()
        for u in range(len(q)):
            if u is 0:
                p +=" " + q[u].upper()
            else:
                p += q[u]
    return p


def firstname():
    a = formatname(input("First Name:"))
    return a


def lastname():
    b = formatname(input("Last Name:"))
    return b


def namewhole():
    c = firstname()
    d = lastname()
    print(c+" "+d)


namewhole()