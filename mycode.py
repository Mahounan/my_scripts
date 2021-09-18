print("I'm running Python code on my own environment!")

# Import modules:
import pandas as pd
import numpy as np

# Import the data:
user_data = pd.read_csv("user_data.csv")

# Create age variable and find population mean:
population_mean = np.mean(user_data["age"])

# Select increasingly larger samples:
extra_small_sample = user_data["age"][:10]
small_sample = user_data["age"][:50]
medium_sample = user_data["age"][:100]
large_sample = user_data["age"][:200]

# Calculate the mean of those samples:
extra_small_sample_mean = np.mean(extra_small_sample)
small_sample_mean = np.mean(small_sample)
medium_sample_mean = np.mean(medium_sample)
large_sample_mean = np.mean(large_sample)

# Print them all out!
print ("Extra Small Sample Mean: " + str(extra_small_sample_mean))
print ("Small Sample Mean: " + str(small_sample_mean))
print ("Medium Sample Mean: " + str(medium_sample_mean))
print ("Large Sample Mean: " + str(large_sample_mean))


print ("\nPopulation Mean: "+ str(population_mean))

# clean data
# Import the data:
pop_data = pd.read_csv("us_cities_small.csv")

# Look at the current pop_data DataFrame:
pop_data.head()

# Look at the current user_data DataFrame:
user_data.head()

# Merge the two datasets on the city column:

new_df = pd.merge(user_data, pop_data)
new_df.head(10)

# Write a logic statement that determines if a location is "rural" or "urban":
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# look at the new DataFrame:
new_df.head(20)

# Plot a histogram that shows the distribution of ages in the dataset:

age = new_df["age"]
sns.distplot(age)
plt.show()

# Find the mean age of urban and rural users:

location_mean_age = new_df.groupby('location').age.mean() # turns it into a series
location_mean_age.head()

# Graph the age difference between rural and urban using a barplot:

sns.barplot(
	data=new_df,
	x= "location",
	y= "age"
)

plt.show()

# Plot a violinplot, which shows the distribution of age in different locations:

sns.violinplot(data=new_df, x="location", y="age")
plt.show()

# Graph the population to age as a scatterplot: 

x = new_df['population_proper']
y = new_df['age']

plt.scatter(x, y, alpha=0.5)

plt.show()

# Use Seaborn to visualize a linear regression: 

sns.regplot(data=new_df, x="population_proper", y="age")

plt.show()



# Now we need to make our visualizations snazzy! 

# Linear regression plot:
sns.regplot(data=new_df, x="population_proper", y="age")

# Change the axes, so they're eaiser to undersatnd:
ax = plt.subplot(1, 1, 1)
ax.set_xticks([100000, 1000000, 2000000, 4000000, 8000000])
ax.set_xticklabels(['100k', '1m', '2m','4m', '8m'])


# Change the figure style and palette:
sns.set_style("white")
sns.set_palette("pastel")
sns.despine()


# Title the axes and plot: 
ax.set_xlabel("City Population") 
ax.set_ylabel("User Age") 
plt.title("Age against Population")


plt.show()