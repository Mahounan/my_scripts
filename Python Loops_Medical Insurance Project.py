names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# CREATING A FOR LOOP

#1-We want to calculate the average insurance cost each person paid. We’ll start by adding up all of the insurance costs.

#Create a variable total_cost and initialize it to 0.

total_cost = 0

#2-Use a for loop to iterate through actual_insurance_costs and add each insurance cost to the variable total_cost.
#for cost in actual_insurance_costs:
  #total_cost += cost

#Using while loop instead of a for loop
i = 0
while i < len(actual_insurance_costs):
  total_cost += actual_insurance_costs[i]
  i +=1

#3-After the for loop, create a variable called average_cost that stores the total_cost divided by the length of the actual_insurance_costs list.

average_cost = total_cost/len(actual_insurance_costs)

#4-Print average_cost with the following message
print("Average Insurance Cost:", str(average_cost))

#USING A RANGE IN LOOPS

#5-For each individual in names, we want to determine whether their insurance cost is above or below average.

#Write a for loop with variable i that goes from 0 to len(names)


#8-Inside of the for loop, use if, elif, else statements after the print statement to check whether the insurance cost is above, below, or equal to the average. Print out messages for each case

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for", name, "is", str(insurance_cost), "dollars.")
  if insurance_cost > average_cost:
    amount = insurance_cost-average_cost
    print("The insurance cost for", name, "is", str(amount), "above average")
  elif insurance_cost < average_cost:
    amount = average_cost-insurance_cost
    print("The insurance cost for", name, "is", str(amount), "below average")
  else:
    print("The insurance cost for", name, "is equal to average")

#10- If you look closely at actual_insurance_costs and estimated_insurance_costs, you will notice that each of the actual insurance costs are 10% higher than the estimated insurance costs.

#Using a list comprehension, create a new list called updated_estimated_costs, which has each element in estimated_insurance_costs multiplied by 11/10.
updated_estimated_costs = [round(cost * (11/10)) for cost in estimated_insurance_costs]

print(updated_estimated_costs)

