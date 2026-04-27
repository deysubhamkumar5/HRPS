from models import Patient, Admission, Bill
from storage import save_data, read_data
from utils import validate_age, validate_gender
from analytics import total_patients, ward_usage
from visualization import ward_chart
from datetime import datetime

def register_patient():
    pid = input("ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")

    if not validate_age(age):
        print("Invalid Age")
        return
    if not validate_gender(gender):
        print("Invalid Gender")
        return

    save_data("data/patients.csv", [pid, name, age, gender])
    print("Patient Registered")

def admit_patient():
    pid = input("Enter Patient ID: ")
    ward = input("Ward (General/ICU/Private): ")
    date = datetime.now()

    save_data("data/admissions.csv",
              [pid, ward, date, ""])
    print("Patient Admitted")

def discharge_patient():
    pid = input("Enter Patient ID: ")
    data = read_data("data/admissions.csv")

    for row in data:
        if row[0] == pid and row[3] == "":
            row[3] = str(datetime.now())

    # rewrite file
    import csv
    with open("data/admissions.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("Patient Discharged")

def generate_bill():
    pid = input("Patient ID: ")
    amount = float(input("Enter Amount: "))

    save_data("data/billing.csv", [pid, amount])
    print("Bill Generated")

def search_patient():
    pid = input("Enter ID: ")
    data = read_data("data/patients.csv")

    for row in data:
        if row[0] == pid:
            print("Found:", row)
            return
    print("Not Found")

def main():
    while True:
        print("\n--- HPRS FULL SYSTEM ---")
        print("1. Register Patient")
        print("2. Admit Patient")
        print("3. Discharge Patient")
        print("4. Generate Bill")
        print("5. Search Patient")
        print("6. Analytics")
        print("7. Graph")
        print("8. Exit")

        ch = input("Choice: ")

        if ch == "1":
            register_patient()
        elif ch == "2":
            admit_patient()
        elif ch == "3":
            discharge_patient()
        elif ch == "4":
            generate_bill()
        elif ch == "5":
            search_patient()
        elif ch == "6":
            total_patients()
            ward_usage()
        elif ch == "7":
            ward_chart()
        elif ch == "8":
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()