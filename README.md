# DATA WRANGLING

Multiple exercises of data wrangling a JSON file of projects funded by world bank using python.

# Following tasks/exercises are performed using the file world_bank_projects.json

1. Find the 10 countries with most projects
2. Find the top 10 major project themes (using column 'mjtheme_namecode')
3. In 2. above you will notice that some entries have only the code and the name is missing. Create a dataframe with the missing names filled in.

# Approach taken to perform above exercises

# TASK 1: Find the 10 countries with most projects
1. Import required libraries such as Pandas, json and json_normalize - as some of the data in the columns are nested.
2. Load JSON file as dataframe using pandas and inspect the data to get a look at the structure and data expecially the columns are needed for the tasks.
3. Find top 10 countries by using 'value_counts' method on 'countryname' column to get the count of no. of times a country name shas repeated stating no.of projects it has done.

# TASK 2: Find the top 10 major project themes (using column 'mjtheme_namecode')
1. Import required libraries such as Pandas, json and json_normalize - as some of the data in the columns are nested.
2. Load JSON file as a string, flatten it and inspect as the column required to get top 10 project themes is nested. Hence, it has to be normalized.
3. Find top 10 project themes by using 'value_counts' method on 'name'.

# TASK 3: In 2. above you will notice that some entries have only the code and the name is missing. Create a dataframe with the missing names filled in.
1. Import required libraries such as Pandas, json and json_normalize - as some of the data in the columns are nested.
2. Load JSON file as dataframe using pandas and inspect the data to get a look at the structure and data expecially the columns are needed for the tasks.
3. Sort teh dataframe, fill empty values usinf NaN value and then replace them by using forward filling 'ffill'.
