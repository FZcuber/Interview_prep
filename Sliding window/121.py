def maxProfit(prices):
    if len(prices) < 2:
        return 0

    result = 0

    l = 0

    for i in range(len(prices)):
        if prices[i] < prices[l]:
            l = i
        else:
            result = max(result, prices[i] - prices[l])

    return result


print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))
