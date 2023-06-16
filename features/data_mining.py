import pandas as pd
import data_wrangling
import sys
import os
sys.path.append(os.path.abspath('../visualization'))
import mining_charts


class FeatureMining:
    def __init__(self):
        # Container declaration
        self.info_books = []
        self.rating_books = []

    @staticmethod
    def display_dataframe(name, df, contents):
        table = df.head(contents)
        print('\n', '_' * 150)
        print("◘ Displaying dataframe for ", name)
        print(table.to_string())
        print('_' * 150)

    def data_wrangling(self):
        # Instance creation
        object_wrangling = data_wrangling.FeatureWrangling()
        info, ratings = object_wrangling.data_processing()

        self.info_books = info
        self.rating_books = ratings

    def data_mining(self):
        graph = mining_charts.MiningCharts()

        # Title-based -----------
        # Books most accessed or bought by users
        most_purchases = self.rating_books.groupby('book_title')['user_id'].count().sort_values()
        df_ratings = most_purchases.to_frame()
        df_ratings['most_purchases'] = most_purchases

        graph.bar_charts_h(most_purchases.values[-15:], most_purchases.index[-15:],
                           "Books most bought by users", 'Purchases', 'Books', most_purchases.index[-15:])

        # Highest rated books
        mean_ratings = self.rating_books.groupby('book_title')['rating'].mean()
        df_ratings['mean_ratings'] = mean_ratings

        graph.bar_charts_h(mean_ratings.values[-15:], mean_ratings.index[-15:],
                           "Highest rated books", 'Ratings', 'Books', mean_ratings.index[-15:])

        # Books with the highest mean price in stores
        mean_price = self.rating_books.groupby('book_title')['book_price'].mean()
        df_ratings['mean_price'] = mean_price

        graph.bar_charts_h(mean_price.values[-15:], mean_price.index[-15:],
                           "Most expensive books", "Price Range", 'Books', mean_price.index[-15:])

        # Top-rated books accumulating over 3500 ratings per book
        books_rated = self.info_books[self.info_books['ratings_count'] > 3500][['book_title', 'ratings_count']]\
            .drop_duplicates()

        graph.bar_charts_v(books_rated['book_title'], books_rated['ratings_count'],
                           "Top-rated books exceeding 3500 ratings per Book")

        # The amount of books in a particular category
        categories_title = self.info_books.groupby('categories')['book_title'].count().sort_values()
        df_records = categories_title.to_frame()
        df_records['categories_title'] = categories_title

        graph.bar_charts_h(categories_title.values[-15:], categories_title.index[-15:],
                           "The amount of books in a particular category", 'Genres', 'Books',
                           categories_title.index[-15:])

        # Author-based -----------
        # Authors with the most published books
        author_publish = self.info_books.groupby('book_author')['book_title'].count().sort_values()
        df_records['author_publish'] = author_publish

        graph.bar_charts_h(author_publish.values[-15:], author_publish.index[-15:],
                           "Authors with the most published books", 'Books', 'Authors', author_publish.index[-15:])

        # Authors who worked in a variety genres of book genres
        author_categories = self.info_books.groupby('book_author')['categories'].nunique()
        df_records['book_genres'] = author_categories

        graph.bar_charts_h(author_categories.values[-15:], author_categories.index[-15:],
                           "Authors in different book genres", "Number of Genres", 'Authors',
                           author_categories.index[-15:])

        # Number of years an author is active
        author_years = self.info_books.groupby('book_author')['published_year'].nunique()
        df_records['author_year'] = author_years

        graph.bar_charts_h(author_years.values[-15:], author_years.index[-15:],
                           "Number of years an author is active", 'Years', 'Authors', author_years.index[-15:])

        # Sort dataframe
        df_records = df_records.sort_values(by=['author_publish', 'book_genres'], ascending=False)
        self.display_dataframe("mining book records", df_records, 25)

        df_ratings = df_ratings.sort_values(by=['most_purchases', 'mean_ratings', 'mean_price'], ascending=False)
        self.display_dataframe("mining book ratings", df_ratings, 25)


if __name__ == "__main__":
    data = FeatureMining()
    data.data_wrangling()
    data.data_mining()
