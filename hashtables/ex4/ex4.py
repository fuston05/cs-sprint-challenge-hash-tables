def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    # Your code here
    # reverse so we can start iterating over + nums
    a.sort(reverse= True)

    for i in a:
      # add to cache
      if i not in cache:
        cache[i]= None

    result= []

    for c in cache:
      # formula to find neg opposite
      isNeg= c- (c*2)
      if isNeg in cache:
        if c > 0:
          result.append(c)
          
    return result