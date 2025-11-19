from cyaron import *

def generate(io, data_id):
    id= data_id
    T = min( 10**5, int( 10**(id/2+uniform(0,1))))
    X = min(10**4, T+5)

    io.input_writeln(T)
    for _ in range(T):
        x1=randint(-X,X)
        y1=randint(-X,X)
        x2=randint(-X,X)
        y2=randint(-X,X)
        while x1==x2 and y1==y2:    #保证不退化成点
            x1=randint(-X,X)
            y1=randint(-X,X)
            x2=randint(-X,X)
            y2=randint(-X,X)
        if x1>x2:   #保证(x1,y1)为左端点
            x1,x2=x2,x1

        xl=randint(-X,X)
        yl=randint(-X,X)
        xr=randint(-X,X)
        yr=randint(-X,X)
        while xl==xr or yl==yr:    #保证不退化成点/线段
            xl=randint(-X,X)
            yl=randint(-X,X)
            xr=randint(-X,X)
            yr=randint(-X,X)
        if xl>xr:   #保证xl<=xr
            xl,xr=xr,xl
        if yl>yr:   #保证yl<=yr
            yl,yr=yr,yl
        
        io.input_writeln(x1,y1,x2,y2)
        io.input_writeln(xl,yl,xr,yr)
