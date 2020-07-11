# Your code here
cache = {}


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    count = 0
    for i in files:
        splitFiles = i.split('/')
        sub = splitFiles[len(splitFiles)-1]

        # if key not in cache:
        if sub not in cache:
          # add that key
          cache[sub]= tuple()
          # add path to tuple value
          cache[sub]+= (i,)

        # if key IS in cache
        else:
          # check key  => values for our current value
          for c in cache[sub]:
            print('check tuple: ', c)

        # else: 
            # if it's not there, add new value to that key




    print('cache: ', cache)
    print('')

    res = []
    

    res.sort()
    # print('res: ', res)
    print('')
    return res


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/test/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]

    queries = [
        "foo",
        "qux",
        "baz"
    ]

    # files= []

    # queries = [
    #         "qux"
    #     ]

    print(finder(files, queries))
