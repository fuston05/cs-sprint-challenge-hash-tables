def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache= {}
    # Your code here
    for i in a:
      if i not in cache:
        cache[i]= None 

    result= []
    for k, v in cache.items():
      k= str(k)
      if k[0] == '-':

        for i, j in cache.items():
          i= str(i)
          if i == k[1]:
            result.append(int(k[1]))

        
      # print(k)

    return(result)

      # if i != '' and i not in cache:
      #   cache[i]= 1
      # else: 
      #   cache[i]+=1


    # # remove the '-'
    # for i in string:
    #   if i[0] == '-':
    #     string= string.replace(i, '')

    # string= string.split()

    # # any dups we have means one had a '-', so return it
    # for i in string:
    #   if i not in cache:
    #     cache[i]= 1
    #   else: 
    #     cache[i]+=1

    # result= []
    # for k, v in cache.items():
    #   if v > 2:
    #     result.append(k)
        
    

      
    


    



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
