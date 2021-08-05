# MultiRegressionModel

## Objective
Find the relationship between multiple independent variables to a dependent variable (GDP Growth %).\
GDP = Consumption + Investment + Government Spending + Net Exports
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20Y_%7Bi%7D%20%3D%20%5Cbeta%20_%7B0%7D%20&plus;%20%5Cbeta%20_%7B1%7DX_%7B1%2C%20i%7D%20&plus;%20...%20&plus;%20%5Cbeta%20_%7Bk%7DX_%7Bk%2C%20i%7D%20&plus;%20%5Cepsilon%20_%7Bi%7D%2C%20i%3D1%2C...%2Cn)\
**Metrics:** Adjusted R-Square is used to explain the degree to which predictor variables explain the variation of dependent variable while penalizing an increase of independent varibles

**Assumptions:** Variance Inflation Factor, Breusch–Pagan, Ljung-Box, Anderson-Darling Test\

## Repository File Structure
    ├── src          
    │   ├── main.py              # Multi Regression Model and loaded to parameters to pickle file
    │   ├── assumptions.py       # Variance Inflation Factor, Breusch–Pagan, Ljung-Box, Anderson-Darling Test
    │   ├── data.py              # Cleaned xlsx file and covert to pandas DataFrame
    │   ├── plot.py              # Plot Variance Inflation Factor, Breusch–Pagan, Ljung-Box, Anderson-Darling Test Assumptionss
    │   └── config.py            # Define path as global variable
    ├── inputs
    │   ├── clean_data.csv       # Cleaned file
    │   └── korea_data.xlsx      # Korea Economic data
    ├── plot
    │   ├── Autocorrelation.png  # Autocorrelation on data
    │   ├── BoxPlot.png          # Boxplot Features
    │   └── ResidualMean.png     # Residual Mean
    ├── requierments.txt         # Packages used for project
    └── README.md

## Output 
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


## Data
Features collected from [WORLD BANK](https://data.worldbank.org/)
```
Target 
- GDP_growth (Annual %): Rate compares the year-over-year change in a country's economic output

Features
- Pop_growth (Annual %): Increase in the number of individuals in a population
- Broad_money_growth (Annual %): Measures economy's money supply (cash and other assets easily liquidated)
- Gov_consumtion_growth (Annual % growth): Aggregate transaction on a national income representing government expenditure on goods&services
- Gross_capital_formation_growth (% of GDP): Measured by the total value of the gross fixed capital formation
- Hh_consumption_growth (Annual % Growth): Value of all goods&services, purchased by households.
```

# LinearRegressionAssets

## Objective
Linear Regression Model is the relationship between an independent variable (MSFT) to a dependent variable (SPY). Calculate the beta coefficient to measure the volatility of an individual stock compared to the systematic risk of the entire market.\
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20Y_%7Bi%7D%20%3D%20%5Cbeta%20_%7B0%7D%20&plus;%20%5Cbeta%20_%7B1%7DX_%7Bi%7D%20&plus;%20%5Cepsilon_%7Bi%7D)

Metrics: R-Square measure the proportion of the variance for a dependent variable that's explained by an independent variable in a regression model\
Metrics: Mean Sqaured Error and Mean Absolute Error

Assumptions:\
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20%5Cepsilon%20_%7Bi%7D%20%5Csim%20N%280%2C%20%5Csigma%20_%7B%5Cepsilon%20%7D%5E%7B2%7D%29)

## Output 
```bash
Slope: 1.47 and Intercept: 78.83

MSE 9.14e+02
MAE 25.8
RMSE 30.2
R2: 0.87
```
```
Target
- S&P500 Index Fund: Index of 500 of the largest companies listed on US stock exchanges (Adjusted-Closing Price)

Feature
- Microsoft (MSFT): Adjusted-Closing Price
```

## Repository File Structure
    ├── src          
    │   ├── main.py              # Initiating Linear Regression Model
    │   ├── metrics.py           # Calculating metrics (R-Squared, MSE, MAE) 
    │   ├── data.py              # Extracted Adj-Closing price from YFinance
    │   └── config.py            # Define path as global variable
    ├── inputs
    │   └── train.csv            # Adj-Closing Price for MSFT and SPY 
    ├── requierments.txt         # Packages used for project
    └── README.md

