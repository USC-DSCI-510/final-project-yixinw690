[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/h_LXMCrc)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12785817&assignment_repo_type=AssignmentRepo)
# DSCI 510 Final Project
Discover the Restaurant Diversity in Boston

## Team Members 
Yixin Wang & Yiqian Zheng

## Instructions to create a conda enviornment

## Instructions on how to install the required libraries

## Instructions on how to download the data
Run the code in get_data.py to download the restaurant data and income data from Yelp API and Census Bureau API. API keys are included in the code. 2 csv files named " restaurants_in_boston.csv" and " census_income_data_acs_boston.csv" will be downloaded.
## Instructions on how to clean the data
Run the code in clean_data.py to conduct data cleaning. 
* For the restaurants data, 3 csv files will be downloaded in 3 steps. In step 1, " cleaned_restaurants_in_boston.csv" is downloaded to remove restaurants without cuisine tags. Then, this file is used to relabel the restaurants' cuisine types, written into the new file "updated_cleaned_restaurants_in_boston.csv"; Lastly, "updated_cleaned_restaurants_in_boston.csv" is used to remove the restaurants that are not in the Boston Metropolitan zip codes, and remove the original cuisine labels column as well. So the final csv used for analysis is called "filtered_restaurants_without_cuisine_types.csv".
* For the income data, we summarized the original 10 brackets into 6 bracktes, and created the new table called "census_income_data_acs_boston_cleaned_combined_reordered.csv" 
## Instrucions on how to run analysis code

## Instructions on how to create visualizations
