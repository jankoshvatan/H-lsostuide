import pandas as pd

REQURED = [
    'id', 'age', 'sex', 'height', 
        'weight', 'systolic_bp', 'cholesterol',
       'smoker', 'disease']

def load_csv(path: str) -> pd.DataFrame:

    df = pd.read_csv(path)

    missing = [i for i in REQURED if i not in df.columns]

    return df

def coerce_numeric(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for c in ["id", "age", "height", "weight", "systolic_bp", "cholesterol", "disease"]:
        out[c] = pd.to_numeric(out[c], errors="coerce")
    return out


