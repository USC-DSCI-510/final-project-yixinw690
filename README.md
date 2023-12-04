[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/h_LXMCrc)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12785817&assignment_repo_type=AssignmentRepo)
# DSCI 510 Final Project
Discover the Restaurant Diversity in Boston

## Team Members 
Yixin Wang & Yiqian Zheng

## Instructions to create a conda enviornment
For macOS and Linux, you can just open the regular terminal.
```
conda create -n income_cuisine_analysis python=3.8
```
This command creates a new conda environment named income_cuisine_analysis with Python 3.8 installed. You can replace 3.8 with any version of Python that you need for your project.
## Instructions on how to install the required libraries
The libraries used in our project include requests, pandas, seaborn, and matplotlib. Install the libraries by running following command in your terminal:
```
pip install -r requirements.txt
```
## Instructions on how to download the data
Run the code in get_data.py to download the cuisine type and zip code data of 1000 randomly selected restaurants from Yelp API, and income data of 31 zip codes in Boston Metropolitan area from Census Bureau API. API keys are included in the code. 2 csv files named " restaurants_in_boston.csv" and " census_income_data_acs_boston.csv" will be downloaded.
* Yelp API generates different sets of 1000 restaurants every time you try a new API requests due to the API restriction, which might leads to statistical results that's slightly different from the statistics in our report (this doesn't impact the general trends in the correlation and descriptive analysis). So please use the file in "processed data" to conduct analysis in order to match the numbers in our report. 
## Instructions on how to clean the data
Run the code in clean_data.py to conduct data cleaning. 
* For the restaurants data, 3 csv files will be downloaded in 3 steps.
  - Firstly, remove restaurants without cuisine tags.
  - Secondly, relabel the restaurants' cuisine types. (e.g. American includes New American, American, Hawaiian, and Southern) 
  - Lastly, remove the restaurants that are not in the Boston Metropolitan zip codes, and remove the original cuisine labels column as well.
* So the final restaurants data csv used for analysis is called "filtered_restaurants_without_cuisine_types.csv".
* For the income data, we summarized the original 10 brackets into 6 bracktes, and created the new table called "census_income_data_acs_boston_cleaned_combined_reordered.csv" 
## Instrucions on how to run analysis code
Run the code in run_analysis.py to get all the visualizations and statistics, including a correlation analysis and a descriptive analysis of the data. 
* In the analysis process, a seperate csv file called "restaurant_count.csv" is created from "filtered_restaurants_without_cuisine_types.csv" for analysis. This step is not considered as part of the data cleaning because the generation of this file is only used for the correlation analysis. 
## Instructions on how to create visualizations
Run the code in visualize_results.py to get graphs of our analysis. The only difference between the analysis code and visualization code is the analysis code generate some descriptive statistics results of our analysis. 
