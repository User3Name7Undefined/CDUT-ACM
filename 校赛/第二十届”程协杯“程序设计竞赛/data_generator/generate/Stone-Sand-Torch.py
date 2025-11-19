from cyaron import *

def generate(io, data_id):
    id=data_id

    X = min(10, id+randint(1,3))
    Y = min(10, id+randint(1,3))
    Z = min(10, id+randint(1,3))
    
    io.input_writeln(X, Y, Z)

    n = min( 10**5, int(10**(id/2+uniform(0,1))) )
    io.input_writeln(n)

    for _ in range(n):
        commands = ('PUT_STONE', 'PUT_SAND', 'PUT_TORCH', 'DESTROY')
        x = randint(0, X - 1)
        y = randint(0, Y - 1)
        z = randint(0, Z - 1)
        f = randint(1, 5)

        chosen_command = choice(commands)
        if chosen_command == 'PUT_TORCH':
            io.input_writeln(chosen_command, x, y, z, f)
        else:
            io.input_writeln(chosen_command, x, y, z)
