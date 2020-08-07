#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    # iterate and add all tickets to cache with key = starting location,
    #  and value being destination
    for i in tickets:
        cache[i.source] = i.destination

    # loop through cache
        # add to result list when destination == source of the next
    start = cache['NONE']
    result = [start]
    count = 0
    cur = start
    for _ in cache:
        for s, d in cache.items():
            if count > 0:
                if cur == s and d != 'NONE':
                    result.append(d)
                    cur = cache[s]
            count += 1
    result.append('NONE')

    return result


if __name__ == "__main__":

    # ticket_1 = Ticket("NONE", "PDX")
    # ticket_2 = Ticket("PDX", "DCA")
    # ticket_3 = Ticket("DCA", "NONE")
    # tickets = [ticket_1, ticket_2, ticket_3]
    # expected = ["PDX", "DCA", "NONE"]
    # print(reconstruct_trip(tickets, 3))

    # ticket_1 = Ticket("PIT", "ORD")
    # ticket_2 = Ticket("XNA", "SAP")
    # ticket_3 = Ticket("SFO", "BHM")
    # ticket_4 = Ticket("FLG", "XNA")
    # ticket_5 = Ticket("NONE", "LAX")
    # ticket_6 = Ticket("LAX", "SFO")
    # ticket_7 = Ticket("SAP", "SLC")
    # ticket_8 = Ticket("ORD", "NONE")
    # ticket_9 = Ticket("SLC", "PIT")
    # ticket_10 = Ticket("BHM", "FLG")

    # tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

    # expected = ["LAX", "SFO", "BHM", "FLG",
    #             "XNA", "SAP", "SLC", "PIT", "ORD", "NONE"]
    # print(reconstruct_trip(tickets, 10))
