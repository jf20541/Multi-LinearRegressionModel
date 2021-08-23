import pandas as pd
import MR_config
import statsmodels.api as sm
import pickle


def deploy_model(data):
    """Deploying Mult-Reg Summry
    Args:
        data ([dataframe]): define DV and selected IV's after assumptions
    Returns:
        [object]: summary of model
    """
    target = data["GDP_growth"]
    new_features = data[
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

    # save model
    with open(MR_config.MODEL, "wb") as f:
        pickle.dump(model, f)
    return est.summary()


if __name__ == "__main__":
    df = pd.DataFrame(pd.read_excel(MR_config.TRAINING_FILE))
    print(deploy_model(df))
