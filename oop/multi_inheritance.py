class Mammals:

    def give_birth_to_young_animals(self):
        print("mammals give bith to young animals")


class Whales:

    def feed_with_milk(self):
        print("They feed their young with milk.")


class Dolphins(Mammals, Whales):  # multiple inheritances

    def swim(self):
        print("They can swim")
        return self


# dolphin inherits from Whales and Mammals
dolphin = Dolphins()
dolphin.swim().feed_with_milk()
dolphin.give_birth_to_young_animals()
