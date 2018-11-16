def sorter(numbers):
	# Input: [3,1,2,4,5,4,5,6]
	# Output: [1,2,3,6,4,4,5,5]
	# Sort by frequency first, and then by value

	sortedNumbers = sorted(numbers)
	grouped = []
	previous = None
	for i in range(0, len(sortedNumbers)):
		if sortedNumbers[i] == previous:
			grouped[-1].append(sortedNumbers[i])
		else:
			grouped.append([])
			grouped[-1].append(sortedNumbers[i])
		previous = sortedNumbers[i]
	sortedGrouped = sorted(grouped, key = len)
	return sortedGrouped

print(sorter([3,1,2,4,5,4,5,6]))