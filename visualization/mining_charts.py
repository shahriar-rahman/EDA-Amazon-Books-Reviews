import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from matplotlib.font_manager import FontProperties
import plotly.express as px
import plotly.graph_objects as go


class MiningCharts:
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
    def bar_charts_h(x, y, title, x_labels, y_labels, color):
        # Horizontal Bar Chart using plotly
        fig = px.bar(x=x, y=y, orientation='h', color=color)

        fig.update_layout(title={'text': title, 'font': {'size': 23, 'color': '#1c0308'}, 'x': 0.5},
                          xaxis_title={'text': x_labels, 'font': {'size': 18, 'color': '#1c0308'}},
                          yaxis_title={'text': y_labels, 'font': {'size': 18, 'color': '#1c0308'}})
        fig.show()

    @staticmethod
    def bar_charts_v(x, y, title):
        # Vertical Bar charts using matplotlib
        plt.figure(figsize=(13, 15))
        plt.bar(x, y)

        plt.title(title, fontsize=16)
        plt.xlabel('Books')
        plt.xticks(rotation='vertical')
        plt.ylabel('Ratings')
        plt.show()


if __name__ == "__main__":
    charts = MiningCharts()
