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




'''input_num = raw_input("Enter numbers separated by space: ")
input_list = [int(n) for n in input_num.split()]

def findMaxMin(input_list):
    biggest = max(input_list)
    smallest = min(input_list)
    final_list=[]
    
    if (biggest > smallest):
        final_list = [smallest, biggest]
    elif (biggest == smallest):
        final_list = [biggest]
    else:
        return False
    return final_list'''