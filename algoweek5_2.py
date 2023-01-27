import pandas as pd

df = pd.read_csv('netflix_titles.csv')
df['date_added'] = pd.to_datetime(df.date_added)
df_sort = df.sort_values(
    by=['date_added', 'release_year', 'duration'], ascending=[False, False, True])
df_sort = df_sort.reset_index(drop=True)
df_sort.index = df_sort.index + 1
df_ranking = df_sort[['title', 'country', 'date_added',
                      'release_year', 'duration', 'listed_in']].head(100)
print(df_ranking)
