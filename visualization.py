import pandas as pd
import matplotlib.pyplot as plt

def ward_chart():
    df = pd.read_csv("data/admissions.csv",
                     names=["PID", "Ward", "Admit", "Discharge"])
    df["Ward"].value_counts().plot(kind="bar")
    plt.title("Ward Usage")
    plt.show()