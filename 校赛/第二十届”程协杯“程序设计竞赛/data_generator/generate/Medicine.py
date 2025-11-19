from cyaron import *

def generate(io, data_id):
    id= data_id
    limit = min(10**9, int( 10**(id/2+uniform(0,1)) ))
    T = min(10**5, limit)
    io.input_writeln(T)
    for _ in range(T):
        x = randint(1, limit)
        if x % 100 == 1:
            io.input_writeln(1)
        else :
            io.input_writeln(x)
