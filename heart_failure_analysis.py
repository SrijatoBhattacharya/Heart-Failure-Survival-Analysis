import pandas as pd
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test  
import matplotlib.pyplot as plt

df=pd.read_csv("heart_failure.csv")

group_a = df[df['diabetes'] == 1]
group_b = df[df['diabetes'] == 0]

results = logrank_test(
    group_a['time'], group_b['time'],
    event_observed_A=group_a['DEATH_EVENT'], event_observed_B=group_b['DEATH_EVENT']
)

print(f"Log-Rank Test P-value: {results.p_value:.4f}")
if results.p_value < 0.05:
    print("Verdict: The difference in survival is STATISTICALLY SIGNIFICANT.")
else:    print("Verdict: The difference is NOT statistically significant.")

kmf = KaplanMeierFitter()

kmf.fit(group_a['time'], event_observed=group_a['DEATH_EVENT'], label='Diabetes')
ax = kmf.plot_survival_function()

kmf.fit(group_b['time'], event_observed=group_b['DEATH_EVENT'], label='No Diabetes')
kmf.plot_survival_function(ax=ax)

plt.text(2, 0.15, f"Log-Rank p-value: {results.p_value:.4f}", fontsize=11,
            bbox=dict(facecolor='white', edgecolor='black', alpha=0.8))

plt.title("Survival Analysis: Diabetes vs No Diabetes in Heart Failure Patients")
plt.ylabel("Probability of Survival")
plt.xlabel("Days")
plt.legend()
plt.show()