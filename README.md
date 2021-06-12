# MultiRegressionModel

## Objective
Multiple Regression Model is the relationship between multiple independent variables to a dependent variable\
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20Y_%7Bi%7D%20%3D%20%5Cbeta%20_%7B0%7D%20&plus;%20%5Cbeta%20_%7B1%7DX_%7B1%2C%20i%7D%20&plus;%20...%20&plus;%20%5Cbeta%20_%7Bk%7DX_%7Bk%2C%20i%7D%20&plus;%20%5Cepsilon%20_%7Bi%7D%2C%20i%3D1%2C...%2Cn)\
Metrics: Adjusted R-Square is used to explain the degree to which predictor variables explain the variation of dependent variable while penalizing an increase of independent varibles\

Assumptions: Variance Inflation Factor, Breusch–Pagan, Ljung-Box, Anderson-Darling Test

### Output 
```bash
                            OLS Regression Results                            
==============================================================================
Dep. Variable:             GDP_growth   R-squared:                       0.892
Model:                            OLS   Adj. R-squared:                  0.880
Method:                 Least Squares   F-statistic:                     71.08
Date:                Thu, 10 Jun 2021   Prob (F-statistic):           1.13e-19
Time:                        11:48:40   Log-Likelihood:                -84.898
No. Observations:                  49   AIC:                             181.8
Df Residuals:                      43   BIC:                             193.1
Df Model:                           5                                         
``` 
### Target
- `GDP_growth (Annual %)`: Rate compares the year-over-year change in a country's economic output
- GDP = Consumption + Investment + Government Spending + Net Exports

### Selected Variables
- `Broad_money_growth (Annual %)`: Measures economy's money supply (cash and other assets easily liquidated)
- `Gov_consumtion_growth (Annual % growth)`: Aggregate transaction on a national income representing government expenditure on goods&services
- `Gross_capital_formation_growth (% of GDP)`: Measured by the total value of the gross fixed capital formation
- `Hh_consumption_growth (Annual % Growth)`: Value of all goods&services, purchased by households.
- `Pop_growth (Annual %)`: Increase in the number of individuals in a population

### Code
Created 4 modules
- `assumptions.py`: Variance Inflation Factor, Breusch–Pagan, Ljung-Box, Anderson-Darling Test
- `main.py`: Used OLS Multi Regression Model and loaded to parameters to pickle file
- `data.py`: Cleaned xlsx file and covert to pandas DataFrame
- `plot.py`: Plot Variance Inflation Factor, Breusch–Pagan, Ljung-Box, Anderson-Darling Test Assumptions

### Install
- [Pandas](http://pandas.pydata.org)
- [StatsModel](https://www.statsmodels.org/stable/index.html)
- [Scipy](https://www.scipy.org/)
- [Matplotlib](https://matplotlib.org/)

### Run
In a terminal or command window, navigate to the top-level project directory `MultiRegressionModel/` and run one of the following command:
```bash
pip install --upgrade pip && pip install -r requirements.txt
``` 

### Data
Features collected from [WORLD BANK](https://data.worldbank.org/)
- GDP_growth
- Gross_capital
- Pop_growth
- Birth_rate
- Broad_money_growth
- Final_consumption_gdp
- Gov_consumtion_growth
- Gross_capital_formation_growth
- Hh_consumption_growth
- Unemployment

## Sources
