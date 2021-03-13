def move_disc(_from, _to):
    print(f'{_from} to {_to}')

def hanoi(_n, _from, _to, _via):
    if _n == 0:
        pass
    else:
        hanoi(_n - 1, _from, _via, _to)
        move_disc(_from, _to)
        hanoi(_n - 1, _via, _to, _from)

def main(argv):
    hanoi(int(argv[1]), 'A', 'C', 'B')

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

main(['a', '3'])
