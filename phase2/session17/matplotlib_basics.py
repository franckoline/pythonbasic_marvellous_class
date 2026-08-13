import matplotlib.pyplot as plt
import numpy as np
# Generate a line chart showing business growth over 12 months.

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
         "October", "November", "December"]
revenue = np.array([5000, 6000, 7500, 9000, 10500, 12500, 14000, 15000, 16000, 17500, 22500, 25000])

print(len(month))
print(len(revenue))
title_style = dict(family = "Times New Roman",
                   fontsize =20,
                   fontweight = "bold")
label_style = dict(family = "Arial",
                   fontsize = 17,
                   fontweight = "bold")
plt.plot( revenue, month,
          marker = ".",
          markersize = 4,
          mfc = "black",
          mec = "black",
          color = "black")
plt.grid(axis = "both",
         linestyle = "dotted")
plt.title("BUSINESS GROWTH", **title_style)
plt.xlabel("Month", **label_style)
plt.ylabel("Revenue", **label_style)
plt.tight_layout()
plt.show()