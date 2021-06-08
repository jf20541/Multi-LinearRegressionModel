import pandas as pd
import config
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm


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
        vif = [variance_inflation_factor(X.iloc[:, variables].values, ix)
               for ix in range(X.iloc[:, variables].shape[1])]

        maxloc = vif.index(max(vif))
        thresh=5.0
        if max(vif) > thresh:
            print('Dropped ' + X.iloc[:, variables].columns[maxloc])
            del variables[maxloc]
            dropped = True
    print(X.columns[variables])

if __name__ == '__main__':
    # import dataset, define IV's and DV
    # VIF expects a constant, add constant
    df = pd.read_csv(config.CLEAN_DATA)
    features = df.drop(['GDP_growth'], axis=1)
    features = sm.tools.add_constant(features)
    print(multicollinearity(features))
    # Index(['Broad_money_growth', 'Gov_consumtion_growth','Gross_capital_formation_growth'],