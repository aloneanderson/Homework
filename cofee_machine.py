class CoffeeMachine:
    water = 100
    seed = 50
    __current_trash = 0
    __max_trash = 100

    def trash(self):
        self.__current_trash = 0

    def add_water(self):
        self.water = 200

    def add_seed(self):
        self.seed = 100

    def check_trash(self, trash):
        return self.__current_trash + trash > self.__max_trash

    def make_americano(self):
        if self.water < 10:
            print("Water is over")
            return
        if self.seed < 5:
            print("Seeds is over")
            return
        if self.check_trash(2):
            print("Clear cofee machine")
            return
        self.water -= 10
        self.seed -= 5
        self.__current_trash += 2
        print("Take ur Americano")
        if self.water <= 0:
            self.add_water()
        if self.seed <= 0:
            self.add_seed()
        if self.__current_trash >= self.__max_trash:
            self.trash()

    def make_espresso(self):
        if self.water < 5:
            print("Water is over")
            return
        if self.seed < 5:
            print("Seeds is over")
            return
        if self.check_trash(2):
            print("Clear cofee machine")
            return
        self.water -= 5
        self.seed -= 10
        self.__current_trash += 10
        print("Take ur Espresso")
        if self.water <= 0:
            self.add_water()
        if self.seed <= 0:
            self.add_seed()
        if self.__current_trash >= self.__max_trash:
            self.trash()


class CoffeeMilk(CoffeeMachine):
    milk = 80

    def add_milk(self):
        self.milk = 100

    def make_latte(self):
        if self.water < 5:
            print("Water is over")
            return
        if self.seed < 5:
            print("Seeds is over")
            return
        if self.check_trash(2):
            print("Clear cofee machine")
            return
        if self.milk < 5:
            print("milk is over")
            return
        self.water -= 10
        self.seed -= 10
        self.milk -= 15
        self._CoffeeMachine__current_trash += 10
        print("Take ur Latte")
        if self.water <= 0:
            self.add_water()
        if self.seed <= 0:
            self.add_seed()
        if self._CoffeeMachine__current_trash == self._CoffeeMachine__max_trash:
            self.trash()
        if self.milk <= 0:
            self.add_milk()

    def make_capuchino(self):
        if self.water < 5:
            print("Water is over")
            return
        if self.seed < 5:
            print("Seeds is over")
            return
        if self.check_trash(2):
            print("Clear cofee machine")
            return
        if self.milk < 5:
            print("milk is over")
            return
        self.water -= 10
        self.seed -= 10
        self.milk -= 5
        self._CoffeeMachine__current_trash += 10
        print("Take ur Capuchino")
        if self.water <= 0:
            self.add_water()
        if self.seed <= 0:
            self.add_seed()
        if self._CoffeeMachine__current_trash == self._CoffeeMachine__max_trash:
            self.trash()
        if self.milk <= 0:
            self.add_milk()


class HappyCoffee(CoffeeMilk):
    cognac = 20

    def add_cognac(self):
        self.cognac = 20

    def make_cofee_with_cognac(self):
        if self.water < 5:
            print("Water is over")
            return
        if self.seed < 5:
            print("Seeds is over")
            return
        if self.check_trash(2):
            print("Clear cofee machine")
            return
        if self.milk < 5:
            print("milk is over")
            return
        if self.cognac <= 1:
            print("cognac is over")
            return
        self.water -= 10
        self.seed -= 10
        self.milk -= 5
        self.cognac -= 2
        self._CoffeeMachine__current_trash += 10
        print("Take ur Coffee with Cognac")
        if self.water <= 0:
            self.add_water()
        if self.seed <= 0:
            self.add_seed()
        if self._CoffeeMachine__current_trash == self._CoffeeMachine__max_trash:
            self.trash()
        if self.milk <= 0:
            self.add_milk()
        if self.cognac <= 1:
            self.add_cognac()


americano = CoffeeMachine()
espresso = CoffeeMachine()
espresso.make_espresso()
americano.make_americano()
latte = CoffeeMilk()
latte.make_latte()
capuchino = CoffeeMilk()
capuchino.make_capuchino()
cognac = HappyCoffee()
cognac.make_cofee_with_cognac()

for i in range(100):
    cognac.make_cofee_with_cognac()


