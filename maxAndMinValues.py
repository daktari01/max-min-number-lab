def findMaxMin():
    input_num = raw_input("Enter numbers separated by space: ")
    input_list = [int(n) for n in input_num.split()]
    
    biggest = max(input_list)
    smallest = min(input_list)
    
    if (biggest > smallest):
        final_list = [smallest, biggest]
    elif (biggest == smallest):
        final_list = [biggest]
    else:
        return False
    return final_list