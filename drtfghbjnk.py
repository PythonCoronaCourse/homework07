def find_largest(sequence):
    if sequence:
        largest = sequence[0]
        for x in range(len(sequence) - 1):
            if largest < sequence[x + 1]:
                largest = sequence[x + 1]
        return largest
    else:
        return None


a = "abAcda"
print(find_largest(a))
