def get_indices_of_item_weights(weights, length, limit):
    cache= {}
    res= []
    """
    YOUR CODE HERE
    """
    # Your code here
    if len(weights) == 1:
        return None
    # 
    # add weights to dict with weight as value, and indicies as key
    for ind, weight in enumerate(weights):
        if ind not in cache:
            cache[ind]= weight

    #  ind  weight
    for ww, vv  in cache.items():
        # ind weight
        for k, v in cache.items():
            # comparr indicies so we dont calc ind[1] with ind[1]
            if ww != k:
                added= vv  + v
                if added == limit:
                    res.append(ww)
    print('res rev: ', res.reverse())
    return res