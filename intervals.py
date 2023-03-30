from scipy.stats import t

# Function to calculate the confidence interval for a given x value
def confidence_interval(x, b0, b1, x_mean, t_val, sigma, sxx, n):
    se_pred = math.sqrt(sigma * (1 + (1/n) + ((x - x_mean)**2)/sxx))
    lower_bound = (b0 + b1 * x) - t_val * se_pred
    upper_bound = (b0 + b1 * x) + t_val * se_pred
    return lower_bound, upper_bound

# Calculating the confidence interval bounds for each x value
n = x_pts.count()
alpha_80 = 1 - 0.80
alpha_95 = 1 - 0.95
alpha_99 = 1 - 0.99

t80 = t.ppf(1 - alpha_80/2, n-2)
t95 = t.ppf(1 - alpha_95/2, n-2)
t99 = t.ppf(1 - alpha_99/2, n-2)

y_lower_80, y_upper_80 = [], []
y_lower_95, y_upper_95 = [], []
y_lower_99, y_upper_99 = [], []

for x in x_pts:
    lower_80, upper_80 = confidence_interval(x, b0, b1, x_mean, t80, sigma, sxx, n)
    lower_95, upper_95 = confidence_interval(x, b0, b1, x_mean, t95, sigma, sxx, n)
    lower_99, upper_99 = confidence_interval(x, b0, b1, x_mean, t99, sigma, sxx, n)

    y_lower_80.append(lower_80)
    y_upper_80.append(upper_80)
    y_lower_95.append(lower_95)
    y_upper_95.append(upper_95)
    y_lower_99.append(lower_99)
    y_upper_99.append(upper_99)

# Plotting the regression line and the confidence intervals
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_pts, [b0 + b1 * x for x in x_pts], "-r", label="Regression Line")
ax.fill_between(x_pts, y_lower_80, y_upper_80, color='orange', alpha=0.2, label="80% Confidence Interval")
ax.fill_between(x_pts, y_lower_95, y_upper_95, color='blue', alpha=0.2, label="95% Confidence Interval")
ax.fill_between(x_pts, y_lower_99, y_upper_99, color='green', alpha=0.2, label="99% Confidence Interval")
ax.scatter(x_pts, y_pts, label="Data points", alpha=0.7)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()
