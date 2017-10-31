# Title
Cooking With Data

# Abstract
Cooking and Eating healthy should not be complicated. In order to make this simple, we would like to explore, map and visualize flavors and ingredients that are dominant in certain dishes and cuisines, which and how ingredients are clustered around these and what information of nutrition benefit can be achieved from this. We would also like to make visualization map of flavors explorable and searchable in order to inspire and educate anyone with interest in looking behind particular recipes. 

 We intend to use different visualization approaches in order to investigate whether interaction does play a significant role in communicating the underlying patterns within the chosen sample data set.

If possible we would like to further enrich the given data set with additional data scraped from the recipe websites. Databases with nutritional information on the ingredients could be used to fill in the nutritional information missing from the recipes.



# Research questions
The  research question that we would like to answer at first is the following: 

"Are there subsets of ingredients that are regularly used together and subsets that are never combined with each other and what is a good way to visualize this?". 

Using this information we could answer other research questions. 


"Are certain ingredients associated more than others and therefore form a basis must have of ingredients at home?   


"Is it possible to, based on the subsets, generate new recipes or propose ingredients that go well with the ingredients that you have at home? "

"Can we propose enhancements to certain recipes?" . 

"Based on the ratings of the recipes,is it possible to find certain combinations that are loved more than others?" 

# Dataset
The dataset that will be used is the one on recipes provided by infolab stanford. This dataset consists of 2.5GB of html files, a readme and 1 $.tsv$ file with tab-seperated columns containing information about: The domain,url,recipe title,kcal,ingredients,.. but a bunch of data is missing. This data is quite limited in the information it provides therefore additional processing of the html files is necesairry to draw more interesting conclusions. We will scrape the recepies for rating and look into adding extra other info to make our picture more complete. 

# A list of internal milestones up until project milestone 2

-	Clear structuring of work packages and distributing tasks
-	Cleaning and Filtering the Dataset
-	Scraping the HTML files for extra info
-	Find subsets of ingredients that are often used together
-	Testing of Graph Plotting Techniques and various Frameworks (4.js, 		etc.)
-	Experimenting with first visualization techniques
-	Testing interactive methods (with WebGL for example)
# Questions for TAa
About the data set. We received 2.5GB of html files but is there a certain systematic in them? Is it possible to find the html files in thoses files with the url or do we have to go online to extract the data? 