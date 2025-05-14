class StockSpanner:
    def __init__(self):
        self.prev_days = []

    def next(self, price: int) -> int:
        days = 1

        while self.prev_days:
            min_price, day_count = self.prev_days[-1]
            if price < min_price:
                break
            days += day_count
            self.prev_days.pop()

        self.prev_days.append((price, days))
        return days
