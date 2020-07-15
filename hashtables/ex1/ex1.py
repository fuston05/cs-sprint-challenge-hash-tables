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
    # add weights to dict with weight as value, index as key
    # to handle duplicate weights
    for ind, weight in enumerate(weights):
        if ind not in cache:
            cache[ind]= weight

    for ww, vv  in cache.items():
        for k, v in cache.items():
            # compare indicies (keys == indicies, values== weights)
            if ww != k:
                added= vv  + v
                if added == limit:
                    res.append(ww)

    return res
