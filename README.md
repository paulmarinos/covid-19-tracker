# covid-19

view covid-19 data by state or date and perform simple regression analysis

## Problem Statement:

How effective has each U.S. state been at treating patients diagnosed with the coronavirus? This question is important because each state has different resources and receives varying levels of government funding. If more people in one state recover from the illness compared to the people living in another state, studying the variables that might have led to this has the potential to increase the nationwide recovery rate. There are many variables that would contribute to state recovery rate, like population density, number of hospitals, number of resources, government funding, geographical features, average diet, average level of physical exercise, and so on. It will be important to study these factors. However, the first step is to study the number of cases and deaths by state over time.

## Objectives: 

Analyze the number of COVID-19 cases and deaths by U.S. state over time
Calculate COVID-19 state mortality rate
Create a tool that will quickly visualize the data using tables and charts
Allow user to search by either state or date and sort data by column
Allow user to plot the data and fit a linear regression model
Calculate the R-squared value

## Libraries used:

- pandas for data preparation
- numpy for data manipulation
- matplotlib for data visualization
- sklearn for statistical modeling

## R-squared value meaning:

The r-squared value, or correlation of determination, explains how closely correlated the dependent value (cases) is with the independent value (deaths). As the number of cases increases, the number of deaths to the virus should increase as well. If the cases and deaths of a state do not have a linear relationship then the way the state is treating patients infected with the disease should be studied.

## Datasource (updated daily):

https://github.com/nytimes/covid-19-data/blob/master/us-states.csv
