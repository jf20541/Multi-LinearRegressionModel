import pandas as pd
import MR_config
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan, acorr_ljungbox, normal_ad
from statsmodels.stats.outliers_influence import variance_inflation_factor

"""
Variance Inflation Factor Test for Mlticollinearity
Breusch–Pagan Test for residuals homoscedastic
Ljung-Box Test for Autocorrelation presence 
Anderson-Darling test for normal distribution
"""


def multicollinearity(X):
    """
    Multicollinearity
    ------------------
    Find variables in the dataset that are correlated.
    Goal: each variables be independent from each other
    """
    variables = list(range(X.shape[1]))
    dropped = True
    while dropped:
        dropped = False
        vif = [
            variance_inflation_factor(X.iloc[:, variables].values, ix)
            for ix in range(X.iloc[:, variables].shape[1])
        ]

        maxloc = vif.index(max(vif))
        thresh = 5.0
        if max(vif) > thresh:
            print("Dropped " + X.iloc[:, variables].columns[maxloc])
            del variables[maxloc]
            dropped = True
    print(X.columns[variables])


def breusch_pagan(error, variables):
    """
    Calculating variance residuals for the Breusch–Pagan Test
    H0: feature's variance for the errors are equal
    HA: feature's varaince are not equal
    """
    # lm, lm_pvalue, fvalue, f_pvalue = het_breuschpagan(est.resid, est.model.exog)
    lm, lm_pvalue, fvalue, f_pvalue = het_breuschpagan(error, variables)

    if lm_pvalue > 0.05:
        print(f"P-value was {lm_pvalue:.3}, FTR H0: No Heterosecdasticity ")
    else:
        print(f"P-value was {lm_pvalue:.3}, Reject H0: There is Heterosecdasticity")


def autocorrelation(errors):
    """
    Calculating autocorrelation residuals for the Ljung-Box Test
    H0: autocorrelation up to lag_k are all 0
    HA: autocorrelation of one or more lags differ from 0
    """
    lbvalue, pvalue = acorr_ljungbox(errors)

    if min(pvalue) > 0.05:
        print(f"P-value is {min(pvalue):.3}, FTR H0: No Autocorrelation")
    else:
        print(f"P-value is {min(pvalue):.3}, Reject H0: There is Autocorrelation")


def andersondarling(errors):
    """
    Calculating residuals for the Anderson-Darling Test
    H0: Residuals aren't Normal Distributed
    HA: Residuals are Normal Distributed
    """
    pvalue = normal_ad(errors)[1]
    if pvalue > 0.05:
        print(f"P-value is {pvalue:.3}, FTR H0: Residuals are Normal Distributed")
    else:
        print(f"P-value is {pvalue:.3}, Reject H0: Residuals aren't Normal Distributed")


if __name__ == "__main__":
    df = pd.read_csv(MR_config.CLEAN_DATA)
    target = df["GDP_growth"]
    features = df.drop("GDP_growth", axis=1)
    new_features = df[
        [
            "Broad_money_growth",
            "Gov_consumtion_growth",
            "Gross_capital_formation_growth",
            "Hh_consumption_growth",
            "Pop_growth",
        ]
    ]
    new_features = sm.add_constant(new_features)
    model = sm.OLS(target, new_features)
    est = model.fit()

    multicollinearity(features)
    # Output: Index(['Broad_money_growth', 'Gov_consumtion_growth','Gross_capital_formation_growth', 'Hh_consumption_growth', 'Pop_growth'])
    breusch_pagan(est.resid, est.model.exog)
    autocorrelation(est.resid)
    andersondarling(est.resid)
