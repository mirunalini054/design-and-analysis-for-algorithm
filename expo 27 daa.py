def coin_change_greedy(coins, amount):
    # Sort in descending order
    coins.sort(reverse=True)
    result = []
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
            
    if amount == 0:
        return result
    return "Greedy approach failed for this coin set"

denom = [1, 2, 5, 10, 20, 50, 100, 500]
amt = 93
print("Coins Used:", coin_change_greedy(denom, amt))
