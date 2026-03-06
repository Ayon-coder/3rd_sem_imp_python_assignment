def add(*args):
    sum = 0
    for i in args:
        if(i > 0):
            sum += i
        else:
            continue
    return sum

print(add(1, 2, -2, 3, 4, -8))