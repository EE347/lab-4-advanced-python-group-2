import csv
import matplotlib.pyplot as plt
from datetime import datetime

x = []
y = []

with open("task9.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[0]))
    
plt.plot(x,y)
plt.show()
        

"""file_path = 'task9.csv'
data = pd.read_csv(file_path)

x_values = []
y_values = []

with open("task9.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            x_values.append(datetime.strptime(row[0], '%Y-%m-%d'))
        except ValueError:
            x_values.append(float(row[0]))
            y_values.append(float(row[0]))

plt.plot(x_values, y_values, label= "Data froom CSV")
plt.xlable("x-axis Date or Value")
plt.ylabel("y-axis")
plt.title("Plot of data")
plt.legend()

if isinstance(x_values[0], datetime):
    plt.gcf().autofmt_xdate()

plt.show

-----------------------------------
def read_csv(filename):
    dates = []
    meta_prices = []
    aapl_prices = []
    amzn_prices = []
    nflx_prices = []
    nvda_prices = []
    googl_prices = []

    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            dates.append(date)
            meta_prices.append(float(row[1]))
            aapl_prices.append(float(row[2]))
            amzn_prices.append(float(row[3]))
            nflx_prices.append(float(row[4]))
            nvda_prices.append(float(row[5]))
            googl_prices.append(float(row[6]))

    return dates, meta_prices, aapl_prices, amzn_prices, nflx_prices, nvda_prices, googl_prices

filename = 'task9.csv'
dates, meta, aapl, amzn, nflx, googl = read_csv(filename)

plt.plot( dates, meta, label="META", color ='blue')

plt.plot( dates, aapl, label ="APPL", color = "greem")

plt.plot( dates, label ="APPL", color = "greem")

plt.plot( dates, label ="APPL", color = "greem")

plt.plot( dates, label ="APPL", color = "greem")

plt.plot( dates,label ="APPL", color = "greem" )
  
plt.show()"""