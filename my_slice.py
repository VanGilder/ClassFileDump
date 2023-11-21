#!/usr/bin/env python3



def my_slice(to_slice, start=0, end=None, step=1):
    if end == None:
        end = len(to_slice)

    #Negative indexing
    if start < 0:
        start+= len(to_slice)

    if end < 0:
        end+= len(to_slice)

    #Overshooting start of end indexing
    if start < 0:
        start = 0

    if end > len(to_slice):
        end = len(to_slice)

    #Get slice
    results = []

    for i in range(start, end, step):
        results.append(to_slice[i])

    if type(to_slice) is str:
        return "".join(results)

    return results


    print(my_slice("abcdefg", -12, 2000))
