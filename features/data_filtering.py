import pandas as pd
path_info = '../data/books_data.csv'
path_rating = '../data/Books_rating.csv'


class FeatureWrangling:
    def __init__(self):
        self.info_books = pd.read_csv(path_info)
        self.rating_books = pd.read_csv(path_rating)

        # Clean data
        self.info_books.dropna(axis=0, how='any')
        self.rating_books.dropna(axis=0, how='any')

        print('_' * 150)
        print("•Raw Features for Book details:\n", self.info_books.columns)
        print('_' * 150)
        print("•Raw Features for Book ratings:\n", self.rating_books.columns, "\n")
        print('_' * 150)

    @staticmethod
    def display_dataframe(name, df, contents):
        table = df.head(contents)
        print('\n', '_' * 150)
        print("◘ Displaying dataframe for ", name)
        print(table.to_string())
        print('_' * 150)

    def data_processing(self):
        # Truncate Redundancies
        info = self.info_books.drop(["image", "previewLink", "publisher", "infoLink"],
                                    axis=1)
        ratings = self.rating_books.drop(["profileName", "review/time", "review/helpfulness", "review/summary"],
                                         axis=1)

        # Data Accessibility
        info.rename(columns={'Title': 'book_title', 'authors': 'book_author', 'publishedDate': 'published_date',
                             'ratingsCount': 'ratings_count'},
                    inplace=True)
        ratings.rename(columns={'Id': 'book_id', 'Title': 'book_title', 'Price': 'book_price',
                                'User_id': 'user_id', 'review/text': 'review', 'review/score': 'rating'},
                       inplace=True)

        print("•Columns for Books data:\n", info.columns)
        print('_' * 150)
        print("•Columns for Books Rating:\n", ratings.columns, '\n')
        print('_' * 150)

        # Remove data inconsistency
        published_year = []
        year = 0
        exception_list = []

        # 'Year' extraction procedure
        for sample in info['published_date']:
            try:
                year = sample.split('-')[0]

            except Exception as exc:
                exception_list.append(exc)
                year = sample

            finally:
                published_year.append(year)

        info['published_year'] = published_year
        info = info.drop(['published_date'], axis=1)
        print("\n! Operation completed with ", len(exception_list), " Exceptions handled")

        # Dataframe diagnostics
        self.display_dataframe("filtered book records", info, 25)
        self.display_dataframe("filtered book ratings", ratings, 25)

        return info, ratings


if __name__ == "__main__":
    feature = FeatureWrangling()
    print(feature.data_processing())
