#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache= {}
    # add to cache where src= key, dest= value
    for i in range(length):
      cache[tickets[i].source]= tickets[i].destination

    # find starting dest. has NONE as src
    route= []
    start= {}
    for i, v in cache.items():
      if i == 'NONE':
        start= v
        route.append(start)

    # start with 'start' get its dest
    next= start
    while len(route) < len(tickets):
      for k, v in cache.items():
        if k == next:
          next= cache[k]
          route.append(next)

    return route