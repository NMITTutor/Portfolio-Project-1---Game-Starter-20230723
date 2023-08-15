import random
# max = 5
# the_bag = [(i,j) for i in range(1,max+1) for j in range(1,max+1)]
# print(the_bag,len(the_bag))

# def take_one():
#     global the_bag 
    
#     i = random.randint(1,len(the_bag)-1)
#     if i < len(the_bag):
#       result = the_bag[i]
#       del(the_bag[i])
#     else:
#        result = the_bag[i-1]
#        del(the_bag[i-1])
       
#     return result

# ten_random_tuples = [ take_one() for i in range(1, 11)]
# print(ten_random_tuples,len(ten_random_tuples))


# Using a closure to "clean" this up
def random_bag(max):
    # Captures a bag of tuples- 2D vectors, coordinates Max by Max
    # take_one takes a random tuple from the bag
    
    # make the bag of tuples - now local to the bag
    the_bag = [(i,j) for i in range(1,max+1) for j in range(1,max+1)]
    
    def take_one():
        # Capture the_bag
        nonlocal the_bag
        
        # Take one from the bag at a random place
        number_left_in_bag = len(the_bag)
        
        if number_left_in_bag > 0 :
            if number_left_in_bag == 1 :
                i = 0
            else:
                i = random.randrange(1,len(the_bag))
            
            result = the_bag[i]
            
            del(the_bag[i]) # this one has been taken
        else:
            result = tuple((),) # empty tuple?
            raise Exception("Tried to get more tuples than there are in this bag.")
        return result 
    
    return take_one

if __name__ == "__main__":
    # Make a bag of 25 tuples (5 x 5)
    next_from_bag =  random_bag(5)


    # # Generator for getting up to 5 random tuples from the bag
    five_from_bag = (next_from_bag() for i in range(1 , 6) )
    twenty_from_bag = (next_from_bag() for i in range(1 , 21) )

    # # Get 20 ... 
    #twenty = [item for item in twenty_from_bag]
    #print(twenty, len(twenty))

    # # There should be 5 left
    five = [item for item in five_from_bag]
    print(five,len(five))

    five = [item for item in five_from_bag]
    print(five,len(five))

    # # Watch out! What happens once we empty our bag? ...
    # try:
    #      print([next_from_bag() for i in range (1, 200)])
    # except Exception as e:
    #      print(e)