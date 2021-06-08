import pandas as pd
import config
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_data(x):
    x.boxplot(column=['Broad_money_growth', 'Gov_consumtion_growth','Gross_capital_formation_growth', 'Hh_consumption_growth'])
    plt.title('Box PLot Features')
    plt.show()

def zscore(x):
    # finding outliers 3-SD from mean 
    outliers = x[(np.abs(stats.zscore(x)) < 3).all(axis=1)]
    print(x.index.difference(outliers.index))

if __name__ == '__main__':
    df = pd.read_csv(config.CLEAN_DATA)
    X = df[['Broad_money_growth', 'Gov_consumtion_growth','Gross_capital_formation_growth', 'Hh_consumption_growth']]
    plot_data(X)
    zscore(X)
    # Index([1998, 2001]
    # 1998: During the Asian-financial crisis (financial contagion)
    # 2001: Slowing global economy
    