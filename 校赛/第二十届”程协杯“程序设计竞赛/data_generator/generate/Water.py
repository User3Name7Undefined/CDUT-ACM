from cyaron import *

def generate(io, data_id):
    id = data_id

    T = min(100, randint(id*3,id*6))
    io.input_writeln(T)

    for _ in range(T):
        n=min( 20 , randint(id,id*3) )
        m=min( 20 , randint(id,id*3) )
        io.input_writeln( n, m )

        k = randint(min(n,m),3*min(n,m))
        k = min(n*m-min(n,m),k)
        io.input_writeln( k )

        xys = []
        for _ in range(k):
            x = randint(0, n-1)
            y = randint(0, m-1)
            while (x,y) in xys:
                x = randint(0, n-1)
                y = randint(0, m-1)
            io.input_writeln( x, y )
            xys.append((x, y))