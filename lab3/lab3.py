import pandas as pd
import seaborn as sns

# Завантаження даних
data = pd.read_csv('Automobile_data.csv')

# Опис ознак
print(data.describe())

# Розподіл ознак
print(data.value_counts())

# Ранжування ознак
ranking = pd.DataFrame({
    'розмах значень': data.describe().std_residuals.to_list(),
    'середнє значення': data.describe().mean.to_list(),
    'дисперсія': data.describe().var.to_list(),
})
ranking = ranking.set_index('розмах значень').sort_values(by='розмах значень', ascending=False)

# Графіки парної кореляції
sns.pairplot(data)

# Матриця теплової карти
plt.figure(figsize=(10, 10))
sns.heatmap(data.corr(), annot=True, cmap='Blues')
plt.show()
