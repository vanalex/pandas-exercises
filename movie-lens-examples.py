import pandas as pd

u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('./data/ml-100k/u.user', sep= '|', names= u_cols, encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('./data/ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')

m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('./data/ml-100k/u.item', sep='|', names=m_cols, usecols=range(5), encoding='latin-1')

print(users.info())
print('')
print(ratings.info())
print('')
print(movies.info())
print('')
print(movies.dtypes)
print('')
print(users.describe())
print('')
print(movies.head())
print('')
print(movies.tail(3))
print('')
print(movies[20:22])
print('')
print(users['occupation'].head())
print('')
print(users[['age', 'zip_code']].head())
print('')
columns_you_want = ['occupation', 'sex']
print(users[columns_you_want].head())

