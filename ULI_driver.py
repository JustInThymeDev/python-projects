import pandas as pd
import csv
headerList = ['First Name', 'Last Name', 'User Name', 'User Password']
with open("User_Login_Info.csv", 'w', newline='') as f:
    dw = csv.DictWriter(f, delimiter=',', fieldnames=headerList)
    dw.writeheader()
