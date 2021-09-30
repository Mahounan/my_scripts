#You are a doctor who needs to clean up medical patient records, which are currently stored in one large string.

#In this project, you will use your new knowledge of Python strings to obtain and clean up medical data so that 
#it is easier to read and analyze.

#Let’s get started!


medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# The string medical_data stores the medical records for ten individuals. Each record is separated by a ; and contains the name, age, BMI (body mass index), and insurance cost for an individual, in that order.

#1-Print medical_data to see the output in the terminal
print(medical_data)

#2-We want the insurance costs to be represented in US dollars.

# Replace all instances of # in medical_data with $. Store the result in a variable called updated_medical_data.

#Print updated_medical_data

updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)

#3-We want to calculate the number of medical records in our data.

#Create a variable called num_records and initialize it at 0.
num_records = 0

#4-Next, write a for loop to iterate through the updated_medical_data string. Inside of the loop, add 1 to num_records when the current character is equal to $.

for update in updated_medical_data:
  if update == "$":
    num_records += 1

#5-Outside of the loop, print num_records with the following message:
print("There are", str(num_records), "medical records in the data.")

#6-The medical data in its current form is difficult to analyze. An essential job for a data scientist is to clean up data so that it’s easy to work with.

#Let’s start off by splitting the updated_medical_data string into a list of each medical record. Remember that each medical record is separated by a ; in the string.

#Store the result in a variable called medical_data_split and print this variable.

medical_data_split = updated_medical_data.split(";")

print(medical_data_split)

#7-Our data is now stored in a list, but it is still hard to read. Let’s split each medical record into its own list.

#First, define an empty list called medical_records.

medical_records = []

#8-Next, iterate through medical_data_split and for each record, split the string after each comma (,) and append the split string to medical_records.

#Print medical_records after the loop.

for split in medical_data_split:
  medical_records.append(split.split(","))

print(medical_records)

#9-Our data is now slightly more readable. However, it is not properly formatted – it contains unnecessary whitespace.

#To fix this, let’s start by creating an empty list called medical_records_clean.

medical_records_clean = []

#10-Next, use a for loop to iterate through medical_records.

#Inside of the loop, create an empty list called record_clean. We’ll use this list to store a formatted version of each medical record.

#11-After the record_clean variable, create a nested for loop that goes through each record:

#for item in record:

#Inside of this loop, append item.strip() to record_clean to remove any whitespace from the string.

#12-Finally, we need to add each cleaned up record to medical_records_clean.

#Outside of the nested for loop, append record_clean to medical_records_clean.

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

#13-Print medical_records_clean outside of the for loops to see the output.

#You should see output that is formatted and much easier to read.

print(medical_records_clean)

#14-Our data is now clean and ready for analysis.

#For example, to print out the names of each of the ten individuals, we can use the following loop:

for record in medical_records_clean:
  print(record[0])

#15-You want all of the names in the medical records to be in uppercase characters.

#In the for loop, update records[0] before the print statement so that all of the characters are uppercase.
for record in medical_records_clean:
  print(record[0].upper())

#16-Let’s store each name, age, BMI, and insurance cost in separate lists.

#To start, create four empty lists: names ages bmis insurance_costs
names = []
ages = []
bmis = []
insurance_costs = []

#17-Next, iterate through medical_records_clean and for each record:

#Append the name to names.
#Append the age to ages.
#Append the BMI to bmis.
#Append the insurance cost to insurance_costs.

for clean in medical_records_clean:
  names.append(clean[0])
  ages.append(clean[1])
  bmis.append(clean[2])
  insurance_costs.append(clean[3])

#18-Print names, ages, bmis, and insurance_costs outside of the loop.
#Make sure the output is what you expect.
print("Names:", names)
print("Ages:", ages)
print("BMIs:", bmis)
print("Insurance Costs:", insurance_costs)

#19-Now that all of our data is in separate lists, we can easily perform analysis on that data. Let’s calculate the average BMI in our dataset.

#First, create a variable called total_bmi and set it equal to 0.

total_bmi = 0

#20-Next, use a for loop to iterate through bmis and add each bmi to total_bmi.

#Remember to convert bmi to a float.
for bmi in bmis:
  total_bmi += float(bmi)

#21-After the for loop, create a variable called average_bmi that stores the total_bmi divided by the length of the bmis list.
average_bmi = total_bmi/len(bmis)

#Print out average_bmi with the following message:
print("Average BMI:", str(round(average_bmi, 2)))

#EXTRA

#22-Calculate the average insurance cost in insurance_costs. You will have to remove the $ in order to calculate this.
total_insur = 0
for item in insurance_costs:
  total_insur += float(item.strip("$"))

average_insurance = total_insur/len(insurance_costs)

print("Average Insurance:", str(round(average_insurance, 2)))


#23-Write a for loop that outputs a string for each individual in the following format:
#Marina is 27 year olds with a BMI of 31.1 and an insurance cost of $7010.0.
#Markus is 30 years old with a BMI of 22.4 and an insurance cost of $4050.0
#...

for i in range(len(medical_records_clean)):
  print(medical_records_clean[i][0], "is", medical_records_clean[i][1], "years olds with a BMI of", medical_records_clean[i][2], "and an insurance cost of", medical_records_clean[i][3])

