import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from scipy.stats import ttest_ind

class HealthPlot:
    def __init__(self, df):
        self.df = df

    @property
    def df(self):
        return self.__df

    @df.setter
    def df(self, df):
        self.__df = df.copy()

    def hist_bloodpressure(self) -> None:
        df = self.df
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(df["systolic_bp"].dropna(), bins=30, edgecolor="black")
        ax.set_xlabel("Systolic Blood Pressure")
        ax.set_ylabel("Frequency")
        ax.set_title("Histogram of Systolic Blood Pressure")
        plt.show()

    def box_weight_sex(self) -> None:
        df = self.df
        fig, ax = plt.subplots(figsize=(8, 4))
        sexes = df["sex"].unique()
        groups = [df[df["sex"] == sex]["weight"].dropna() for sex in sexes]
        ax.boxplot(groups, labels=sexes)
        ax.set_title("Boxplot of Weight by Sex")
        ax.set_xlabel("Sex")
        ax.set_ylabel("Weight")
        plt.show()

    def bar_smokers(self) -> None:
        df = self.df
        fig, ax = plt.subplots(figsize=(8, 4))
        smoker_counts = df["smoker"].value_counts(normalize=True)
        ax.bar(smoker_counts.index, smoker_counts.values, edgecolor="black")
        ax.set_title("Proportion of Smokers")
        ax.set_xlabel("Smoker")
        ax.set_ylabel("Proportion")
        plt.show()