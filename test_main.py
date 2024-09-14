from main import load_dataset, get_mean, get_median, get_std, save_to_md, create_boxplot

import numpy as np
import pandas as pd

data = "https://raw.githubusercontent.com/anlane611/datasets/main/population.csv"
dataframe = load_dataset(data)


print(dataframe)

# Print descriptive statistics
print(dataframe.describe())
print(get_mean(dataframe["Y"]))
print(get_median(dataframe["Y"]))
print(get_std(dataframe["Y"]))


# Define test functions
def test_mean():
    """Test the get_mean function"""
    assert get_mean(dataframe["Y"]) == round(np.mean(dataframe["Y"]), 3)
    assert get_mean(dataframe["X1"]) == round(np.mean(dataframe["X1"]), 3)


def test_median():
    """Test the get_median function"""
    assert get_median(dataframe["Y"]) == round(np.median(dataframe["Y"]), 3)
    assert get_median(dataframe["X1"]) == round(np.median(dataframe["X1"]), 3)


def test_std():
    """Test the get_std function"""
    assert get_std(dataframe["Y"]) == round(np.std(dataframe["Y"]), 3)
    assert get_std(dataframe["X2"]) == round(np.std(dataframe["X2"]), 3)


if __name__ == "__main__":
    test_mean()
    test_median()
    test_std()
    create_boxplot(dataframe["Y"], "boxplot.png")
    mean_y = get_mean(dataframe["Y"])
    median_y = get_median(dataframe["Y"])
    std_y = get_std(dataframe["Y"])
    save_to_md(mean_y, median_y, std_y)
