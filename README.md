===========================================================================
# EDA Amazon Books Reviews
An exploratory analysis of the Amazon Book Reviews. An expansion to this project is carried out using Collaborative Filtering models from the research: [A Comparative Analysis of Amazon Book Ratings Using Collaborative Filtering](https://github.com/shahriar-rahman/A-Comparative-Analysis-of-Amazon-Book-Ratings-using-Collaborative-Filtering/tree/main).

![alt text](https://github.com/shahriar-rahman/A-Comparative-Analysis-of-Amazon-Book-Ratings-using-Collaborative-Filtering/blob/main/img/amazon%20(13).jpg)

### ◘ Introduction
The general idea behind this research is to identify and establish a pattern or a set of patterns and relationships 
among a plethora of features available within the acquired data. A thorough analysis is performed by using a 
multitude of tools and packages using Python so that a set of statistical and/or machine learning models can 
be applied to accomplish better generalization.

</br></br>

### ◘ Study Flowchart
![alt text](https://github.com/shahriar-rahman/EDA-Amazon-Books-Reviews/blob/main/img/img1.JPG)

</br></br>

### ◘ Project Organization
------------

    ├── LICENSE
    ├── Makefile          				<- Makefile with commands.
    ├── README.md             	<- The top-level README for developers using this project.
    ├── data
	|
	|
    ├── features                		<- Set of files to construct a more readable and useable data.
	|   |── data_filtering.py		<- Script that filters through the data and keeps important features.
	|   |── data_processing.py   <- File where data is cleaned and visually analyzed for its distribution.
	|   |── data_inspection.py    <- Script to observe and search for patterns and relationship among various features.
	|   └── nlp.py                     <- Text from the review features are processed and analyzed for better intuition.
    │	 
	|
    ├── figures            				<- Generated graphics and figures to be used in reporting (includes IDE and Notebooks generated graphs).
    │    				     
    │
    ├── notebooks          			<- Additional script for Jupyter Notebooks for better visualization.
    │
	│
    ├── requirements.txt    		<- The requirements file for reproducing the analysis environment, e.g.
    │                         				    generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           			<- makes project pip installable (pip install -e .) so src can be imported
	|
    │
	|	
    ├── visualization           		<- Create exploratory and results oriented visualizations.
	|   |── analysis_charts.py		<- Script to better facilitate abstractions for generating simple graphs.
	|   └── mining_charts.py		<- Can be used to generate a more specific type of graph to be utilized during data inspection.
    │
    └── tox.ini            				<- tox file with settings for running tox; see tox.readthedocs.io

--------

</br></br>

### ◘ Modules Required:
* pandas 2.0.0
* plotly 5.15.0
* missingno 0.5.2
* vaderSentiment 3.3.2
* spacy 3.5.3
* matplotlib 3.7.1
* seaborn 0.12.2
* wordcloud 1.9.2

</br></br>

===========================================================================

