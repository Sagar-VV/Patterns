# This was the required output, Please find the code below for the same.
#           1 
#         2 2 
#       3 3 3 
#     4 4 4 4 
#   5 5 5 5 5 

def numpat(n):

    for i in range(n,0,-1):
        for y in range(i - 1, -1, -1):
            print(' ', end=' ')
        for z in range (n-i+1):
            print(n-i+1, end=' ')

        print('')    

numpat(5)
