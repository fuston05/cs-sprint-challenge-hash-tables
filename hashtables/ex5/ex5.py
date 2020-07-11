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
        # we have to store the path as key for Large tests to work
        if i not in cache:
            cache[i] = sub
            count += 1

    print('cache: ', cache)
    print('')

    res = []
    count = 0
    for q in queries:
        # *** left off here trying to match the query to dict values ****
        items = cache.values()
        if q == items[]:
            print('found Q: ', q)
            res.append(k)
        count += 1

    res.sort()
    print('res: ', res)
    print('')
    return res


if __name__ == "__main__":
    files = [
        '/bin/foo',
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
