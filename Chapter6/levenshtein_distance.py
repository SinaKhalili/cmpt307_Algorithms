def edit_distance(v, w):
    v = [*[0], *v]
    w = [*[0], *w]

    table = [[] for i in range(len(v))]
    for i in range(len(table)):
        table[i] = [float('inf') for i in range(len(w))]
    for i in range(len(v)):
        table[i][0] = i
    for i in range(len(w)):
        table[0][i] = i

    for i in range(1,len(table)):
        for j in range(1,len(table[0])):
            if( v[i] == w[j]):
                table[i][j] = table[i-1][j-1] 
            else:
                table[i][j] = min(
                                table[i-1][j] + 1,
                                table[i][j-1] + 1,
                                table[i-1][j-1] + weight_sub(v[i],w[j])
                                )
    return table[len(v)-1][len(w)-1]
                
def weight_sub(a,b):
    return 2

def pprint(matrix, v, w):
    # Function to pretty print these 2d matrices
    print('_ | ', end='')
    for i in range(len(v)):
        print(v[i], end=' ')
    print('')
    for j in range(len(w)):
        print(w[j],'|',  end=' ')
        for i in range(len(v)):
            print(matrix[i][j], end=' ')
        print('')
