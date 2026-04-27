import pandas as pd

def total_patients():
    df = pd.read_csv("data/patients.csv",
                     names=["ID", "Name", "Age", "Gender"])
    print("Total Patients:", len(df))

def ward_usage():
    df = pd.read_csv("data/admissions.csv",
                     names=["PID", "Ward", "Admit", "Discharge"])
    print(df["Ward"].value_counts())