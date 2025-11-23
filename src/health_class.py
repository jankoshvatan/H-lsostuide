import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from scipy.stats import ttest_ind
from src.class_plot import HealthPlot

class HealthAnalyser(HealthPlot):
    def __init__(self, df: pd.DataFrame):
        HealthPlot.__init__(self, df)
    
    @property
    def df(self):
        return self.__df
    
    @df.setter
    def df(self, df: pd.DataFrame):
        self.__df = df.copy()
    
    def sim_disease(self):
        df = self.df
        df = df["disease"]
        disease_prop = df.mean()
        sim_disease = np.random.binomial(n=1, p=disease_prop, size=1000)
        sim_prop = sim_disease.mean()

        print(f"Verklig andel: {disease_prop:.3f}")
        print(f"Simulerad andel: {sim_prop:.3f}")
        print(f"Skillnad: {abs(disease_prop - sim_prop):.3f}")

    def connfidence_interval(self, column_name: str):
        sample = self.df[column_name].dropna().to_numpy()
        sample_size = len(sample)
        sample_mean = sample.mean()
        std = std = sample.std(ddof=1)
        confidence = 0.95
        alpha = 1 - 0.95 
        degrees_of_freedom = sample_size - 1

        t_critical = stats.t.ppf(1 - alpha / 2, degrees_of_freedom) 
        sigma = std / math.sqrt(sample_size)
        me = t_critical * sigma 
        t_low = sample_mean - me
        t_high = sample_mean + me

        return f"CL low {t_low:.2f}, CL high {t_high:.2f}"
    
    def blood_pressure_smoker_vs_nonesmoker(self):
        df = self.df
        smokers = df[df["smoker"] =="Yes"]["systolic_bp"]
        none_smokers = df[df["smoker"] =="No"]["systolic_bp"]

        # Welch’s t-test
        t_stat, p_value = ttest_ind(smokers, none_smokers, equal_var=False, alternative="greater")

        return f"t -score {t_stat:.2f}, p value {p_value:.2f}"

