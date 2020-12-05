# The Bachelorette Predictor
### Kwame V. Taylor

The goal of this project is to create a machine learning model that accurately predicts which contestant will win a given season of the ABC reality show The Bachelorette, based on data from Seasons 1-2 and 4-9 (train), Season 10 & 11 (validate), and Seasons 11 & 12 (test).

A note on transparency -- I have not seen any of the above selected seasons of the show. I have, however, seen Season 15 of The Bachelorette, and I am currently watching Season 16. <!--I have left Season 13 and 14 out of the data for the sake of time efficiency, as I would have to scrape that data myself from the Bachelor Nation Wiki, since the FiveThirtyEight data has not been updated past Season 13.--> I may include Seasons 3, 13, and 14 in a future iteration of this project.

<img src="https://static.tumblr.com/c8504796ecc695283d1e8af5c7f137c9/oig2scu/qjlo45s32/tumblr_static_8e9p6wr2jy0wks8c4004w8k4s.png">

---

## Background

From [Wikipedia](https://en.wikipedia.org/wiki/The_Bachelorette):
> ***The Bachelorette*** is an American reality television dating game show that debuted on ABC on January 8, 2003. The show is a spin-off of The Bachelor and the staple part of The Bachelor franchise. The first season featured Trista Rehn, the runner-up from the first season of The Bachelor, offering the opportunity for Rehn to choose a husband among 25 bachelors.

> All of the rules are adapted from the rules of The Bachelor—its parent show. As the name implies, the series revolves around a single bachelorette, usually a former contestant from the previous Bachelor season, and a pool of romantic interests ... which could include a potential husband for the bachelorette; it is essentially a gender-reversed version of the parent show. The show starts with the bachelorette standing in front of the mansion and greeting each male contestant individually, as they make an entrance to the bachelorette. After each rose ceremony, at least one contestant does not receive a rose and goes home; therefore, the pool of contenders gets smaller, and eventually leaves the bachelorette to decide between two contestants in the final rose ceremony.

> For the final selection, one of two male suitors proposes to the bachelorette. Unlike its parent show, all fifteen seasons of The Bachelorette have ended with a proposal which the bachelorette either accepted or declined.

[![9 Things You’ve ALWAYS Wanted To Know About The Bachelor](https://img.youtube.com/vi/p-Jr8iNdXOQ/0.jpg)](https://www.youtube.com/watch?v=p-Jr8iNdXOQ)

9 Things You’ve ALWAYS Wanted To Know About The Bachelor

---

## Project Plan

|    Date    |                                Goal                               |     Finished?     |
|:----------:|:-----------------------------------------------------------------:|:-----------------:|
| 12/3/2020 | Finish project planning and the project MVP with modules.         |<ul><li>- [ ] </li>
| 12/4/2020 | Finish second pipeline iteration.                                 |<ul><li>- [ ] </li>
| 12/5/2020 | Finish third pipeline iteration, with presentation prepared.      |<ul><li>- [ ] </li>
| 12/6/2020 | Practice presentation, exercise, meditate, sleep.                 |<ul><li>- [ ] </li>
| 12/7/2020 | Presentation day!                                                 |<ul><li>- [ ] </li>

<!-- The project deliverables are the following: **Jupyter Notebook** data science pipeline walkthrough with **conclusions**, data **visualizations**, **README**, and **modules with functions** (```wrangle.py```, ```preprocessing.py```, ```explore.py```, and ```model.py```). -->

---

## Deliverables
* Github Repo w/ Final Notebook and README
* Class Presentation + Slide Deck
* Project description for resume, etc.

---

## Iterations through the Data Science Pipeline

**Pipeline iteration 1:**
* Project plan and timeline
* README outline
* Structure project bones
* Reach the minimum/MVP for each stage to be able to move on to the next stage
    * README
    * Jupyter notebook
    * wrangle.py
    * preprocessing.py
    * explore.py
    * model.py

**Pipeline iteration 2:**
* Recalibrate project plan timeline and goals
* Tidy the data a little further
* Put functions into modules
* Fill out the data dictionary
* Create Google slides

**Pipeline iteration 3:**
* Make README more thorough
* Clarify conclusions
* Make visualizations prettier
* Finetune Google slides
* Practice presentation & type up speaker notes

**Things I'll save for future iterations for the sake of time:**
* Incorporate more of the data, including more features
* Add feature: contestant's hometown's proximity to that season's bachelorette's hometown
* Add feature: Received a first impression rose

---

## Data Dictionary

| Term                     | Definition                                                 | Data type                |
|--------------------------|------------------------------------------------------------|--------------------------|
| Term here                | Definition here                                            | int64                    |
| Term here                | Definition here                                            | float                    |
| Term here                | Definition here                                            | object                   |

---

## Hypotheses

𝐻0: Null Hypo 1<br>
𝐻𝑎: Alt Hypo 1

𝐻0: Null Hypo 2<br>
𝐻𝑎: Alt Hypo 2

---

Instructions for use and reproduction:
## Main notebook
To see and read through the main notebook, you can navigate to ```bachelorette-predictor.ipynb``` in this GitHub repository.

You can explore the functions from the notebook more indepth in the ```wrangle.py```, ```preprocessing.py```, ```explore.py```, and ```model.py``` files.

## Setup

In order to run the code in this repository, you'll need:

1. An installation of python through anaconda
2. A local clone of this repository
<!--3. An ```env.py``` file that defines the following variables:
  - 'user'
  - 'host'
  - 'password'-->

The code in here was developed on MacOS, but should run fine anywhere you can install python + anaconda.

<!--
---

### Big thanks to the following resources for education and inspiration:
* <a href="https://ds.codeup.com/">Codeup curriculum</a>
* <a href="https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9">Simple and Multiple Linear Regression in Python</a>
* <a href="https://geopy.readthedocs.io/en/stable/">GeoPy</a>
* <a href="https://machinelearningmastery.com/model-based-outlier-detection-and-removal-in-python/">4 Automatic Outlier Detection Algorithms in Python</a>
* <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html">Isolation Forest documentation</a>
* <a href="https://towardsdatascience.com/outlier-detection-with-isolation-forest-3d190448d45e">Outlier Detection with Isolation Forest</a>
* <a href="https://www.tablesgenerator.com/markdown_tables#">Markdown Table generator</a>
* <a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.13-geographic-data-with-basemap.html">Geographic Data with Basemap</a>
* <a href="https://medium.com/@samchaaa/preprocessing-why-you-should-generate-polynomial-features-first-before-standardizing-892b4326a91d">Preprocessing: why you should generate polynomial features first before standardizing</a>
* <a href="https://apps.gis.ucla.edu/geodata/en/dataset/world_elevation_contours">World Elevation Contours data from UCLA</a>
* <a href="https://apps.gis.ucla.edu/geodata/dataset/california-public-schools">California school districts data from UCLA</a>
* <a href="https://www.cde.ca.gov/ds/si/ds/pubschls.asp">California school districts from CA's DoE</a>
* <a href="https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1">Understanding K-means Clustering in Machine Learning</a>
* <a href="https://dardenreviews.github.io/">Faith's Darden reviews, of course!</a>
* And extra big thanks to my Codeup Darden cohort colleagues for being a constant source of knowledge, help, and motivation!
-->
