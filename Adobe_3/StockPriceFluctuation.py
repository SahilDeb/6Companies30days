from heapq import heappush, heappop


class StockPrice:
    def __init__(self):
        self.price_updates = dict()
        self.latest_timestamp = 0
        self.max_price = []
        self.min_price = []

    def update(self, timestamp: int, price: int) -> None:
        self.price_updates[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        heappush(self.max_price, (-price, timestamp))
        heappush(self.min_price, (price, timestamp))

    def current(self) -> int:
        return self.price_updates[self.latest_timestamp]

    def maximum(self) -> int:
        while self.price_updates[self.max_price[0][1]] != -self.max_price[0][0]:
            heappop(self.max_price)
        return -self.max_price[0][0]

    def minimum(self) -> int:
        while self.price_updates[self.min_price[0][1]] != self.min_price[0][0]:
            heappop(self.min_price)
        return self.min_price[0][0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
