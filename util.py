import pandas as pd


def get_data(url):
    return pd.read_csv(url, sep='\t')


def show_dataframe_info(df):
    print(df)
    print(df.head(10))
    print(df.info())
    print(df.shape[0])
    print(df.shape[1])
    print(df.columns)
    print(df.index)


def get_most_ordered_item(df):
    c = df.groupby('item_name')
    c = c.sum()
    c = c.sort_values(['quantity'], ascending=False)
    return c


def get_head(df):
    return df.head(1)


def get_times_items_were_ordered(df):
    c = df.groupby('item_name')
    c = c.sum()
    c = c.sort_values(['quantity'], ascending =False)
    return c


def get_most_ordered_item_by_choice_description(df):
    c = df.groupby('choice_description').sum()
    c = c.sort_values(['quantity'], ascending =False)
    return c


def get_ordered_items_in_total(df):
    c = df.quantity.sum()
    return c


