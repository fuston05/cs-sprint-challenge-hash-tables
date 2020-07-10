# Your code here
cache= {}


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    count= 0
    for i in files:
      if i not in cache:
        cache[i]= count
        count+= 1

    res= []
    for i in cache:
      if queries[count] in cache:
        res.append()
      

    # print(res)

    return res


if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    files= []
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]
    queries = [
            "qux"
        ]

    print(finder(files, queries))
