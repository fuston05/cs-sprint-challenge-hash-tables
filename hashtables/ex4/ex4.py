def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    # Your code here
    a.sort(reverse= True)

    for i in a:
      if i not in cache:
        cache[i]= None

    result= []
    for c in cache:
      isNeg= c- (c*2)
      if isNeg in cache:
        if c > 0:
          result.append(c)

    result.sort()
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    #                     [-4, -2, -1, 1, 2, 3, 4]

    # print(has_negatives([1,2,3]))
    # self.assertTrue(result == [])

    # print(has_negatives([1,2,3,-4]))
    # # self.assertTrue(result == [])

    # print(has_negatives([-1,-2,1,2,3,4,-4]))
    # result.sort()
    # self.assertTrue(result == [1,2,4])