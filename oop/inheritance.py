class Animal:
    alive = True

    def eat(self):
        print("Animal is eating")

    def go(self):
        print("Animal can go")


class Duck(Animal):

    def go(self):  # method overiding
        print("duck can walk.")


class Bird(Animal):

    def fly(self):
        print("bird can only fly.")
        return self

    def speak(self):
        print("bird can only speak.")
        return self


ducky = Duck()
birdy = Bird()
print(ducky.alive)
print(birdy.alive)

ducky.go()
ducky.eat()

# method chaining
birdy \
    .fly() \
    .speak() \
    .eat()
