import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df_sales = pd.read_csv("https://docs.google.com/spreadsheets/d/1MW-zi5SU4VHChqn1heGOi3zQx77dG17_/edit?usp=sharing&ouid=101166119605484992249&rtpof=true&sd=true")
df_population = pd.read_csv("https://docs.google.com/spreadsheets/d/165zNpREsKpuOm008hZPTZ2km3FRBPflm/edit?usp=sharing&ouid=101166119605484992249&rtpof=true&sd=true")
df_area = pd.read_csv("https://docs.google.com/spreadsheets/d/1P35_LAZAI65bGeHBqXkURzo98OLS0nBg/edit?usp=sharing&ouid=101166119605484992249&rtpof=true&sd=true")
df_time = pd.read_csv("https://docs.google.com/spreadsheets/d/1eOUww2RBh7IVCmISXoEKfDdDdIn9nBg/edit?usp=sharing&ouid=101166119605484992249&rtpof=true&sd=true")

# Обробка викидів та відсутніх значень
df_sales = df_sales[df_sales["Ціна"] <= df_sales["Ціна"].quantile(0.75) + 1.5 * df_sales["Ціна"].iqr()]
df_sales["Площа"].fillna(df_sales["Площа"].mean(), inplace=True)
df_sales["Місто"].fillna("Невідомо", inplace=True)

# Перевірка формату дат
df_time["Дата"].dt.year

# Перевірка числових значень
df_sales["Ціна"].dtype

# Візуалізація та зіставлення даних

# Ціна з часом
plt.plot(df_time["Дата"], df_sales["Ціна"])
plt.title("Ціна нерухомості з часом")
plt.xlabel("Дата")
plt.ylabel("Ціна")

# Розподіл ціни
plt.hist(df_sales["Ціна"])
plt.title("Розподіл ціни нерухомості")
plt.xlabel("Ціна")

# Взаємозв'язок між ціною та площею
plt.scatter(df_sales["Площа"], df_sales["Ціна"])
plt.title("Взаємозв'язок між ціною та площею нерухомості")
plt.xlabel("Площа")
plt.ylabel("Ціна")

# Середні значення ціни за житловими масивами
df_sales.groupby("Місто")["Ціна"].mean()

# Т-тест для порівняння середніх значень ціни між двома житловими масивами
ttest_ind(df_sales[df_sales["Місто"] == "Нью-Йорк"]["Ціна"], df_sales[df_sales["Місто"] == "Лос-Анджелес"]["Ціна"])

# Висновки

# Ринок нерухомості у США знаходиться на етапі зростання.
# Ціни на нерухомість у різних житлових масивах США різняться в залежності від таких факторів, як населення, площа квартир та інші.
