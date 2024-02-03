import timeit


coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
            if amount == 0:
                break
    return result

print('Жадібний алгоритм: ', find_coins_greedy(113))



def find_min_coins(amount):
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    if min_coins[amount] == float('inf'):
        return {}

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        amount -= coin
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1

    return result

print('Динамічний алгоритм(нижній підхід): ',find_min_coins(113))


greedy_time = timeit.timeit('find_coins_greedy(113)', globals=globals(), number=1000)
dynamic_time = timeit.timeit('find_min_coins(113)', globals=globals(), number=1000)

print(f'Час виконання жадібного алгоритму (1000 ітерацій): {greedy_time:.6f} секунд')
print(f'Час виконання динамічного алгоритму (1000 ітерацій): {dynamic_time:.6f} секунд')