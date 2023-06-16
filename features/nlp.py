from wordcloud import WordCloud as WC
import data_wrangling
import matplotlib.pyplot as plt
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as Sia
import sys
import os
sys.path.append(os.path.abspath('../visualization'))
import analysis_charts


class TextProcessing:
    def __init__(self):
        obj_wrangling = data_wrangling.FeatureWrangling()
        self.books_info, self.books_rating = obj_wrangling.data_processing()

    @staticmethod
    def display_dataframe(name, df, contents):
        table = df.head(contents)
        print('\n', '_' * 50)
        print("◘ Displaying dataframe ", name)
        print(table.to_string())
        print('_' * 50)

    @staticmethod
    def word_cloud_ratings(data, feature, target_rating, target_text, op):
        cloud = WC(width=500, height=500, min_font_size=15, background_color='white')
        if op == '>':
            spam_wc = cloud.generate(data[data[feature] > target_rating][target_text].str.cat(sep=" "))
        else:
            spam_wc = cloud.generate(data[data[feature] < target_rating][target_text].str.cat(sep=" "))

        plt.figure(figsize=(20, 10))
        plt.axis('off')
        plt.imshow(spam_wc)

    def text_processing(self):
        self.word_cloud_ratings(self.books_rating, 'rating', 3, 'review', '>')
        self.word_cloud_ratings(self.books_rating, 'rating', 2, 'review', '<')

        nlp = spacy.load("en_core_web_sm")

        # Locate entities from description of the book to refine the searching engine optimization algorithm
        self.books_info.dropna(axis='columns')
        self.books_info = self.books_info[self.books_info['description'].notna()]
        description = self.books_info['description'].head(100)

        for text_block in description:
            print('\n◘ Text Block:\n', text_block)
            doc = nlp(str(text_block))

            #  Find named entities, phrases and concepts
            print('\n◘ Entities present:')
            for entity in doc.ents:
                print('\n•', entity.text, entity.label_)

        # Sentiment Analysis
        vader = Sia()
        data = self.books_rating.head(10000)

        # Lower casing the reviews
        data['clean_review'] = data['review'].str.lower()

        # Calculating Polarity score of reviews
        data['score'] = data['clean_review'].apply(lambda review: vader.polarity_scores(review))

        # Extracting compound column
        data['compound'] = data['score'].apply(lambda score_dict: score_dict['compound'])

        # Sentiment generation based on compound values: 0.05 = positive, -0.0 = negative, 0.0 = neutral
        data['Sentiment'] = data['compound'].apply(
            lambda x: 'positive' if x >= 0.05 else 'negative' if x < -0.05 else 'neutral')

        # Dataframe diagnostics
        self.display_dataframe("with Sentiment analysis value:", data, 25)

        sentiment = data['Sentiment'].value_counts()
        explode = (0.1, 0.1, 0.1)
        labels = ['positive', 'negative', 'neutral']
        title = 'Pie-chart distribution of Sentiment analysis:'

        charts = analysis_charts.AnalysisCharts()
        charts.pie_charts_matplotlib(sentiment, explode, labels, title)


if __name__ == "__main__":
    text = TextProcessing()
    text.text_processing()
