def lcs(v, w):
    table = [[] for i in range(len(v))]
    for i in range(len(table)):
        table[i] = ['0' for i in range(len(w))]

    for i in range(len(table)):
        for j in range(len(table[0])):
            if v[i] == w[j]:
                table[i][j] = '1'
    pprint(table, v, w)
    
    score = {}
    for i in range(len(table)):
        # Initialize the score table
        for j in range(len(table[0])):
                    score[str(i-1)+','+str(j)] = 0
                    score[str(i)+','+str(j-1)] = 0
                    score[str(i-1)+','+str(j-1)] = 0
    
    # TODO : Change score table, I just used a hash table because I was being lazy
    for i in range(len(table)):
        for j in range(len(table[0])):
            score[str(i)+','+str(j)] = max(score[str(i-1)+','+str(j)],
                                           score[str(i)+','+str(j-1)],
                                           score[str(i-1)+','+str(j-1)] + 1 
                                                            if table[i][j] == '1' 
                                                            else score[str(i-1)+','+str(j-1)]) 
    
    print('Longest common subsequence length : %s' % 
            score[str(len(v)-1) + ',' + str(len(w)-1) ])


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
