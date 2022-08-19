# reversing a list

list = [55,643,87,43,5,90]
list.reverse()
print(list)

#Other method to reverse a list 
def reverse(lst):
    new_lst = lst[::-1] #it reverse the elements one by one in reverse 
    return new_lst
 
lst = [10, 11, 12, 13, 14, 15]
print(reverse(lst))


