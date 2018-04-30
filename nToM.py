def nToMFunct():
    n = int(input('What number would you like to start at?: '))
    m = int(input('What number would you like to end on?: '))
    print('Start from: %d' % (n))
    print('End on: %d' % (m))
    while n <= m:
        print(int(n))
        n = n + 1
    
