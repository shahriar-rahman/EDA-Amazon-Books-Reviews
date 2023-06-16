import pandas as pd
import missingno as msn
from matplotlib import pyplot as plt
import plotly.graph_objs as go
import sys
import os
import data_wrangling
sys.path.append(os.path.abspath('../visualization'))
import analysis_charts


class FeatureAnalysis:
    def __init__(self):
        # Create instance
        object_wrangling = data_wrangling.FeatureWrangling()
        self.info_books, self.rating_books = object_wrangling.data_processing()

    @staticmethod
    def display_dataframe(name, df, contents):
        table = df.head(contents)
        print('\n', '_' * 150)
        print("◘ Displaying dataframe for ", name)
        print(table.to_string())
        print('_' * 150)

    def data_observation(self):
        # Display Structural Integrity
        print("\n◘ Dataset statistical Information: ")
        print('• Book Records dataset structure:\n', self.info_books.describe(), '\n')
        print('• Book Ratings dataset structure:\n', self.rating_books.describe(), '\n')
        print('_' * 150)

        print('• Book Records dataset info:\n', self.info_books.info(), '\n')
        print('• Book Ratings dataset info:\n', self.rating_books.info(), '\n')
        print('_' * 150)

        print('• Book Records dataset shape:\n', self.info_books.shape, '\n')
        print('• Book Ratings dataset shape:\n', self.rating_books.shape, '\n')
        print('_' * 150)

        print('• Book Records dataset columns:\n', self.info_books.columns, '\n')
        print('• Book Ratings dataset columns:\n', self.rating_books.columns, '\n')
        print('_' * 150)

        # Visualize the distribution of NaN values using Missingno
        print('• Book Records dataset Null checking:\n', self.info_books.isnull().sum(), '\n')
        print('_' * 150)
        msn.matrix(self.info_books, color=(0.66, 0.25, 0.013), figsize=[13, 15], fontsize=10)
        plt.title("Missingno Matrix for Book Records:")
        plt.show()

        print('• Book Ratings dataset Null checking:\n', self.rating_books.isnull().sum(), '\n')
        print('_' * 150)
        msn.matrix(self.rating_books, color=(0.66, 0.25, 0.013), figsize=[13, 15], fontsize=10)
        plt.title("Missingno Matrix for Book Ratings:")
        plt.show()

        # Distribution Plotting
        analysis = analysis_charts.AnalysisCharts()
        analysis.pie_charts(self.rating_books, 'rating', 'Pie Chart for the distribution of Ratings:')
        analysis.histograms(self.rating_books, 'rating', 'Data distribution for Ratings:')

        # Visual distribution of Genres
        genres = self.info_books['categories'].value_counts().sort_values(ascending=False)
        genres = genres.head(10)

        genres.plot(kind='barh', figsize=(13, 15))
        plt.title('Frequency of Genres', fontsize=20)
        plt.grid()
        plt.show()

        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        labels = genres.keys().map(str)
        title = 'Genre Pie-chart distribution:'
        analysis.pie_charts_matplotlib(genres, explode, labels, title)


if __name__ == "__main__":
    feature = FeatureAnalysis()
    feature.data_observation()
