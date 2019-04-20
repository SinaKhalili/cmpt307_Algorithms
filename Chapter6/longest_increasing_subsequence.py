''' Calculate the longest increasing subsequence ''' 

def longest_increasing_subsequence(array):
    # Input array sequence
    # Outpout length of longest increasing sequence
    L = [0 for i in range(len(array))]
    P = [0 for i in range(len(array))]

    for i in range(len(array)):
        for j in range(i):
            if (array[j] < array[i]):
                if( L[i] < 1 + L[j]):
                    L[i] = 1 + L[j]
                    P[i] = j


    increasing_subsequence = []
    max_num = max(L)
    i = L.index(max_num)
    while(P[i] != 0):
        increasing_subsequence.append(array[i])
        i = P[i]
    increasing_subsequence.append(array[i])

    print(increasing_subsequence[::-1])
    return max(L) + 1

