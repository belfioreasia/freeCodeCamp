# freeCodeCamp Projects
Repository for Code used for various freeCodeCamp courses.


# 1. Data Analysis with Python

View Certificate [here](Certificates/Data_Analysis_with_Python.pdf).

## a. Projects

### i. Mean-Variance-Standard Deviation Calculator
Use Numpy to calculate the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements of given input datasets.

### ii. Demographic Data Analyzer
Analyze demographic data using Pandas of a given dataset of demographic data that extracted from the 1994 Census database. Extract information for the following questions:
- How many people of each race are represented in this dataset? 
- What is the average age of men?
- What is the percentage of people who have a Bachelor's degree?
- What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
- What percentage of people without advanced education make more than 50K?
- What is the minimum number of hours a person works per week?
- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
- What country has the highest percentage of people that earn >50K and what is that percentage?
- Identify the most popular occupation for those who earn >50K in India.

### iii. Medical Data Visualizer
Visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations: the rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. \
Use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

- Determine if a person is overweight, by calculating their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
- Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
- Draw the Categorical Plot.
- Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. 
- Draw the Heat Map.
- Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
    - diastolic pressure is higher than systolic 
    - height is less than the 2.5th percentile
    - height is more than the 97.5th percentile
    - weight is less than the 2.5th percentile
    - weight is more than the 97.5th percentile
- Calculate the correlation matrix and generate a mask for the upper triangle. Plot the correlation matrix using *sns.heatmap()*.

### iv. Page View Time Series Visualizer
Visualize time series data using a line chart, bar chart, and box plots. The dataset contains the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03: understand the patterns in visits and identify yearly and monthly growth.

- Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
- Create a function that uses Matplotlib to draw a line chart that describes the evolution of Daily freeCodeCamp Forum Page Views from 5/2016 to 12/2019.
- Create a function that draws a bar chart that shows average daily page views for each month grouped by year.
- Create a draw_box_plot function that shows how the Page View values are distributed within a given year or month and how it compares over time. 

### v. Sea Level Predictor
Analyze a dataset of the global average sea level change since 1880 and  use the data to predict the sea level change through year 2050.

- Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
- Get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot and predict the sea level rise in 2050.
- Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.


## b. Skills and Tools

The project is written in `python`. The following tools and packages were used to complete the course:

- [**Numpy**](https://numpy.org/doc/stable/index.html): python package for mathematical and scientific computing.

- [**Pandas**](https://pandas.pydata.org/): python package for data analysis, particularly suitable for handling relational and labelled data.

- [**Matplotlib**](https://scikit-learn.org/stable/index.html): python package for data plotting and visualization.

- [**Seaborn**](https://scikit-learn.org/stable/index.html): python package for data plotting and visualization.
