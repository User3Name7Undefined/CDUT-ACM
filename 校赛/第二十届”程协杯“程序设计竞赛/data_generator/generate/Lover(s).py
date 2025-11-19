from cyaron import *

def generate(io, data_id):
    id= data_id
    T = min(100, int(10**(id/10+uniform(0.4,0.5))))
    X = min(100, int(10**(id/2+uniform(0,0.5))))

    io.input_writeln(T)
    for _ in range(T):
        n=randint(2, X)
        m=randint(2, X)
        io.input_writeln(n, m)
        for _ in range(n):
            io.input_write(randint(1,m))
        io.input_writeln()
        for _ in range(m):
            io.input_write(randint(1,n))
        io.input_writeln()