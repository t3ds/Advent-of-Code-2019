from math import floor


def load(file):
    with open(file, "rt") as f:
        return list(int(line) for line in f.readlines())


def module_fuel(mass):
    return int(floor(mass / 3)) - 2


def fuelFuel(mod_fuel):
    mass = 0
    add_mass = module_fuel(mod_fuel)

    while add_mass > 0:
        mass += add_mass
        add_mass = module_fuel(add_mass)

    return mass


if __name__ == "__main__":

    modules = load('1_input.txt')
    mod_fuel_req = 0
    fuel_fuel_req = 0
    for i in modules:
        mod_fuel = module_fuel(i)
        mod_fuel_req += mod_fuel

        fuel_fuel = fuelFuel(mod_fuel)
        fuel_fuel_req += fuel_fuel

    print("Part 1 : " + str(int(mod_fuel_req)))
    print("Part 2 : " + str(int(fuel_fuel_req)))
    print("Total : " + str(int(mod_fuel_req + fuel_fuel_req)))
