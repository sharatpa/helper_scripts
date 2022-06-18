import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cols = ["Country", "Power Distance", "Individualism", "Masculinity",
        "Uncertainty Avoidance", "Long Term Orientation", "Indulgence"]
stats_list = list()
india_stats = ['India', 77, 48, 56, 40, 51, 26]
stats_list.append(india_stats)
us_stats = ['USA', 40, 91, 62, 46, 26, 68]
stats_list.append(us_stats)
netherlands_stats = ['Netherlands', 38, 80, 14, 53, 67, 68]
stats_list.append(netherlands_stats)
japan_stats = ['Japan', 54, 46, 95, 92, 88, 42]
stats_list.append(japan_stats)
metrics_df = pd.DataFrame(stats_list, columns=cols)
print(metrics_df)
melted_df = pd.melt(metrics_df, id_vars="Country", var_name="Metric", value_name="Value")
print(melted_df)
ax = sns.factorplot(x="Country", y="Value", hue="Metric", data=melted_df, kind='bar')
plt.show()
# ax = sns.barplot(x=metrics_df["Country"], y=metrics_df["Power Distance"], hue=metrics_df["Country"])

