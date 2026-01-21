def mean(lyst):
    """Returns the mean of a list of numbers."""
    sum = 0
    for number in lyst:
        sum += number
    if len(lyst) == 0:
        return 0
    else:
        return sum / len(lyst)

def mode(lyst):
    """Returns the mode of a list of numbers."""
    # Obtain the set of unique numbers and their
    # frequencies, saving these associations in
    # a dictionary
    theDictionary = {}
    for number in lyst:
        freq = theDictionary.get(number, None)
        if freq == None:
            # number entered for the first time
            theDictionary[number] = 1
        else:
            # number already seen, increment its freq
            theDictionary[number] = freq + 1

    # Find the mode by obtaining the maximum freq
    # in the dictionary and determining its key
    if len(theDictionary) == 0:
        return 0
    else:
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                return key

def median(lyst):
    """Returns the median of a list of numbers."""
    # Create a copy of lyst before sorting
    numbers = []
    for number in lyst:
        numbers.append(number)
    # Sort the list and return the number at its midpoint
    numbers.sort()
    if len(numbers) == 0:
        return 0
    else:
        midpoint = len(numbers) // 2
        if len(numbers) % 2 == 1:
            return numbers[midpoint]
        else:
            return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def main():
    """Tests the functions."""
    lyst = []
    for i in range(6):
      lyst.append(int(input('Enter a Value for the list: ')))
    print("List:", lyst)
    print("Mode:", mode(lyst))
    print("Median:", median(lyst))
    print("Mean:", mean(lyst))

if __name__ == "__main__":
    main()
