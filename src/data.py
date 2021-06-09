import pandas as pd
import config


def clean_data(data):
    """
    Clean xlsx file, set index, replace NaN values, set data type
    Parameters: data as pandas dataframe
    Returns: clean dataset and convert to csv file
    """
    data = data.set_index("Year")
    data = data.astype(float)

    if data.isnull().values.any() == False:
        print("No Null-Values found")
    else:
        print("Null-Values found and fillna")

    data.to_csv(config.CLEAN_DATA, index_label=False)


if __name__ == "__main__":
    df = pd.DataFrame(pd.read_excel(config.TRAINING_FILE))
    clean_data(df)
