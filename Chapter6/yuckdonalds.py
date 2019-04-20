''' Program for the yuckdonald's question '''

def yuck_binsearch(distances, optimal,i, m):
    if( len(distances) == 1 or distances[i] == optimal ):
        return m
    if (distances[i] < optimal):
        return yuck_binsearch(distances[i:m-1], optimal,(i//2), m)
    if (distances[i] >  optimal):
        return yuck_binsearch(distances[0:i-1], optimal,(m-i)//2, m)



def ysearch(distances, k, m):
    return yuck_binsearch(distances, k, m, m-k, 0, len(distances) -1)

def find_best_path(path, k):
    ''' This doesn't do what the question wants '''
    # input array of profits, k-space minimum
    max_profit = [0 for x in range(len(path))]
    for i in range(len(path)):
        add = max_profit[i-k] if i - k > 0 else 0
        max_profit[i] = max(max_profit[i-1], path[i] + add)

    print(max_profit)

    print("The maximum is : ")

    return max_profit.pop()
