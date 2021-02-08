
def numpat(n):

    for i in range(n,0,-1):
        for y in range(i - 1, -1, -1):
            print(' ', end=' ')
        for z in range (n-i+1):
            print(n-i+1, end=' ')

        print('')    

numpat(5)
