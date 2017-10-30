def findMaxMin(my_list):
    biggest = max(my_list)
    smallest = min(my_list)
    final_list=[]
    
    if (biggest > smallest):
        final_list = [smallest, biggest]
    elif (biggest == smallest):
        final_list = [biggest]
    else:
        return False
    return final_list

