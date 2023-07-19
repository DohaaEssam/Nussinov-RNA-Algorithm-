import numpy as np

x=input("Please Enter The Sequence")
r=len(x)
def pairing(i,j):
    if (x[i] == 'A' and x[j] == 'U') or (x[i] == 'U' and x[j] == 'A') or (x[i] == 'C' and x[j] == 'G') or (x[i] == 'G' and x[j] == 'C') or (x[i] == 'G' and x[j] == 'U')or (x[i] == 'U' and x[j] == 'G'):
        return True
    else:
        return False
def initialization(x):
    matrix = [[np.NAN for x in range(r)] for x in range(r)]
    matrix = np.array(matrix).reshape(r, r)
    for i in range(0, len(matrix)):
        # main diagonal
        matrix[i][i] = 0
    for i in range(1, len(matrix)):
        # lower diagonal
        matrix[i][i - 1] = 0
    # print(matrix)
    for col in range(1, r):
        for i in range(r - col):
            j = i + col
            if j - i >= 1:
                if x[i] == 'A' and x[j] == 'U':
                    score = 1
                elif x[i] == 'U' and x[j] == 'A':
                    score = 1
                elif x[i] == 'C' and x[j] == 'G':
                    score = 1
                elif x[i] == 'G' and x[j] == 'C':
                    score = 1
                elif x[i] == 'G' and x[j] == 'U':
                    score = 1
                elif x[i] == 'U' and x[j] == 'G':
                    score = 1
                else:
                    score = 0
                burification=0
                for t in range(i+1, j):
                    if burification <matrix[i][t] + matrix[t + 1][j]:
                       burification =matrix[i][t] + matrix[t + 1][j]
                if j - i >= 0:
                    matrix[i][j] = max(matrix[i + 1][j], matrix[i][j - 1], matrix[i + 1][j - 1] + score, burification)  # max of all
    print(matrix)
    return matrix

def TraceBack(i,j,Matrix,RNA):
    while j!=i and i<len(x)+1 and j>0:
        if Matrix[i][j] == Matrix[i + 1][j - 1]+1 and pairing(i,j)==True:
            if j > i:
                RNA[i] = '('
                RNA[j] = ')'
            else:
                RNA[i] = ')'
                RNA[j] = '('
            i = i + 1
            j = j - 1
        elif Matrix[i][j] == Matrix[i][j - 1]:
            j = j - 1
        elif Matrix[i][j] == Matrix[i + 1][j]:
            i = i + 1
        else:
            for k in range(i + 1, j):
                if Matrix[i, k] + Matrix[k + 1][j] == Matrix[i][j]:
                    Test = RNA
                    TraceBack(x,k+1,j,Matrix,RNA)
                    j = k
                    break
    print(RNA)



m=len(x)-1
RNA=[]
Test=[]
for N in range(len(x)):
    RNA.append('.')
matrix=initialization(x)
TraceBack(0,m,matrix,RNA)