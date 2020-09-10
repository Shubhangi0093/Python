lst=[10,20,"Shubhangi",-10,30.5]
#list display
print(lst)

#displays obj at index 3
print(lst[3])

#displays obj from index 3 to 5
print(lst[3:5])

#repeats the list elements 4 time
print(lst*4)

# displays the length of the list
print(len(lst))

#append is to add element to the list
lst.append(40)
print(lst)

#remove keyword is used to remove the element from the list and it is case sensitive
lst.remove("Shubhangi")
print(lst)

#'del', deletes the element at index 1
del(lst[1])
print(lst)

print(max(lst))
print(min(lst))

