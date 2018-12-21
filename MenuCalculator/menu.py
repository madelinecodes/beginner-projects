'''class food:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    def order(self):




print(f1.name)
print(f1.price)'''


class Menu:
    def __init__(self, *args):
        self.items = dict()
        for idx in range(0, len(args)):
            item = args[idx]
            # put all the tuples into our dict
            # e.g., '1' -> ('1', 'name', 'amount)
            self.items[item[0]] = item
    
    def take_input(self):
        print(self.items)
        while True:
            nums = input()
            total = 0
            for idx in range(0, len(nums)):
                key = nums[idx]
                # access tje 
                total += self.items[key][2]
            print(total)

fast_food_menu = Menu(
    ('1', "Chicken Strips", 3.50),
    ('2', "French Fries", 2.50),
    ('3', "Hamburger ", 4.00),
    ('4', "Hotdog ", 3.50),
    ('5', "Large Drink", 1.75),
    ('6', "Medium Drink", 1.50),
    ('7', "Salad", 3.75),
    ('8', "Small Drink", 1.25),
)

fast_food_menu.take_input()


food = {
"Chicken Strips": 3.50,
"French Fries": 2.50,
"Hamburger ": 4.00,
"Hotdog ": 3.50,
"Large Drink": 1.75,
"Medium Drink": 1.50,
"Salad": 3.75,
"Small Drink": 1.25
}