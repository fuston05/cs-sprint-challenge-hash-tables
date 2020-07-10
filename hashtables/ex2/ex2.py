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
    # print(start)
    # final dest has NONE as dest


    # start with 'start' get its dest
    next= start
    while len(route) < len(tickets):
      for k, v in cache.items():
        if k == next:
          next= cache[k]
          route.append(next)

      # if i.source == start.destination:
      #   print(i.source)
    # search and find ticket with src == start.dest
    # that will be the next ticket.
    # move to next ticket, and repeat




    # print('route: ', route)
    # print('')
    # print('next: ', next)
    # print('')
    # print('cache: ', cache)
    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, len(tickets)))

# expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP", "SLC", "PIT", "ORD", "NONE"]