#1. Append Size
#For the first code challenge, we are going to calculate the length of a list and then 
#append the value to the end of the list.Write your function here
def append_size(lst):
  lst_len = len(lst)
  lst.append(lst_len)
  return lst
   

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))



#2. Append Sum
#Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end. 
#After doing so, it will repeat this process two more times and return the resulting list. 
#Write your function here
#1-Manual repetition
def append_sum(lst):
  lst_len = len(lst)
  lst.append((lst[lst_len-2] + lst[lst_len-1]))
  lst_len = len(lst)
  lst.append((lst[lst_len-2] + lst[lst_len-1]))
  lst_len = len(lst)
  lst.append((lst[lst_len-2] + lst[lst_len-1]))
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#Or a more simple code
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst



#3. Larger List
#Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end. 
#After doing so, it will repeat this process two more times and return the resulting list. 
#Write your function here
#2-Looping version of the above
def append_sum(lst):
    for i in range(3):
        lst_len = len(lst)
        lst.append((lst[lst_len-2] + lst[lst_len-1]))     
  
    return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#Or a more simple code
def append_sum(lst):
    for i in range(3):
        lst.append(lst[-1] + lst[-2])
    return lst


#4. More Than N
#Our factory produces a variety of different flavored snacks and we want to check the number of instances of a 
#certain type. We have a conveyor belt full of different types of snacks represented by different numbers. 
#Our function will accept a list of numbers (representing the type of snack), 
#a number for the second parameter (the type of snack we are looking for), 
#and another number as the third parameter (the maximum number of that type of snack on the conveyor belt). 
#The function will return True if the snack we are searching for appears more times than we provided as our 
#third parameter. 

#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))




#5. Combine Sort
#Finally, let’s create a function that combines two different lists together and then sorts them. 
#To do this we can combine the lists with an operation and then sort using a function call.

#Write your function here
def combine_sort(lst1, lst2):
  new_lst = sorted(lst1 + lst2)
  return new_lst

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))