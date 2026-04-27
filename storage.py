import csv

def save_data(file, row):
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

def read_data(file):
    data = []
    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            data = list(reader)
    except:
        pass
    return data