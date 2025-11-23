import pingouin as pg
import pandas as pd 
import numpy as np
from statsmodels.stats.power import TTestIndPower
from sklearn.linear_model import LinearRegression

def information(df):
    columns = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    summary = df[columns].agg(['mean', 'median', 'min', 'max'])
    return summary





def smoker_power_analysis(df):
    """Utför en power-analys för skillnaden i systoliskt blodtryck mellan rökare
    och icke-rökare baserat på observerad effektstorlek."""
    smokers = df[df["smoker"] == "Yes"]["systolic_bp"]
    non_smokers = df[df["smoker"] == "No"]["systolic_bp"]

   
    d = pg.compute_effsize(smokers, non_smokers, eftype="cohen")

    
    analysis = TTestIndPower()
    n1 = len(smokers)
    n2 = len(non_smokers)
    ratio = n2 / n1

    power = analysis.power(effect_size=d, nobs1=n1, alpha=0.05, ratio=ratio)

    return f"power : {power}"



def linear_model(df, parameters):
    """Anpassar en linjär regressionsmodell för att förutsäga systoliskt blodtryck."""
    x = df[parameters].values
    y = df["systolic_bp"].values

    linreg = LinearRegression()
    linreg.fit(x, y)

    intercept = float(linreg.intercept_)
    slope = float(linreg.coef_[0])
    r2 = float(linreg.score(x, y))

    print(f"intercept: {intercept:.3f}")
    print(f"slope (weight): {slope:.3f}")
    print(f"R²: {r2:.3f}")

    return linreg, x, y, r2