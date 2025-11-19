from cyaron import *
import random

def generate(io, data_id):
    id = int(data_id)
    T = min(2*10**5, int(10**(id/3+uniform(0.25,0.35))))
    X = min(4*10**6, int(T*20*uniform(0.75,1.33)))

    if randint(0,1) == 0:   
        t=randint(1,int(sqrt(T)))
    else:
        t=randint(int(sqrt(T)),T)
    
    single=X//t

    io.input_writeln(t)
    for _ in range(t):
        a=randint(0,single//4)
        b=min(single//4,max(0,randint(a-2,a+2)))
        c=randint(0,single//4)
        d=randint(0,single//4)
        io.input_writeln(a,b,c,d)