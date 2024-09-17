import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def read_csv(filename):
    try:
        df = pd.read_csv(filename, sep=';', encoding='utf-8-sig')
        print("Файл CSV успішно відкрито.")
        print("Ok")
        return df
    except FileNotFoundError:
        print("Файл CSV не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при відкритті файлу CSV: {e}")
        return None

def calculate_age(birth_date):
    today = datetime.today()
    birth_date = pd.to_datetime(birth_date)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def add_age_column(df):
    df['Дата народження'] = pd.to_datetime(df['Дата народження'])
    df['Вік'] = df['Дата народження'].apply(calculate_age)
    return df

def plot_gender_distribution(df):
    gender_counts = df['Стать'].value_counts()
    print("\nКількість співробітників за статтю:")
    print(gender_counts)
    gender_counts.plot(kind='bar', color=['blue', 'pink'])
    plt.title('Розподіл за статтю')
    plt.xlabel('Стать')
    plt.ylabel('Кількість співробітників')
    plt.xticks(rotation=0)
    plt.show()

def plot_age_distribution(df):
    age_bins = [0, 18, 45, 70, 150]
    age_labels = ['Менше 18', '18-45', '45-70', 'Більше 70']
    df['Вікова категорія'] = pd.cut(df['Вік'], bins=age_bins, labels=age_labels, right=False)
    age_counts = df['Вікова категорія'].value_counts().sort_index()
    print("\nКількість співробітників за віковими категоріями:")
    print(age_counts)
    age_counts.plot(kind='bar', color='lightblue')
    plt.title('Розподіл за віковими категоріями')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.xticks(rotation=0)
    plt.show()

def plot_gender_age_distribution(df):
    gender_age_distribution = pd.crosstab(df['Вікова категорія'], df['Стать'])
    print("\nКількість співробітників за віковими категоріями і статтю:")
    print(gender_age_distribution)
    gender_age_distribution.plot(kind='bar', stacked=True, colormap='Paired')
    plt.title('Розподіл за статтю по віковим категоріям')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.xticks(rotation=0)
    plt.show()

def main():
    filename = 'employees.csv'
    df = read_csv(filename)

    if df is not None:
        df = add_age_column(df)
        plot_gender_distribution(df)
        plot_age_distribution(df)
        plot_gender_age_distribution(df)

if __name__ == "__main__":
    main()
