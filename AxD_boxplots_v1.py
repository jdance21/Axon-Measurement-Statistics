### Makes a boxplot of AxD Values for each angle of each mouse ###

### not coloured in boxplot, vertical lines in background ###

import numpy as np
import matplotlib.pyplot as plt

# Makes boxes, bounds, and outliers
def plot_boxplot(dataset, position, color, point_size=20):
    Q1 = np.percentile(dataset, 25)
    Q3 = np.percentile(dataset, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    boxprops = dict(marker='o', color='black', markersize=1, markerfacecolor='none')
    boxplot = plt.boxplot(dataset, positions=[position], widths=0.5, flierprops=boxprops)

    scatter = plt.scatter(np.ones(len(dataset)) * position, dataset, color=color, s=point_size, zorder=2)
    is_outlier = (np.array(dataset) < lower_bound) | (np.array(dataset) > upper_bound)
    scatter.set_color(np.where(is_outlier, 'blue', color))

# Load data
data0 = [0.641649, 0.896996, 0.893408, 1.054659, 0.983915, 0.709809]
data45 = [0.758947, 0.776973, 0.779329, 1.178353, 1.148037, 0.726551]
data90 = [0.681292, 0.796390, 0.943940, 1.137404, 1.255703, 0.895933]
data315 = [0.609591, 0.928828, 1.054659, 1.079928, 1.006901, 0.891354]

# Plot at evenly spaced x positions (0, 1, 2, 3)
plot_boxplot(data0, 0, 'green', point_size=30)
plot_boxplot(data45, 1, 'green', point_size=30)
plot_boxplot(data90, 2, 'green', point_size=30)
plot_boxplot(data315, 3, 'green', point_size=30)

# Set evenly spaced tick labels
plt.xticks([0, 1, 2, 3], ['0', '45', '90', '315'])

# Labels and title
plt.title('Boxplot of AxD Values for Each Angle Orientation')
plt.ylabel('AxD Values (μm)')
plt.xlabel('Angle Orientations ($^\circ$)')

# Legend
median_handle = plt.Line2D([], [], color='orange', linewidth=2, label='Median')
data_handle = plt.Line2D([], [], marker='o', color='green', markersize=6, linestyle='None', label='Data Points')
outlier_handle = plt.Line2D([], [], marker='o', color='blue', markersize=6, linestyle='None', label='Outliers')
plt.legend(handles=[median_handle, data_handle, outlier_handle])


# Save and show boxplot
plt.tight_layout()
plt.savefig('AxD_Boxplot.png', dpi=300, bbox_inches='tight') # Change filename
plt.show()
