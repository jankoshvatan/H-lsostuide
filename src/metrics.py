def information(df):
    columns = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    summary = df[columns].agg(['mean', 'median', 'min', 'max'])
    return summary