# World Happiness Report Analysis

*A data analytics project exploring factors related to national happiness*

* [1. Introduction](#1-introduction)  
* [2. Project Goals & Key Questions](#2-project-goals--key-questions)  
* [3. Data Sources & References](#3-data-sources--references)  
* [4. Future Directions](#4-future-directions)
---

## 1. Introduction

Since 2012, the *World Happiness Report* has published an annual ranking of countries based on happiness scores. In fact, as of 2024, Finland is the happiest country in the world. This work — a collaboration between Gallup, the Oxford Wellbeing Research Centre, the UN Sustainable Development Solutions Network, and the WHR’s Editorial Board — is an internationally recognized project with implications for shaping decisions that could improve national satisfaction and well-being. 

In addition to ranking happiness scores, the report also provides measures of other variables associated with national happiness, such as GDP per capital, healthy life expectancy, and generosity. This project analyzes data from the World Happiness Report 2024 to explore the factors associated with national happiness scores.

---

## 2. Project Goals & Key Questions
This project demonstrates key data analytics skills, including:
* Data cleaning and preparation (handling missing values, structuring datasets)
* Statistical analysis and correlation studies
* Machine learning (linear regression, SVM, random forest) for predicting happiness scores
* Data visualization (Matplotlib, Seaborn, Tableau)

Ultimately, I aimed to answer the following questions:
* What are the distributions of the variables?
* What are the top and bottom countries for each variable?
* How are these variables correlated with each other?
* What are the distributions of the variables within each SDG region?
* What are the regional averages for each variable, and how have they changed over time?
* Using the latest data (2023), can we accurately predict a happiness score based on values for each variable?

In the end, I produced the following:
* A Jupyter Notebook consisting of my EDA work (including data cleaning, preparation, and visualizations) and machine learning models
* An [interactive Tableau map](https://public.tableau.com/app/profile/comfort.ohajunwa/viz/WorldHappinessData_17362896398450/WorldHappinessMap) displaying happiness data
* A [Streamlit tool](https://worldhappinessreportproject.streamlit.app/) for predicting happiness scores based on relevant well-being factors 

---


## 3. Data Sources & References
* *2024 World Happiness Report*: https://worldhappiness.report/ed/2024/
* *2024 World Happiness Report Data for Table 2.1* (Automatic download): https://happiness-report.s3.amazonaws.com/2024/DataForTable2.1.xls
* *2024 World Happiness Report Statistical Appendix 1 for Chapter 2* (Details about variables and data collection): https://happiness-report.s3.amazonaws.com/2024/Ch2+Appendix.pdf
* *World Regions in the SDG Framework* (SDG region designations): https://ourworldindata.org/grapher/world-regions-sdg-united-nations

---

## 4. Future Directions
* Explore affects of other factors (geopolitical conflicts, natural disasters, and other critical events) on happiness
* Display visualizations from Jupyter notebook 
