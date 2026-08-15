import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Observed frequencies (tweaked parameters for a unique run)
observed = np.array([22, 17, 18, 26, 15, 22])

# Total trials and expected uniform frequencies
total_trials = np.sum(observed)
num_categories = len(observed)
expected = np.full(num_categories, total_trials / num_categories)

# Chi-Square Test calculation
chi2_stat, p_val = stats.chisquare(f_obs=observed, f_exp=expected)

print("Observed Frequencies:", observed)
print("Expected Frequencies:", expected)
print("Chi-Square Statistic:", round(chi2_stat, 4))
print("p-value:", round(p_val, 4))

# Decision logic
alpha = 0.05
if p_val > alpha:
    print(
        "Result: Fail to reject H0 (Data fits the expected distribution well)"
    )
else:
    print(
        "Result: Reject H0 (Data differs significantly from expected distribution)"
    )

# Visualizing Observed vs Expected frequencies
categories = [f"Die {i+1}" for i in range(num_categories)]
x = np.arange(len(categories))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x - width / 2, observed, width, label="Observed", color="skyblue")
plt.bar(x + width / 2, expected, width, label="Expected", color="orange")

plt.xlabel("Outcomes")
plt.ylabel("Frequency")
plt.title("Chi-Square Goodness-of-Fit Test")
plt.xticks(x, categories)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()