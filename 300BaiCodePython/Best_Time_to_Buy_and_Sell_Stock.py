def maxProfit(self, prices: List[int]) -> int:
    """
        :type prices: List[int]
        :rtype: int
    """
    res = 0
    temp = float('inf')
    for price in prices:
        temp = min(temp, price)
        res = max(price - temp, res)
    return res