from main import get_mean, get_median, get_std
import numpy as np
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/anlane611/datasets/main/population.csv"
)

df_y = df["Y"]


def test_mean():
    """testing out get_mean function"""
    assert get_mean(df_y) == round(np.mean(df_y), 3)


def test_median():
    """testing out get_median function"""
    assert get_median(df_y) == round(np.median(df_y), 3)


def test_std():
    """testing out get_std function"""
    assert get_std(df_y) == round(np.std(df_y), 3)


if __name__ == "__main__":
    test_mean()
    test_median()
    test_std()
