# Brayden VanGilder

# Function to find a target number using binary search -- Time Complexity: O(log N)
def findNumber(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Read numbers and queries from file -- Time Complexity: O(N)
inputFile = open("input.dat", "r")
numOfNumbers = int(inputFile.readline().strip())
numbers = list(map(int, inputFile.readline().split()))
numOfQueries = int(inputFile.readline().strip())
queries = list(map(int, inputFile.readline().split()))
inputFile.close()

# Sort the list of numbers -- Time Complexity: O(N log N)
numbers.sort()

# Prepare to write the output to file
outputFile = open("output.dat", "w")

# Loop over each query -- Time Complexity: O(Q log N)
for query in queries:
    position = findNumber(numbers, query)

    if position != -1:
        first = position
        last = position

        # Find the first occurrence
        while first > 0 and numbers[first - 1] == query:
            first = first - 1

        # Find the last occurrence
        while last < len(numbers) - 1 and numbers[last + 1] == query:
            last = last + 1

        # Write the count to the output file
        outputFile.write(str(last - first + 1) + "\n")
    else:
        outputFile.write("0\n")

# Close the output file
outputFile.close()



'''

Reading N numbers and Q queries takes O(N) time
Sorting N numbers using python's built in Timsort function takes O(N log N) time
For each query finding the first and last occurrence of a number using binary search takes O(log N) time but since there are Q queries this step has a time complexity of O(Q log N).

So the overall time complexity of the algorithm is O(N log N)+O(Q log N)+O(N)
= O((N+Q) log N).

'''
