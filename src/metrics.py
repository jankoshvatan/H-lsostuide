
import pandas as pd 
import numpy as np
from scipy import stats
import pingouin as pg
from statsmodels.stats.power import TTestIndPower
from sklearn.linear_model import LinearRegression

def information(df):
    """Returnerar medelvärde, median, min och max för utvalda kolumner."""
    columns = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    summary = df[columns].agg(['mean', 'median', 'min', 'max'])
    return summary





def smoker_power_analysis(df):
    """Beräknar power för skillnaden i systoliskt blodtryck mellan rökare och icke-rökare."""
    smokers = df[df["smoker"] == "Yes"]["systolic_bp"]
    non_smokers = df[df["smoker"] == "No"]["systolic_bp"]

   
    d = pg.compute_effsize(smokers, non_smokers, eftype="cohen")

    
    analysis = TTestIndPower()
    n1 = len(smokers)
    n2 = len(non_smokers)
    ratio = n2 / n1

    power = analysis.power(effect_size=d, nobs1=n1, alpha=0.05, ratio=ratio)

    return f"power : {power:.3f}"



def linear_model(df, parameters):
    """Anpassar en linjär regressionsmodell för att förutsäga systoliskt blodtryck."""
    x = df[parameters].values
    y = df["systolic_bp"].values

    linreg = LinearRegression()
    linreg.fit(x, y)

    intercept = float(linreg.intercept_)
    slopes = linreg.coef_.astype(float)
    r2 = float(linreg.score(x, y))

    print(f"intercept: {intercept:.3f}")
    print("Slopes:")

    for param, slope in zip(parameters, slopes):
        print(f"  {param}: {slope:.3f}")

    print(f"R²: {r2:.3f}")

    return linreg, x, y, r2



def run_power_simulation(df, effect_list=[0,1,2,3,4,5], iters=2000, alpha=0.05):
    """Simulerar power för olika möjliga blodtrycksskillnader mellan rökare och icke-rökare."""
    smokers = df[df["smoker"] == "Yes"]["systolic_bp"].dropna().values
    nonsmokers = df[df["smoker"] == "No"]["systolic_bp"].dropna().values

    n_s  = len(smokers)
    n_ns = len(nonsmokers)

    var_s  = np.var(smokers, ddof=1)
    var_ns = np.var(nonsmokers, ddof=1)

    print("Antal rökare:", n_s)
    print("Antal icke-rökare:", n_ns)

    def estimate_power(effect_mmHg):
        rng = np.random.default_rng()
        sig = 0
        base_mean = np.mean(nonsmokers)

        for _ in range(iters):
            sim_ns = rng.normal(loc=base_mean,           scale=np.sqrt(var_ns), size=n_ns)
            sim_s  = rng.normal(loc=base_mean+effect_mmHg, scale=np.sqrt(var_s),  size=n_s)

            t_stat, p_val = stats.ttest_ind(
                sim_s, sim_ns, equal_var=False, alternative="greater"
            )

            if p_val < alpha:
                sig += 1

        return sig / iters

    results = {e: estimate_power(e) for e in effect_list}

    for e, p in results.items():
        print(f"Sann skillnad = {e:>2} mmHg  ->  power ≈ {p:.3f}")

  