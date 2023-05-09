from vehicles import Car


def main():
    car = Car()
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, or show average [S]peed?\n").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            car.accelerate()
        elif action == 'B':
            car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(car.average_speed()))
        car.step()
        car.say_state()


if __name__ == '__main__':
    main()
