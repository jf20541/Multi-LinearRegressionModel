import pandas as pd
import MR_config


def clean_data(data):
    """Clean xlsx file, set index, replace NaN values,
        convert to csv file
    Args:
        data [float]: set data as pandas dataframe
    """
    data = data.set_index("Year")
    data = data.astype(float)

    if data.isnull().values.any() == False:
        data.to_csv(MR_config.CLEAN_DATA, index_label=False)
        print("No Null-Values found")
    else:
        print("Null-Values found and fillna")


if __name__ == "__main__":
    df = pd.DataFrame(pd.read_excel(MR_config.TRAINING_FILE))
    clean_data(df)
