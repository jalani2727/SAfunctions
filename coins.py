def coinsFunct():
    coins = 0
    print('You have %d coins.' % (coins))
    another = input('Do you want another?: ').lower()
    while another == 'yes':
        coins += 1
        print('You have %d coins.' % (coins))
        if another == 'yes':
            another = input('Do you want another?: ')
        else:
            print('')
    print('Well fuck you then, nigga.')        

"""
#here's a simpler way:
coins = 0 
another = "yes"

while another == "yes":
    print("You have %d coins" % coins)
    another = input("You want another, nigga?:").lower()
    coins = coins + 1

print("Peace, bih.")
"""