highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#1-Preserve the Verse has one final task for you. They have delivered you a string that contains a list of poems, titled highlighted_poems, they want to highlight on the site, but they need your help to parse the string into something that can display the name, title, and publication date of the highlighted poems on the site.

#First, start by printing highlighted_poems to the terminal and see how it displays..
print(highlighted_poems)

#2-The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication.

#Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.
highlighted_poems_list = highlighted_poems.split(",")

#3-Print highlighted_poems_list, how does the structure of the data look now?
print(highlighted_poems_list)


#4-Notice that there is inconsistent whitespace in highlighted_poems_list. Let’s clean that up.

#Start by creating a new empty list, highlighted_poems_stripped.

#Then, iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped.

highlighted_poems_stripped=[]
for element in highlighted_poems_list:
  stripped = element.strip()
  highlighted_poems_stripped.append(stripped)

#5-Print highlighted_poems_stripped.
#Looks good! All the whitespace is cleaned up.
print(highlighted_poems_stripped)

#6-Next we want to break up all the information for each poem into it’s own list, so we end up with a list of lists.

#Create a new empty list called highlighted_poems_details.

#7-Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details
highlighted_poems_details=[]
for element in highlighted_poems_stripped:
  stripped=element.split(":")
  highlighted_poems_details.append(stripped)

print(highlighted_poems_details)

#8-Great! Now we want to separate out all of the titles, the poets, and the publication dates into their own lists.

#Create three new empty lists, titles, poets, and dates.

#9-Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates.
titles=[x for (x,y,z) in highlighted_poems_details]
poets=[y for (x,y,z) in highlighted_poems_details]
dates=[z for (x,y,z) in highlighted_poems_details]

#10-Finally, write a for loop that uses .format() to print out the following string for each poem:

#The poem TITLE was published by POET in DATE.
for i in range(len(highlighted_poems_details)):
  print("The poem {title} was published by {poet} in {date}.".format(title=highlighted_poems_details[i][0], poet=highlighted_poems_details[i][1], date=highlighted_poems_details[i][2]))







