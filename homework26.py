class Bus:
    def __init__(self):
        pass
    def fare(self, seats, mcharge):
        totfare = ((mcharge/100 * seats) + seats) * 100
        print(totfare)
obj = Bus()
obj.fare(50, 10)