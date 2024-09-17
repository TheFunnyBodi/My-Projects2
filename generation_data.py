import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker('uk_UA')

def generate_record(gender):

    surname = fake.last_name()
    name = fake.first_name_male() if gender == 'Чоловіча' else fake.first_name_female()

    if gender == 'Чоловіча':
        middle_name = fake.first_name_male() + "ович"
    else:
        middle_name = fake.first_name_female() + "івна"

    start_date = datetime(1938, 1, 1)
    end_date = datetime(2008, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = fake.random_int(0, days_between_dates)
    birth_date = start_date + timedelta(days=random_number_of_days)

    return {
        'Прізвище': surname,
        'Ім\'я': name,
        'По-батькові': middle_name,
        'Стать': gender,
        'Дата народження': birth_date.date().isoformat(),
        'Посада': fake.job(),
        'Місто проживання': fake.city(),
        'Адреса проживання': fake.address().replace('\n', ', ').replace(';', ','),
        'Телефон': fake.phone_number(),
        'Email': fake.email()
    }

def generate_records(num_male, num_female):
    records = []
    for _ in range(num_male):
        records.append(generate_record('Чоловіча'))
    for _ in range(num_female):
        records.append(generate_record('Жіноча'))

    random.shuffle(records)
    return records

def write_csv(filename, records):
    if not records:
        print("Немає даних для запису.")
        return

    df = pd.DataFrame(records)
    df.to_csv(filename, index=False, sep=';', encoding='utf-8-sig')

    print(f"Дані успішно згенеровані та збережені у файл {filename}")

total_records = 2000
num_male = int(total_records * 0.6)
num_female = total_records - num_male

records = generate_records(num_male, num_female)
write_csv('employees.csv', records)
