def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache= {}
    a.sort(reverse= True)

    for i, v in enumerate(a): 
        cache[v]= i

    result= []

    for k, v in cache.items():
        if k > 0:
            item= k
            cur= (k - (k*2))
            if cache.get(cur):
                result.append(k)
    return result



if __name__ == "__main__":
    # print(has_negatives([1,2,3]))
    print(has_negatives([-1,-2,1,2,3,4,-4]))

