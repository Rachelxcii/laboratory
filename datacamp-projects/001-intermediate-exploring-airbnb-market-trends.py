# Import necessary packages
import pandas as pd
import numpy as np


# Load data
df_price = pd.read_csv('data/airbnb_price.csv')
df_room = pd.read_excel('data/airbnb_room_type.xlsx')
df_review = pd.read_csv('data/airbnb_last_review.tsv', sep='\t')

cols_price = df_price.columns
print(f'PRICE COLS: {cols_price}')

cols_room = df_room.columns
print(f'ROOM COLS: {cols_room}')

cols_review = df_review.columns
print(f'REVIEW COLS: {cols_review}')


# What are the dates of the earliest and most recent reviews?
print(f'REVIEW DATA TYPES:\n{df_review.dtypes}\n')

df_review['last_review'] = pd.to_datetime(df_review['last_review'])#.dt.strftime('%d/%m/%Y')

first_reviewed = df_review['last_review'].min()
last_reviewed = df_review['last_review'].max()

print(f'EARLIEST DATE: {first_reviewed}')
print(f'LASTEST DATE: {last_reviewed}')


# How many of the listings are private rooms?
print(f'UNIQUE VALUES ROOM TYPE:\n{df_room.groupby("room_type").count()}\n')

df_room['room_type'] = df_room['room_type'].str.lower()

print(f'UNIQUE VALUES ROOM TYPE:\n{df_room.groupby("room_type").count()}\n')

nb_private_rooms = df_room[df_room['room_type'] == 'private room']['listing_id'].count()
print(f'NUMBER OF PRIVATE ROOMS LISTED: {nb_private_rooms}')


# What is the average listing price?
df_price = pd.read_csv('data/airbnb_price.csv')

print(f'COLUMN DATA TYPE:\n{df_price.dtypes}\n')
print(f'HEAD PRICE COLUMN:\n{df_price["price"].head()}\n')

df_price["price"] = df_price["price"].str.replace(' dollars', '')

print(f'HEAD PRICE COLUMN:\n{df_price["price"].head()}\n')

df_price["price"] = df_price["price"].astype('int')
avg_price = df_price["price"].mean().round(2)
print(f'AVG PRICE: {avg_price}')


# Combine the new variables into one DataFrame called review_dates
review_dates_dict = {
    'first_reviewed': [first_reviewed],
    'last_reviewed': [last_reviewed],
    'nb_private_rooms': [nb_private_rooms],
    'avg_price': [avg_price]
}

review_dates = pd.DataFrame(review_dates_dict)
