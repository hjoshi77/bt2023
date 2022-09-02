import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")

df = datasets[0]

f, ax = plt.subplots(figsize=(8, 8))

# Show each distribution with both violins and points
sns.violinplot(x="feed",y="weight",data=df, inner="box", palette="Set3", cut=2, linewidth=3)

sns.despine(left=True)

f.suptitle('Chick weights by feed type', fontsize=18, fontweight='bold')
ax.set_xlabel("Feed",size = 16,alpha=0.7)
ax.set_ylabel("Weight (g)",size = 16,alpha=0.7)
