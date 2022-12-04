class Elf:
    def __init__(self, id):
        self.id = id
    
    # the calories in each food the elf is carrying
    foods = []

    def get_total_cals(self):
        cals = 0
        for c in self.foods:
            cals += int(c)
        return cals