from datetime import datetime, timedelta

def nora():
    datan = datetime(2019, 9, 22, 14, 00)
    dias =41 * 7 + 2
    data_g = datan + timedelta(days=dias)
    return data_g


print(nora())
