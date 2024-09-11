"""Requirements:

Python script using Pandas for descriptive statistics
Read a dataset (CSV or Excel)
Generate summary statistics (mean, median, standard deviation)
Create at least one data visualization
Deliverable:

Python script
Generated summary report (PDF or markdown)"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from ydata_profiling import ProfileReport


df = pd.read_csv(
    "https://raw.githubusercontent.com/anlane611/datasets/main/population.csv"
)

df_y = df["Y"]
print(df_y)


# calculate the mean of variable Y:
def get_mean(script):
    sum_script = 0
    for i in range(len(script)):
        sum_script += script[i]

    mean_script = sum_script / len(script)
    return round(mean_script, 3)


print(get_mean(df_y))


# calculate the median of variable Y:
def get_median(script):
    sorted_script = np.sort(script)
    num = len(sorted_script)
    if num % 2 == 0:
        median_script = (sorted_script[num // 2] + sorted_script[num // 2 + 1]) / 2
    else:
        median_script = sorted_script[np.ceil(num / 2)]
    return round(median_script, 3)


print(get_median(df_y))


# calculate the standard deviation of variable Y:
def get_std(script):
    num = len(script)
    mean_s = np.mean(script)
    sum_error = 0
    for i in range(num):
        sum_error += (mean_s - script[i]) ** 2
    std_script = np.sqrt(sum_error / (num - 1))
    return round(std_script, 3)


print(get_std(df_y))


# data visualization: boxplot for variable Y"
plt.boxplot(df_y)
plt.xlabel("variable_Y")
plt.ylabel("values")
plt.title("Visualization for Boxplot of variable_Y")
plt.show()


# create summary report pdf
def create_pdf(csv):
    """generates report of any dataset"""
    df_to_generate = pd.read_csv(csv)
    profile = ProfileReport(df_to_generate, title="Population Summary Report")
    profile.to_file("summary_report.html")
