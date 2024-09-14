from main import load_dataset, get_mean, get_median, get_std, save_to_md, create_boxplot

import numpy as np
import pandas as pd

data = "https://raw.githubusercontent.com/anlane611/datasets/main/population.csv"
dataframe = load_dataset(data)
df_y = dataframe["Y"]

print(df_y)

# Print descriptive statistics
print(df_y.describe())


# Define test functions
def test_mean():
    """Test the get_mean function"""
    assert get_mean(df_y) == round(np.mean(df_y), 3)


def test_median():
    """Test the get_median function"""
    assert get_median(df_y) == round(np.median(df_y), 3)


def test_std():
    """Test the get_std function"""
    assert get_std(df_y) == round(np.std(df_y), 3)


if __name__ == "__main__":
    test_mean()
    test_median()
    test_std()
    create_boxplot(df_y, "boxplot.png")
    mean_y = get_mean(df_y)
    median_y = get_median(df_y)
    std_y = get_std(df_y)
    save_to_md(mean_y, median_y, std_y)
