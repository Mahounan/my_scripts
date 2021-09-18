#1. Every Three Numbers

#Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3 
#starting from a number that is passed to the function as an input parameter. 

#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))



#2. Remove Middle
#Our next function will remove all elements from a list with an index within a certain range. 
#The function will accept a list, a starting index, and an ending index. All elements with an index 
#between the starting and ending index should be removed from the list.

#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))



#3. More Frequent Item

#Let’s go back to our factory example. We have a conveyor belt of items where each item is represented by 
#a different number. We want to know, out of two items, which one shows up more on our belt. 
#To solve this, we can use a function with three parameters. One parameter for the list of items, 
#another for the first item we are comparing, and another for the second item.

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))



#4. Double Index

#Our next function will double a value at a given position. We will provide a list and an index to double. 
#This will create a new list by replacing the value at the index provided with double the original value. 
#If the index is invalid then we should return the original list.

#Write your function here
def double_index(lst, index):
  if index >= (len(lst)-1):
    return lst
  else:
    new_lst = lst[0:index]
    new_lst.append(lst[index]*2)
    new_lst = new_lst + lst[index+1:]
    return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))



#5. Middle Item

#For the final code challenge, we are going to create a function that finds the middle item from a list of values. 
#This will be different depending on whether there are an odd or even number of values. In the case of an odd 
#number of elements, we want this function to return the exact middle value. If there is an even number of elements,
#it returns the average of the middle two elements. 

#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2)-1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))