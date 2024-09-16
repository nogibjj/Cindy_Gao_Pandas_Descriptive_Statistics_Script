import matplotlib.pyplot as plt
import pandas as pd


# read dataset from csv file
def load_dataset(dataset):
    df = pd.read_csv(dataset)
    return df


# calculate the mean of variable:
def get_mean(df, var):
    mean_var = df[var].mean()
    return mean_var


# calculate the median of variable:
def get_median(df, var):
    median_var = df[var].median()
    return median_var


# calculate the standard deviation of variable:
def get_std(df, var):
    std_var = df[var].std()
    return std_var


# data visualization: boxplot for variable Y
def create_boxplot(script, filename="Boxplot.png"):
    plt.boxplot(script)
    plt.xlabel("variable_Y")
    plt.ylabel("values")
    plt.title("Visualization for Boxplot of variable_Y")
    plt.savefig(filename)
    plt.show()


# create the summary markdown
def save_to_md(mean_y, median_y, std_y):
    with open("boxplot.md", "a", encoding="utf-8") as file:  # Specify encoding
        file.write("# Markdown for the boxplot of variable Y\n")
        file.write("![Figure](boxplot.png)\n")
        file.write(f"\n**Mean**: {mean_y}\n")
        file.write(f"**Median**: {median_y}\n")
        file.write(f"**Standard Deviation**: {std_y}\n")
