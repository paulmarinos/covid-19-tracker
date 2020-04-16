'''
author:  paul marinos
contact: paul.marinos@baruch.cuny.edu
datasource: https://github.com/nytimes/covid-19-data/blob/master/us-states.csv
last updated: 2020-04-07
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('covid - states.csv')
df = df[['date', 'state', 'cases', 'deaths']]
df['mort rate'] = df.deaths / df.cases * 100


def filter_state(df):
	state = input('State: ')
	is_state = (df['state'] == state)
	df = df[is_state]
	print('\n', df, '\n')
	sort_by_column(df)

def filter_date(df):
	date = input('Date (YYYY-MM-DD): ')
	is_date = (df['date'] == date)
	df = df[is_date]
	print('\n', df, '\n')
	sort_by_column(df)

def sort_by_column(df):
	sort_column = input ('Sort by column: ')
	df = df.sort_values(by=[sort_column])
	print ('\n', df, '\n')

def plot_regression(df):
	state = input('State: ')
	is_state = (df['state'] == state)
	df = df[is_state]

	X = df['cases'].values.reshape(-1, 1)  
	Y = df['deaths'].values.reshape(-1, 1)  
	linear_regressor = LinearRegression()
	linear_regressor.fit(X, Y)
	Y_pred = linear_regressor.predict(X)
	print('R-squared: %.2f' % r2_score(X, Y))
	plt.scatter(X, Y)
	plt.plot(X, Y_pred, color = 'red')
	plt.title(state + ' Covid-19 Cases')
	plt.xlabel('cases')
	plt.ylabel('deaths')
	plt.show()

def options():
	print('\n1 - View State')
	print('2 - View Date')
	print('3 - Regression')
	choice = int(input('\nInput: '))
	if (choice == 1):
		filter_state(df)
	elif (choice == 2):
		filter_date(df)
	elif (choice == 3):
		plot_regression(df)
	else:
		print ('Error: Invalid Input')
		options()

def main():	
	options()

main()	




