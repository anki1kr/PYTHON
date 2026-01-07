import csv
import io

# Create a CSV sample in memory
# csv_data = """Year,Industry,Value
# 2014,Manufacturing,769400
# 2014,Manufacturing,48000
# 2014,Manufacturing,12
# """
try:
    with open("sample.csv","r")as csv_data:
        #if reading from sample in memory folowing is used
        # csvfile=io.StringIO(csv_data)
        csvread=csv.reader(csv_data)
        for i in csvread:
            print(i)
            
except Exception as e:
    print(f"Error occured as {e}")