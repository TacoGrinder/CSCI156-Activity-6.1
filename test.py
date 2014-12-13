__author__ = 'Sean'


def formatname(m):
    position=""
    for i in range(len(m)):
        if m[i] == m[0]:
            x = m[i].upper()
        else:
            x = m[i]
        position += x
    return position


def test():
    i = 1
    while i != 0:
        s = input("Prompt")
        if s == ("sean"):
            s = formatname(s)
            print(s)
            exit()
        #print(s)


test()

