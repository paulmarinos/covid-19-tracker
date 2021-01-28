# covid-19

view covid-19 data by U.S. state or date and perform a simple linear regression analysis.

## Problem Statement:

How effective has each U.S. state been at treating patients diagnosed with the coronavirus? If more people in one state recover from the illness compared to the people living in another state, studying the variables that might have led to this has the potential to increase the nationwide recovery rate. There are many variables that would contribute to state recovery rate, like population density, number of hospitals, number of resources, government funding, geographical features, average diet, average level of physical exercise, and so on. It may be useful to study these factors, however the first step is to study the number of cases and deaths over time.

## Objectives: 

- Analyze the number of COVID-19 cases and deaths by U.S. state over time
- Calculate COVID-19 mortality rate by state
- Create a tool that will quickly visualize the data using tables and charts
- Allow user to search by either state or date and sort data by columns
- Allow user to plot the data and fit a linear regression model
- Calculate R-squared value

## Libraries used:

- pandas for data preparation
- numpy for data manipulation
- matplotlib for data visualization
- sklearn for statistical modeling

## R-squared value meaning:

The Rsquared value, or correlation of determination, explains how closely correlated the dependent value (cases) is with the independent value (deaths). As the number of cases increases, the number of deaths to the virus should increase as well. It may be useful to study how linear this relationship is.

## Datasource (updated daily):

https://github.com/nytimes/covid-19-data/blob/master/us-states.csv
