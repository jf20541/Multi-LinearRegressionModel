# MultiRegressionModel
ELT (Extract, Load, Transform) pipelines have gained traction since the advent of cloud computing. Which has lowered the cost of storing data and running queries using SQL on large raw data sets. 

### Goal




### Install
This project requires **Python 3.7** and the following Python libraries installed:

- [Pandas](http://pandas.pydata.org)
- [StatsModel](https://www.statsmodels.org/stable/index.html)
- [Scipy](https://www.scipy.org/)
- [Matplotlib](https://matplotlib.org/)


### Code

Created 4 modules (assumptions, model, data plot.py)


### Run

In a terminal or command window, navigate to the top-level project directory `MultiRegressionModel/` (that contains this README) and run one of the following commands:

```bash
pip install --upgrade pip
``` 
```bash
pip install -r requirements.txt
``` 

### Data

Data collected from the [WORLD BANK](https://data.worldbank.org/) with the following variables
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

**Selected Variables**
- `Broad_money_growth (Annual %)`: Measures economy's money supply (cash and other assets easily liquidated)
- `Gov_consumtion_growth (Annual % growth)`: Aggregate transaction on a national income representing government expenditure on goods&services
- `Gross_capital_formation_growth (% of GDP)`: Measured by the total value of the gross fixed capital formation
- `Hh_consumption_growth (Annual % Growth)`: Value of all goods&services, purchased by households.
- `Pop_growth (Annual %)`: Increase in the number of individuals in a population
