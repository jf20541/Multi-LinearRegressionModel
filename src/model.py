import pandas as pd
import config
import statsmodels.api as sm
import pickle


def deploy_model(data):
    """
    Parameters: define DV and selected IV's after assumptions
    Return: summary of model 
    """
    target = data['GDP_growth']
    new_features = data[['Broad_money_growth', 'Gov_consumtion_growth','Gross_capital_formation_growth', 'Hh_consumption_growth', 'Pop_growth']]
    new_features = sm.add_constant(new_features)
    model = sm.OLS(target,new_features)
    est = model.fit()

    # save model
    with open(config.MODEL,'wb') as f:
        pickle.dump(model, f)
    return est.summary()

if __name__ == '__main__':
    df = pd.DataFrame(pd.read_excel(config.TRAINING_FILE))
    print(deploy_model(df))