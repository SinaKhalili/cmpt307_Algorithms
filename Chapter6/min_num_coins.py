''' Calculate fewest amount of coins given some denominations array 'coins' needed to get to some value'''

def min_num_coins_memo(M, coins, L=None):
    # Here is the memoized recursive solution
    # Pros : Calculates only the needed answers
    # Cons : Can reach max recursion depth quickly
    if(M < 0):
        return 1
    if L is None:
        L = {}
        L[0] = 1
    if M in L:
        return L[M]

    possible_answers = []
    for coin in coins:
        possible_answers.append(min_num_coins_memo(M-coin, coins, L))
    L[M] = min(possible_answers) + 1

    return L[M]

def min_num_coins(M, coins):
    # Here is the normal dynamic programming solution
    # Pros: Can handle very large inputs
    # Cons: Calculates a few redundant answers

    L = [float('inf') for i in range(M + 1)]
    P = [0 for i in range(M + 1)]
    P2 = [0 for i in range(M + 1)]
    L[0] = 0


    for i in range(1,M + 1):
        for j in range(len(coins)):
            if(coins[j] <= i):
                if( L[i]  > 1 + L[i - coins[j]]):
                    L[i] = 1 + L[i - coins[j]]
                    P[i] = j
                    P2[i] = i - coins[j]

    # Don't need P2, could just follow the coin vals
    # TODO ^
    c_needed = [0 for i in range(len(coins))]
    i = M
    while(P2[i] != 0):
        c_needed[P[i]] += 1
        i = P2[i]
    c_needed[P[i]] += 1
    
    print('---------')
    for i in range(len(coins)):
        print(' %s coins of %s value needed ' % (c_needed[i], coins[i]))
    print('---------')
    
    return L[-1]

