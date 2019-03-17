def simple_summa(a,b):
    c = []
    for i in range(10):
        c.append(a+b)
    return c


def difficult_summa():
    for i in range(10):
        yield i


for i in difficult_summa():
    print(i)

