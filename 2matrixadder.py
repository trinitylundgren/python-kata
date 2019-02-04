def add(a,b):
    if len(a) != len(b):
        return None
    for x in range(len(a)):
        if len(a[x]) != len(a[0]):
            return None
    for x in range(len(b)):
        if len(b[x]) != len(b[0]):
            return None
    if len(a[0]) != len(b[0]):
        return None
    c = [[0] * len(a[0]) for _ in range(len(a))]
    for x in range(len(a)):
        for y in range(len(a[0])):
            c[x][y] = a[x][y] + b[x][y]
    return c

a = [[3,5,6], [2,3,7]]
b = [[6,6,3], [3,3,8]]

print(add(a,b))

a = [0]
b = [[0,0], [0,6]]

print(add(a,b))

a = [['a','b'],['c','d']]
b = [['e','f'],['g','h']]
        
print(add(a,b))            

a = 'foo'
b = 'bar'

print(add(a,b))
