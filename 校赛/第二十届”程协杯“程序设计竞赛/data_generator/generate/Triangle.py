from cyaron import *

def generate_interval(n):
    x=randint(0,n)
    l=randint(1,n)
    r=randint(1,n)

    if x==0:
        return (l,l)
    else :
        return (min(l,r), max(l,r))

def generate(io, data_id):
    id= data_id
    X = min( 10**9, int( 10**(id/2+uniform(0,0.5))))
    T = min( 10**5, int( 10**(id/2+uniform(0,0.5))))

    n=randint(T//4,T//2)
    n=max(n,6)
    q=randint(T//2,T)

    io.input_writeln(n, q)
    for _ in range(n):
        io.input_write(randint(1,X))
    io.input_writeln()
    for _ in range(q):
        l,r=generate_interval(n)
        while r-l+1<6 :
            l,r=generate_interval(n)
        io.input_writeln(l,r)