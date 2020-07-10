def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache1= {}
    cache2= {}

    for i in range(len(arrays)):
      cache1[i]= arrays[i]
      cache2[i]= arrays[i]

    for i in range(len(arrays-1)):
      if cache1[i] in cache2[i]

    return cache[0]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
