# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    res = []
    # Your code here
    for i in files:
        # get substr from file path, that matches queries
        splitFiles = i.split('/')
        sub = splitFiles[len(splitFiles)-1]

        # if key not in cache:
        if sub not in cache:
            # store 'sub' as key, and full path as tuple of values
            # add that key to a new tuple
            cache[sub] = tuple()
            # add full path to tuple
            cache[sub] += (i,)

        # if key IS in cache
        else:
            # append path to existing tuple for given key
            cache[sub] += (i,)

    for q in queries:
      # get the KEY
      if cache.get(q):
        # if key is found
        # check the tuple for the exact path value
        for i in cache[q]:
          res.append(i)
    res.sort()
    return res
