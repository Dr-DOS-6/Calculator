import readchar
def test():
    while 1:
        kb = readchar.readchar()
        print(kb, end='', flush=True)
        if kb == 'q':
            print("")
            break