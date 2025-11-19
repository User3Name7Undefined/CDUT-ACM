from cyaron import *

def generate(io, data_id):
    id= data_id
    T = min(10**6, int(10**(id/2+uniform(0.5,1))))  #tot n

    if randint(0,1) == 0:
        t=randint(1,int(sqrt(T)))
    else:
        t=randint(int(sqrt(T)),T)
    t=min(t,10**5)  #T

    single = T // t
    single = min(single,10**5)
    io.input_writeln(t)

    for _ in range(t):
        n=randint(max(5,single//2),max(5,single))
        r=randint(1,n)
        io.input_writeln(n,r)

        tree=None
        if id == 15 or id == 17:
            tree = Graph.chain(n,weight_limit=(1,min(T,1000)))
        elif id == 16 or id == 18:
            tree = Graph.flower(n,weight_limit=(1,min(T,1000)))
        else:
            tree = Graph.tree(n,weight_limit=(1,min(T,1000)))
        io.input_writeln(tree)
        
        for _ in range(n):
            if _ == r-1:
                io.input_write(0)
            else:
                io.input_write(randint(1,min(T,1000)))
        io.input_writeln()