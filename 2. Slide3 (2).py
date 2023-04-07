import matplotlib.pyplot as plt
import numpy as np

labels = np.array(["A", "B", "C", "D"])
sizes = np.array([35, 25, 25, 15])
colors = np.array(["MediumVioletRed",
                   "Violet",
                   "DodgerBlue",
                   "DeepSkyBlue"])
explodes = np.array([0.1, 0.05, 0.05, 0.05])

plt.pie(sizes, labels = labels,
               explode = explodes,
               colors = colors,
               autopct = '%.0f%%')

plt.title("Simple Pie Chart")

plt.legend(title = "Segments:",
           loc = "upper left")

plt.show()