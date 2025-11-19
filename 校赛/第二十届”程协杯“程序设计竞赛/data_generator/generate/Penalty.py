from cyaron import *

def generate(io, data_id):
    id = data_id

    T = id*5
    X = min( 1000,int(10**(id/5+0.3)) )

    io.input_writeln(T)

    for _ in range(T):
        n=randint(1,20)
        io.input_writeln(n)
        for _ in range(n):
            io.input_write(randint(1,X))
        io.input_writeln()
