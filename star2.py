#      *
#     **
#    ***
#   ****
#  *****

n = 5

for i in range (n, 0, -1):
    for s in range(i):
        print(' ', end='')

    for t in range (n-i+1):
        print('*', end='')

    print('')        

