class Bacteria:

    def __init__(self, x, y, life_count=5, level=1, passed=False):
        self.x = x
        self.y = y
        self.life_count = life_count
        self.passed = passed
        self.level = level


bacteria_1 = Bacteria(2, 6, 5)
bacteria_2 = Bacteria(1, 4, 5)
bacteria_3 = Bacteria(5, 7, 5)

color_entered = input("Guess color of bacteria_1: ")
if color_entered == "red":
    print("CORRECT!!!!!")
    bacteria_1.passed = True
    bacteria_1.level += 1
else:
    bacteria_1.life_count -= 1

print("Axis:", bacteria_1.x, ",", bacteria_1.y)
print("Current level:", bacteria_1.level)
print("Passed:", bacteria_1.passed)
print("Life count:", bacteria_1.life_count)


color_entered = input("Guess color of bacteria_2: ")
if color_entered == "blue":
    print("CORRECT!!!!!")
    bacteria_2.passed = True
    bacteria_2.level = bacteria_1.level
    bacteria_2.level += 1
    bacteria_2.life_count = bacteria_1.life_count
else:
    bacteria_2.level = bacteria_1.level
    bacteria_2.life_count = bacteria_1.life_count
    bacteria_2.life_count -= 1

print("Axis:", bacteria_2.x, ",", bacteria_2.y)
print("Current level:", bacteria_2.level)
print("Passed:", bacteria_2.passed)
print("Life count:", bacteria_2.life_count)


color_entered = input("Guess color of bacteria_3: ")
if color_entered == "yellow":
    print("CORRECT!!!!!")
    bacteria_3.passed = True
    bacteria_3.level = bacteria_2.level
    bacteria_3.level += 1
    bacteria_3.life_count = bacteria_2.life_count
else:
    bacteria_3.level = bacteria_2.level
    bacteria_3.life_count = bacteria_2.life_count
    bacteria_3.life_count -= 1

print("Axis:", bacteria_3.x, ",", bacteria_3.y)
print("Current level:", bacteria_3.level)
print("Passed:", bacteria_3.passed)
print("Life count:", bacteria_3.life_count)
