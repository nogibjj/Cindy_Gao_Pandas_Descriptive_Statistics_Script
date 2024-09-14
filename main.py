import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = "https://raw.githubusercontent.com/anlane611/datasets/main/population.csv"


# read dataset from csv file
def load_dataset(dataset):
    df = pd.read_csv(dataset)
    return df


# calculate the mean of variable Y:
def get_mean(script):
    sum_script = 0
    for i in range(len(script)):
        sum_script += script[i]

    mean_script = sum_script / len(script)
    return round(mean_script, 3)


# calculate the median of variable Y:
def get_median(script):
    sorted_script = np.sort(script)
    num = len(sorted_script)
    if num % 2 == 0:
        median_script = (sorted_script[num // 2] + sorted_script[num // 2 + 1]) / 2
    else:
        median_script = sorted_script[np.ceil(num / 2)]
    return round(median_script, 3)


# calculate the standard deviation of variable Y:
def get_std(script):
    num = len(script)
    mean_s = np.mean(script)
    sum_error = 0
    for i in range(num):
        sum_error += (mean_s - script[i]) ** 2
    std_script = np.sqrt(sum_error / (num - 1))
    return round(std_script, 3)


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
