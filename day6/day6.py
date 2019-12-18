from dataclasses import dataclass
from typing import Union


@dataclass()
class Planet:
    name: str
    orbits:  Union['Planet', None]


def main():
    orbits = {}
    with open("input.txt", "r") as file:
        for line in file:
            item = line.strip().split(")")
            if item[0] not in orbits:
                orbits[item[0]] = Planet(item[0], None)
            if item[1] in orbits:
                orbits[item[1]].orbits = orbits[item[0]]
            orbits[item[1]] = Planet(item[1], orbits[item[0]])
    return orbits


def distance(orbits):
    planet = orbits["SAN"]
    dist = 0
    san = {planet.name: dist}
    while planet.orbits is not None:
        dist += 1
        san[planet.orbits.name] = dist
        planet = planet.orbits

    dist = 0
    common_planet = None
    planet = orbits["YOU"]
    print("SAN" in san)
    while planet.orbits is not None:
        if planet.orbits.name in san:
            common_planet = planet.orbits.name
            break
        dist += 1
        planet = planet.orbits

    """for item in san:
        if item[0] == common_planet:
            return dist + item[1]"""
    return san[common_planet] + dist - 1


def get_tot_orbits(orbits):
    tot = 0
    for planet in orbits.values():
        while True:
            if planet.orbits is None:
                break
            planet = planet.orbits
            tot += 1
    print(tot)


if __name__ == "__main__":
    print(distance(main()))
