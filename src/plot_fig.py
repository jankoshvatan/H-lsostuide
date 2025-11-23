import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def hist_bloodpresure(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(df["systolic_bp"].dropna(), bins=30, edgecolor="black")
    ax.set_xlabel("Systolic Blood Pressure")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Systolic Blood Pressure")
    plt.show()

def box_weight_sex(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    sexes = df["sex"].unique()
    groups = [df[df["sex"] == sex]["weight"].dropna() for sex in sexes]
    ax.boxplot(groups, labels=sexes)
    ax.set_title("Boxplot of Weight by Sex")
    ax.set_xlabel("Sex")
    ax.set_ylabel("Weight")
    plt.show()

def bar_smokers(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    smoker_counts = df["smoker"].value_counts(normalize=True)
    ax.bar(smoker_counts.index, smoker_counts.values, edgecolor="black")
    ax.set_title("Proportion of Smokers")
    ax.set_xlabel("Smoker")
    ax.set_ylabel("Proportion")
    plt.show()


def plot_regression(x, y, linreg) -> None:
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=0.7, label="Data", color="blue")
    x_line = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
    y_line = linreg.predict(x_line)
    plt.plot(x_line, y_line, color="black", label="Regression")
    plt.xlabel("Age")
    plt.ylabel("Systolic Blood Pressure")
    plt.title("Linear Regression: Systolic BP vs Age")
    plt.legend()
    plt.grid(True)
    plt.show()