import pandas as pd
import config
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.api as sm


def plot_data(x):
    x.boxplot(column=['Broad_money_growth', 'Gov_consumtion_growth','Gross_capital_formation_growth','Hh_consumption_growth', 'Pop_growth'])
    plt.title('Box PLot Features')
    plt.savefig('../plots/BoxPlot.png')


def zscore(x):
    # finding outliers 3-SD from mean 
    outliers = x[(np.abs(stats.zscore(x)) < 3).all(axis=1)]
    print(x.index.difference(outliers.index))


def autocorrelation(errors):
    # plot autocorrelation
    sm.graphics.tsa.plot_acf(errors.resid)
    plt.savefig('../plots/Autocorrelation.png')


def qqplot(errors):
    # residuals normality
    sm.qqplot(errors, line='s')
    plt.savefig('../plots/ResidualMean.png')


if __name__ == '__main__':
    df = pd.read_csv(config.CLEAN_DATA)
    target = df['GDP_growth']
    X = df[['Broad_money_growth', 'Gov_consumtion_growth','Gross_capital_formation_growth', 'Hh_consumption_growth', 'Pop_growth']]
    features = sm.add_constant(X)
    model = sm.OLS(target,features)
    est = model.fit()

    plot_data(X)
    zscore(X)
    autocorrelation(est)
    qqplot(est.resid)

    # Index([1998, 2001]
    # 1998: During the Asian-financial crisis (financial contagion)
    # 2001: Slowing global economy
    