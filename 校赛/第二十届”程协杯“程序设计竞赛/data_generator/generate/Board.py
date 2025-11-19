from cyaron import *

def generate(io, data_id):
    id = data_id

    X=min( 10**8, int(10**(id/2)) )
    T=id*5

    io.input_writeln(T)

    for _ in range(T):
        n=randint(1,T)
        m=randint(1,T)
        x=randint(1,int(sqrt(X)))

        io.input_writeln(n,m,x)
        for _ in range(n):
            for __ in range(m):
                io.input_write(randint(0,x))
            io.input_writeln()