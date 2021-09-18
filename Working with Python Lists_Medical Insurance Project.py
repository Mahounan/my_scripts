names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]


#1-
#Append a new individual, "Priscilla", to names.
#Append her insurance cost, 8320.0, to insurance_costs.
names.append("Priscilla")
insurance_costs.append(8320.0)

#2-Create a new variable called medical_records that combines insurance_costs and names into a list using the zip() function.
medical_records = list(zip(insurance_costs, names))

#3-Print out medical_records in the terminal, and make sure the output is what you expected.
print(medical_records)

#4-We want to see how many medical records we’re dealing with. Create a variable called num_medical_records that stores the length of medical_records.
num_medical_records = len(medical_records)

#5-Print num_medical_records with the following message:
print("There are", str(num_medical_records), "medical records")

#6-Select the first medical record in medical_records, and save it to a variable called first_medical_record.
first_medical_record = medical_records[0]

#7-Print first_medical_record with the following message:
print("Here is the first medical record:", str(first_medical_record))


#8-
#Sort medical_records so that the individuals with the lowest insurance costs appear at the start of the list.
medical_records.sort()

#Print the sorted medical_records with the following message:
print("Here are the medical records sorted by insurance cost:", str(medical_records))

#9-Slice the medical_records list, and store the three cheapest insurance costs in a list called cheapest_three.
cheapest_three = medical_records[:3]

#10-Print cheapest_three with the following message:
print("Here are the three cheapest insurance costs in our medical records:", str(cheapest_three))

#11-Slice the medical_records list, and store the three most expensive insurance costs in a list called priciest_three.
priciest_three = medical_records[-3:]

#12-Print priciest_three with the following message:
print("Here are the three most expensive insurance costs in our medical records:", str(priciest_three))

#13.Some individuals in our medical records have the same name. For example, the name “Paul” shows up twice.

#Count the number of occurrences of “Paul” in the names list, and store the result in a variable called occurrences_paul.

#Print occurrences_paul with the following message
occurrences_paul = names.count("Paul")
print("There are", str(occurrences_paul), "individuals with the name Paul in our medical records.")

#14-
#Sort the medical records alphabetically by name. You’ll have to create a new list using zip() to do this.
medical_records_names = list(zip(names, insurance_costs))
print(medical_records_names)

#Select the medical records starting at index 3 and ending at index 7 and save it in a variable called middle_five_records.
middle_five_records = medical_records_names[3:8]
print(middle_five_records)

