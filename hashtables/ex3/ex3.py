def intersection(arrays):
  """
  YOUR CODE HERE
  """
  
  cache= {}
  res= []

  listCount= 0
  for list in arrays: 
    # list is a sub array
    #remove duplicates
    list= set(list)

    for num in list:
    # if num not in cache add it.
      if num not in cache:
        cache[num]= 1
      elif num in cache and listCount > 0:
        # if it IS in cache, increment its counter
        cache[num]+= 1
    listCount+= 1

    # find all counters that equal the num of sub lists that were passed in
    for k,v in cache.items():
      if v == len(arrays):
        res.append(k)

  return res


if __name__ == "__main__":
  arrays = []

  arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
  arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
  arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

  print(intersection(arrays))
