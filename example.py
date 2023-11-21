sequence = [8, 6, 9, 3, 1, 5]
queries = [9, 10, -8, 8, 5]

#sort the sequence - TIme complexity O(N long N)
sequence.sort()
print("Sorted sequence:", sequence)

#Binary search
def binary_search(seq, x):
    left = 0
    right = len(seq) - 1
    while left <= right:
        mid = (left + right) // 2
        if seq[mid] == x:
            left = mid + 1
        else:
            right = mid -1
    return False

# for each query, execute the binary search - Time complexity O(Q log N)
# Total time complexity for the whole algorithm = O((N + Q) log N)
for key in queries:
    result = binary_search(sequence, key)
    if result == True:
        print("The key", key, " exists in the sequence.")
    else:
        print("The key", key, " does not exist in the sequence.")

print("Done")
