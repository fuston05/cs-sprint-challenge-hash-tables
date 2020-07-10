def get_indices_of_item_weights(weights, length, limit):
    cache= {}
    """
    YOUR CODE HERE
    """
    # Your code here
    # 
    # add weights to dict with index as value
    for i in range(length):
        if weights[i] not in cache:
            cache[weights[i]]= [i]
        else: cache[weights[i]].append(i)
    



    return cache

    # iterate dict adding all key pairs of weights
      # create a list of tuples containg weights indicies pair and their total value
      #        ind, ind, total
      # list[ (4, 5, 9), (2, 6, 8), (8, 4, 12) ]
    
    # then we can iterate list checking list[i][2] against limit
    # if it matches return list[i][0], list[i][1]

weights_1 = [9]
weights_2 = [4, 4]
weights_3 = [4, 6, 10, 15, 16]
weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# print(get_indices_of_item_weights(weights_1, 1, 9))
print('')
# print(get_indices_of_item_weights(weights_2, 2, 8))
print('')
print(get_indices_of_item_weights(weights_3, 5, 21))
print('')
# print(get_indices_of_item_weights(weights_4, 9, 7))