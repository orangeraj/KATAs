count = 0

def bigger_neighbour(lst):
    global count

    for item in lst:
        index = lst.index(item)
      
        if index != 0 and index != len(lst)-1:
            if lst[index] > lst[index+1] and lst[index] > lst[index-1]:
                count+=1
                print(lst[index])
            else:
                pass


    return count


lst = ['1','2','1','4','2']
print(bigger_neighbour(lst))