def try_me():
    last_num = 0
    fibonacci = [1, 1]
    for i in range(10):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    fibofunc = lambda x : f'{x} nacho' if x == 1 else f'{x} nachos'
    return [fibofunc(x) for x in fibonacci]
