import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from matplotlib.font_manager import FontProperties
import plotly.express as px
import plotly.graph_objects as go


class AnalysisCharts:
    def __init__(self):
        pass

    @staticmethod
    def graph_settings():
        # Customizable Set-ups
        plt.figure(figsize=(13, 15))
        font = FontProperties()
        font.set_family('serif bold')
        font.set_style('oblique')
        font.set_weight('bold')
        ax = plt.axes()
        ax.set_facecolor("#e6eef1")

    @staticmethod
    def pie_charts(df, feature, title):
        # Plot pie chart using Plotly library
        color_scheme = ['orange', 'mediumturquoise', 'maroon']
        labels = df[feature].value_counts().keys().map(str)
        values = df[feature].value_counts() / df[feature].value_counts().shape[0]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20,
                          marker=dict(colors=color_scheme, line=dict(color='white', width=0.1)))
        fig.update_layout(title={'text': title, 'font': {'size': 23, 'color': '#1c0308'}, 'x': 0.5})
        fig.show()

    def pie_charts_matplotlib(self, df, explode, labels, title):
        # Plot pie chart using Matplotlib library
        self.graph_settings()

        plt.pie(df, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
        plt.title(title, fontsize=20)
        plt.axis('off')
        plt.legend(loc="upper left")
        plt.show()

    def histograms(self, df, feature, title):
        # Plot Histograms using Matplotlib library
        self.graph_settings()

        plt.hist(df[feature])
        plt.xlabel('Ratings')
        plt.ylabel('Frequency')
        plt.title(title)
        plt.show()


if __name__ == "__main__":
    charts = AnalysisCharts()
