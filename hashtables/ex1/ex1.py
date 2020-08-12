def get_indices_of_item_weights(weights, length, limit):
    result = None
    cache = {}
    # iterate and store weight and indicies in dict
    for i, weight in enumerate(weights):
        cache[i] = weight
    # loop over dict, check if each pair == limit
    for k, v in cache.items():
        cur = v
        for ind, weight in cache.items():
            if k != ind:
                if length != 1:
                    if cur + weight == limit:
                        if k > ind:
                            result = [k, ind]
                        else:
                            result = [ind, k]
        # if so, return the 2 indicies in a list,
    # sort greatest to smallest
    return result


if __name__ == "__main__":

    # weights_1 = [9]
    # print(get_indices_of_item_weights(weights_1, 1, 9))

    # weights_2 = [4, 4]
    # print(get_indices_of_item_weights(weights_2, 2, 8))

    # weights_3 = [4, 6, 10, 15, 16]
    # print(get_indices_of_item_weights(weights_3, 5, 21))

    # weights_4 = []
    # print(get_indices_of_item_weights(weights_4, 0, 21))
