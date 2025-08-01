### Makes boxplot of AxD values for each angle orientation for each mouse ###

### coloured in boxplot, no vertical lines in background ###


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

# Step 1: Input your own data
data = {
    '0':   [0.641649, 0.896996, 0.893408, 1.054659, 0.983915, 0.709809],
    '45':  [0.758947, 0.776973, 0.779329, 1.178353, 1.148037, 0.726551],
    '90':  [0.681292, 0.796390, 0.943940, 1.137404, 1.255703, 0.895933],
    '315': [0.609591, 0.928828, 1.054659, 1.079928, 1.006901, 0.891354]
}

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Melt DataFrame to long format
df_long = pd.melt(df, var_name='Angles ($^\circ$)', value_name='AxD Values (um)')

# Step 4: Set the plot style and create a color palette
sns.set(style='whitegrid')
palette = {'0': 'b', '45': 'b', '90': 'b', '315': 'b'}


# Step 5: Create the boxplot
ax = sns.boxplot(
    x='Angles ($^\circ$)', 
    y='AxD Values (um)', 
    data=df_long, 
    palette=palette, 
    showfliers=True,  # show outliers
    flierprops=dict(marker='o', markerfacecolor='yellow', markersize=5, linestyle='none')
)

# Step 6: Add custom legend for median and outliers
median_patch = mpatches.Patch(color='grey', label='Median')
outlier_marker = plt.Line2D([], [], color='yellow', marker='o', markeredgecolor='black', markersize=5, linestyle='None', label='Outlier')
plt.legend(handles=[median_patch, outlier_marker], loc='upper right')


# Optional: Add a title or adjust labels
plt.title("Boxplot of AxD Values Across Angle Orientations")
plt.ylabel("AxD Values (μm)")

# Step 7: Show and save plot
plt.tight_layout()
plt.savefig('AxD_Boxplot.png', dpi=300, bbox_inches='tight')
plt.show()
