ls =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]

i = 0
j = 0
n=len(ls)
for i in range(n):
    for j in range(n):
        if i == 0 or i==n-1 or j == 0 or j==n-1:
            value = ls[i][j]
            print(i, j, value)


#0 0 1
#0 1 2
#0 2 3
#0 3 4
#1 0 5

#2 3 12
#3 0 13
#3 1 14
#3 2 15
#3 3 16

#----
#1 1 6
#1 2 7
#2 1 10
#2 2 11

