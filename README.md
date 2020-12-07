# The Bachelorette Predictor
### Kwame V. Taylor

The goal of this project is to create a machine learning model that accurately predicts how many weeks a contestant will last on the ABC reality show The Bachelorette, based on data from Seasons 1-2 and 4-12.

A note on transparency -- I have not seen any of the above selected seasons of the show. I have, however, seen Season 15 of The Bachelorette, and I am currently watching Season 16. <!--I have left Season 13 and 14 out of the data for the sake of time efficiency, as I would have to scrape that data myself from the Bachelor Nation Wiki, since the FiveThirtyEight data has not been updated past Season 13.--> I may include Seasons 3, 13, and 14 in a future iteration of this project.

**Warning: This project contains *many* spoilers for past seasons.** Proceed at your own risk.

<img src="https://static.tumblr.com/c8504796ecc695283d1e8af5c7f137c9/oig2scu/qjlo45s32/tumblr_static_8e9p6wr2jy0wks8c4004w8k4s.png">

---

## Background

From [Wikipedia](https://en.wikipedia.org/wiki/The_Bachelorette):
> ***The Bachelorette*** is an American reality television dating game show that debuted on ABC on January 8, 2003. The show is a spin-off of The Bachelor and the staple part of The Bachelor franchise. The first season featured Trista Rehn, the runner-up from the first season of The Bachelor, offering the opportunity for Rehn to choose a [spouse] among 25 bachelors.

> All of the rules are adapted from the rules of The Bachelor—its parent show. As the name implies, the series revolves around a single bachelorette, usually a former contestant from the previous Bachelor season, and a pool of romantic interests [...] which could include a potential [spouse] for the bachelorette; it is essentially a gender-reversed version of the parent show. The show starts with the bachelorette standing in front of the mansion and greeting each contestant individually, as they make an entrance to the bachelorette. After each rose ceremony, at least one contestant does not receive a rose and goes home; therefore, the pool of contenders gets smaller, and eventually leaves the bachelorette to decide between two contestants in the final rose ceremony.

> For the final selection, one of two male suitors proposes to the bachelorette. Unlike its parent show, all fifteen seasons of The Bachelorette have ended with a proposal which the bachelorette either accepted or declined.

[![9 Things You’ve ALWAYS Wanted To Know About The Bachelor](https://img.youtube.com/vi/p-Jr8iNdXOQ/0.jpg)](https://www.youtube.com/watch?v=p-Jr8iNdXOQ)

9 Things You’ve ALWAYS Wanted To Know About The Bachelor

---

## Data Dictionaries

| Term                     | Definition                                                 | Data type                |
|--------------------------|------------------------------------------------------------|--------------------------|
| Age                      | The contestant's age at the start of the season            | int64                    |
| ElimWeek                 | The week that the contestant was eliminated from the show. | float64                  |
| Season                   | The season of the show that the contestant was on.         | object                   |
| Dates2-OneonOneScore, Dates3-OneonOneScore     | A constestant's calculated One-on-One Score for that week. Equal to 1 divided by the number of contestants on a date. i.e., a One-on-One would have a score of 1.            | float32                  |
| One-on-One_Score         | Equal to a contestant's average One-on-One score from all weeks they were on the show. | float64                  |
| FirstDate                | A boolean of whether a contestant went on a date in Week 2, which is the first week of dates with the Bachelorette.      | float64           |
| N                 | A boolean of whether the contestant's Hometown is in the Midwest region of the United States. | uint8                  |
| N                 | A boolean of whether the contestant's Hometown is in the North East region of the United States. | uint8                  |
| O                   | A boolean of whether the contestant's Hometown is in a 'Other' region of the United States. | uint8                  |
| S                 | A boolean of whether the contestant's Hometown is in the South region of the United States. | uint8                  |
| W                   | A boolean of whether the contestant's Hometown is in the West region of the United States. | uint8                  |
| Other                      | A boolean of whether the contestant's Hometown is outside of the United States. | uint8                  |          |

Feature         | Description
----------------|------------
`ELIMINATION-1` | Who was eliminated in week 1
`ELIMINATION-2` | Who was eliminated in week 2
`ELIMINATION-3` | Who was eliminated in week 3
`ELIMINATION-4` | Who was eliminated in week 4
`ELIMINATION-5` | Who was eliminated in week 5
`ELIMINATION-6` | Who was eliminated in week 6
`ELIMINATION-7` | Who was eliminated in week 7
`ELIMINATION-8` | Who was eliminated in week 8
`ELIMINATION-9` | Who was eliminated in week 9
`ELIMINATION-10`| Who was eliminated in week 10
`DATES-1`       | Who was on which date in week 1
`DATES-2`       | Who was on which date in week 2
`DATES-3`       | Who was on which date in week 3
`DATES-4`       | Who was on which date in week 4
`DATES-5`       | Who was on which date in week 5
`DATES-6`       | Who was on which date in week 6
`DATES-7`       | Who was on which date in week 7
`DATES-8`       | Who was on which date in week 8
`DATES-9`       | Who was on which date in week 9
`DATES-10`      | Who was on which date in week 10

- Eliminates connote either an elimination (starts with "E") or a rose (starts with "R").
- Eliminations supercede roses.
- "E" connotes a standard elimination, typically at a rose ceremony. "EQ" means the contestant quits. "EF" means the contestant was fired by production. "ED" connotes a date elimination. "EU" connotes an unscheduled elimination, one that takes place at a time outside of a date or rose ceremony.
- "R" means the contestant received a rose. "R1" means the contestant got a first impression rose.
- "D1" means a one-on-one date, "D2" means a 2-on-1, "D3" means a 3-on-1 group date, and so on.
- Weeks of the show are deliminated by rose ceremonies, and may not line up exactly with episodes.

---

## Hypotheses

𝐻0: There is no linear correlation between a contestant's One-on-One Score and a contestant's Elimination Week.<br>
𝐻𝑎: There is a linear correlation between a contestant's One-on-One Score and a contestant's Elimination Week.

---

<!--## Predictive Modeling

| # | Model | Features Used | RMSE on train | RMSE on validate | RMSE on test |
|---|-------|---------------|---------------|------------------|--------------|
| 1 |       |               |               |                  |              |
| 2 |       |               |               |                  |              |
| 3 |       |               |               |                  |              |

---

## Conclusions and Findings

* Findings

---
-->
## Project Plan

|    Date    |                                Goal                               |     Finished?     |
|:----------:|:-----------------------------------------------------------------:|:-----------------:|
| 12/3/2020 | Finish project planning and start MVP.                            |<ul><li>- [x] </li>
| 12/4/2020 | Finish the project MVP with modules.                              |<ul><li>- [x] </li>
| 12/5/2020 | Finish second pipeline iteration, with presentation begun.        |<ul><li>- [x] </li>
| 12/6/2020 | Finish presentation, practice, exercise, meditate, sleep.         |<ul><li>- [ ] </li>
| 12/7/2020 | Presentation day!                                                 |<ul><li>- [ ] </li>

<!-- The project deliverables are the following: **Jupyter Notebook** data science pipeline walkthrough with **conclusions**, data **visualizations**, **README**, and **modules with functions** (```wrangle.py```, ```preprocessing.py```, ```explore.py```, and ```model.py```). -->

---

## Deliverables
* Github Repo w/ Final Notebook and README
* Class Presentation + Slide Deck
* Project description for resume, etc.

---

## Iterations through the Data Science Pipeline

<details>
  <summary>Pipeline iteration 1:</summary>
  
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
</details>

<details>
  <summary>Pipeline iteration 2:</summary>
  
* Recalibrate project plan timeline and goals
* Tidy the data a little further
* Put functions into modules
* Fill out the data dictionary
* Create Google slides
</details>

<details>
  <summary>Pipeline iteration 3:</summary>
  
* Make README more thorough
* Clarify conclusions
* Make visualizations prettier
* Finetune Google slides
* Practice presentation & type up speaker notes
</details>

<details>
  <summary>Things I'll save for future iterations for the sake of time:</summary>

* Incorporate more of the existing data
* Create function to cache modified data
* Add feature: contestant's hometown's proximity to that season's bachelorette's hometown
* Add feature: Received a first impression rose
* In the future I'd like to analyze this as a time series, sampled by week and divided by season
* Go back to the joining of the two dataframes and recover the lost 18 observations (because of mismatched key pairs)
* Incorporate data from the Bachelor
* Join data about each contestant's corresponding bachelorette from their season, such as Age and HomeRegion
* Utilize clustering in feature engineering
* Deploy predictor as a software product
* Tune the hyperparameters of my Random Forest Regressor and use Grid-Search
* Use my best model to predict on the current season of The Bachelorette (I haven't seen past episode three yet :D)
* Add visual to my data dictionary for my engineered features
</details>

---

Instructions for use and reproduction:
## Main notebook
To see and read through the main notebook, you can navigate to ```bachelorette-predictor.ipynb``` in this GitHub repository.

You can explore the functions from the notebooks more concisely in the ```wrangle.py```, ```preprocessing.py```, ```explore.py```, and ```model.py``` files.

You can read about my thought process for this project more indepth, if you'd like, in the corresponding ```.ipynb``` files for ```wrangle```, ```preprocessing```, ```explore```, and ```model```.

## Setup

In order to run the code in this repository, you'll need to:

1. Have an installation of python through anaconda
2. Clone this repository
3. Copy or move the .csv files from ```kaggle-datasets/``` and ```kaggle-datasets/FiveThirtyEight/``` into the main repository folder
<!--3. An ```env.py``` file that defines the following variables:
  - 'user'
  - 'host'
  - 'password'-->

The code in here was developed on MacOS, but should run fine anywhere you can install python + anaconda.

---

### Big thanks to the following resources for resources, education, and inspiration:
* <a href="https://abc.com/shows/the-bachelorette">ABC's The Bachelorette</a>!
* The <a href="https://bachelor-nation.fandom.com/wiki/Bachelor_Nation_Wiki">Bachelor Nation Wiki</a>
* <a href="https://www.kaggle.com/fivethirtyeight/fivethirtyeight-bachelorette-dataset">FiveThirtyEight and ABC</a> and Kaggle user <a href="https://www.kaggle.com/brianbgonz/the-bachelorette-contestants">brianbgonz</a> for their work in collecting the data I used in this project
* <a href="https://www.kaggle.com/jasminedogu/bachelorettedataset">jasminedogu</a>'s Bachelorette data on Kaggle
* The <a href="https://codeup.com/">Codeup</a> data science curriculum
* <a href="https://alexjs.com/">Alex</a> (via the alexLinter extension on VS Code) for helping me catch insensitive and inconsiderate writing in my README
* Faith's <a href="https://dardenreviews.github.io/">Darden reviews</a>
* Zach's <a href="https://github.com/zgulde/hlre">hlre</a> tool (useful for highlighting regular expressions)
* Jackson Killian's <a href="https://code.activestate.com/recipes/580661-states-to-regions/">States to Regions</a> python dictionary that I used
* <a href="https://stats.stackexchange.com/questions/282803/response-is-an-integer-should-i-use-classification-or-regression">This post on Stats StackExchange</a>, which helped me decide whether to use classification or regression
* <a href="https://www.bachelornationdata.com/">Bachelor Nation Data</a>
* This <a href="https://www.vice.com/en/article/qvdbem/using-data-to-predict-this-seasons-winner-of-the-bachelor">Vice</a> article
* <a href="https://www.thrillist.com/entertainment/nation/height-chart-the-bachelorette-bachelor-contestants">This article</a> on Thrillist
* The <a href="https://stoltzmaniac.shinyapps.io/TheBacheloretteApp/">Bachelorette App</a> Dashboard, accompanied by <a href="https://www.r-bloggers.com/2020/10/the-bachelorette-ep-1-every-has-its-thorn-data-analysis-in-r/">this</a> writeup
* <a href="http://www.tortureddata.com/tag/bachelorette/">Does Your Salary Influence Your Chances of Winning the Bachelor/Bachelorette?</a>
* This <a href="https://www.cnn.com/interactive/2019/05/entertainment/bachelorette-numbers/index.html">interactive dashboard</a> about roses and dates
* And extra big thanks to the Codeup data science instructors and my Darden cohort colleagues for being constant sources of knowledge, help, and motivation!
<!-- https://adashofdata.com/2015/02/18/the-data-behind-the-bachelor-the-bachelorette/ -->
<!-- cute[cute['ElimWeek'] == 11.0] is missing season's 6 and 7. -->