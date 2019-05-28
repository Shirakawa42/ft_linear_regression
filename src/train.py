import sys
import csv
import matplotlib.pyplot as plt
import itertools

x = []
y = []

with open(sys.argv[1], newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        try:
            x.append(int(row[0]))
            y.append(int(row[1]))
        except:
            pass

plt.scatter(x, y)

plt.title('ft_linear_regression')
plt.xlabel('km')
plt.ylabel('price')

plt.show()
