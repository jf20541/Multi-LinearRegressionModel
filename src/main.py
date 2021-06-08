import pandas as pd
import numpy as np
import config
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan, acorr_ljungbox
from statsmodels.stats.stattools import durbin_watson
import matplotlib.pyplot as plt


df = pd.read_csv(config.CLEAN_DATA)
target = df['GDP_growth']
features = df[['Broad_money_growth', 'Gov_consumtion_growth','Gross_capital_formation_growth']]
features = sm.add_constant(features)
model = sm.OLS(target,features)
est = model.fit()

def breusch_pagan():
    """
    H0: feature's variance for the errors are equal
    HA: feature's varaince are not equal 
    """
    lm, lm_pvalue, fvalue, f_pvalue = het_breuschpagan(est.resid, est.model.exog)
    print(lm_pvalue, f_pvalue)

    if lm_pvalue > 0.05:
        print(f"The p-value was {lm_pvalue}, FTR H0: No Heterosecdasticity ")
    else:
        print(f"The p-value was {lm_pvalue:.4}, Reject H0: There is Heterosecdasticity")

def autocorrelation():
    """
    H0: autocorrelation up to lag_k are all 0 
    HA: autocorrelation of one or more lags differ from 0 
    """
    lag = min(10, (len(X)//3))
    test_results = acorr_ljungbox(est.resid, lags = lag)
    ibvalue, p_val = test_results

    if min(p_val) > 0.05:
        print(f"The lowest p-value found was {min(p_val):.4}, FTR H0: No Autocorrelation")
    else:
        print(f"The lowest p-value found was {min(p_val):.4}, Reject H0: There is Autocorrelation")

    # plot autocorrelation
    sm.graphics.tsa.plot_acf(est.resid)
    plt.show()


if __name__ == '__main__':
    breusch_pagan()
