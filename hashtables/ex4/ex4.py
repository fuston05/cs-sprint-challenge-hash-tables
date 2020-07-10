def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    # Your code here
    string = ''
    for i in a:
        string += str(i)+' '
    string= string.split()

    for i in string:
        # print(i)
        if i not in cache:
            if i[0] == '-':
                cache[i] = 'neg'
            else: 
              cache[i]= 'pos'


    return cache

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
