def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    string= ''
    for i in a:
      string+= str(i)+' '

    for i in string:
      i= i.strip('-')
    
    return string
    



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
