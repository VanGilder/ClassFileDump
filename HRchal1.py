#!/bin/python3

import math
import os
import random
import re
import sys

def gridlandMetro(n, m, k, track):
    totalCells = n * m
    cellsOccupiedByTracks = 0

    rowTrackInformation = {}

    # Loop through each track to update the row track information
    for index in range(k):
        rowNumber, startingColumn, endingColumn = track[index]
        if rowNumber not in rowTrackInformation:
            rowTrackInformation[rowNumber] = []
        rowTrackInformation[rowNumber].append((startingColumn, endingColumn))

    # Loop through each row to count the cells that are occupied by tracks
    for rowNumber in rowTrackInformation.keys():
        listOfTracks = rowTrackInformation[rowNumber]
        listOfTracks.sort()

        mergedStartingColumn = listOfTracks[0][0]
        mergedEndingColumn = listOfTracks[0][1]

        # Loop through each track in this row
        for index in range(1, len(listOfTracks)):
            currentStartingColumn, currentEndingColumn = listOfTracks[index]

            # If the current track overlaps with the merged track then update the merged track
            if currentStartingColumn <= mergedEndingColumn:
                mergedEndingColumn = max(mergedEndingColumn, currentEndingColumn)
            else:
                # Add the length of the current merged track to cellsOccupiedByTracks
                cellsOccupiedByTracks += mergedEndingColumn - mergedStartingColumn + 1

                mergedStartingColumn = currentStartingColumn
                mergedEndingColumn = currentEndingColumn

        cellsOccupiedByTracks += mergedEndingColumn - mergedStartingColumn + 1

    return totalCells - cellsOccupiedByTracks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()

