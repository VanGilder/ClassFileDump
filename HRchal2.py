#!/bin/python3

import math
import os
import random
import re
import sys


def journeyToMoon(totalAstros, astroPairs):
    astroCountry = {i: set([i]) for i in range(totalAstros)}

    # Process each pair of astronauts
    for a1, a2 in astroPairs:
        country1 = astroCountry[a1]
        country2 = astroCountry[a2]

        # If they belong to different countries, merge the countries
        if country1 != country2:
            newCountry = country1.union(country2)
            for astro in newCountry:
                astroCountry[astro] = newCountry

    # Get unique countries
    uniqueCountries = set(map(tuple, astroCountry.values()))

    # Calculate sizes of each unique country
    countrySizes = [len(country) for country in uniqueCountries]

    # Calculate number of valid pairs
    totalPairs = totalAstros * (totalAstros - 1) // 2
    sameCountryPairs = sum(size * (size - 1) // 2 for size in countrySizes)

    return totalPairs - sameCountryPairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

