class Animal():
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed=1.7):
            self._cords = [0, 0, 0]
            self.speed = speed
    def move(self,dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(self._cords[0] * self.speed)
        print(self._cords[1] * self.speed)
        print(self._cords[2] * self.speed)

    def attack(self):
        if Animal._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif Animal._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(Animal.sound)

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f'Here are 2 eggs for you')

class AquaticAnimal(Animal):
    Animal._DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] -= abs(dz)*(self.speed//2)

class PoisonousAnimal(Animal):
    Animal._DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    Animal.sound = "Click-click-click"

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.lay_eggs()