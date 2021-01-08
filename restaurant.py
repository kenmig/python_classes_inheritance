class Restaurant():
    """ This is a car class that will display the location, price, and type of food """
    def __init__(self, location, price, food):
        self.location = location
        self.price = price
        self.food = food
        self.revenue = 5000

    def __str__(self):
        return "{}, {}, {}".format(self.location, self.price, self.food)

    def promotion(self):
        self.revenue += 500
        print(f"Amount made: {self.revenue}")

    def check_revenue(self):
        print(f"Revenue: {self.revenue}")

restaurant1 = Restaurant('Atlanta', 'Average', 'Wings')

restaurant1.check_revenue()
restaurant1.promotion()
restaurant1.check_revenue()