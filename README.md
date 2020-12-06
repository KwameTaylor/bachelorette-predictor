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

## Data Dictionary

| Term                     | Definition                                                 | Data type                |
|--------------------------|------------------------------------------------------------|--------------------------|
| Term here                | Definition here                                            | int64                    |
| Term here                | Definition here                                            | float                    |
| Term here                | Definition here                                            | object                   |

---

## Hypotheses

𝐻0: There is no linear correlation between a contestant's One-on-One Score and a contestant's Elimination Week.<br>
𝐻𝑎: There is a linear correlation between a contestant's One-on-One Score and a contestant's Elimination Week.

---

## Predictive Modeling

| # | Model | Features Used | RMSE on train | RMSE on validate | RMSE on test |
|---|-------|---------------|---------------|------------------|--------------|
| 1 |       |               |               |                  |              |
| 2 |       |               |               |                  |              |
| 3 |       |               |               |                  |              |

---

## Project Plan

|    Date    |                                Goal                               |     Finished?     |
|:----------:|:-----------------------------------------------------------------:|:-----------------:|
| 12/3/2020 | Finish project planning and start MVP.                            |<ul><li>- [x] </li>
| 12/4/2020 | Finish the project MVP with modules.                              |<ul><li>- [x] </li>
| 12/5/2020 | Finish second pipeline iteration, with presentation begun.        |<ul><li>- [ ] </li>
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
  <summary>**Pipeline iteration 1:**</summary>
  
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
* Incorporate more of the existing data
* Create function to cache modified data
* Add feature: contestant's hometown's proximity to that season's bachelorette's hometown
* Add feature: Received a first impression rose
* Add analysis of the data as a time series (sampled by week)
* Go back to the joining of the two dataframes and recover the lost 18 observations (because of mismatched key pairs)
* Incorporate data from the Bachelor
<!-- cute[cute['ElimWeek'] == 11.0] is missing season's 6 and 7. -->
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
* <a href="https://www.kaggle.com/jasminedogu/bachelorettedataset">jasminedogu</a>'s Bachelorette data on Kaggle
* The <a href="https://codeup.com/">Codeup</a> data science curriculum
* <a href="https://abc.com/shows/the-bachelorette">ABC's The Bachelorette</a>!
* The <a href="https://bachelor-nation.fandom.com/wiki/Bachelor_Nation_Wiki">Bachelor Nation Wiki</a>
* <a href="https://www.kaggle.com/fivethirtyeight/fivethirtyeight-bachelorette-dataset">FiveThirtyEight and ABC</a> for their work in collecting the data I used in this project
* <a href="https://alexjs.com/">Alex</a> (via the alexLinter extension on VS Code) for helping me catch insensitive and inconsiderate writing in my README
* Faith's <a href="https://dardenreviews.github.io/">Darden reviews</a>
* Zach's <a href="https://github.com/zgulde/hlre">hlre</a> tool (useful for highlighting regular expressions)
* <a href="https://stats.stackexchange.com/questions/282803/response-is-an-integer-should-i-use-classification-or-regression">This post on Stats StackExchange</a>, which helped me decide whether to use classification or regression
* <a href="https://www.bachelornationdata.com/">Bachelor Nation Data</a>
* This <a href="https://www.vice.com/en/article/qvdbem/using-data-to-predict-this-seasons-winner-of-the-bachelor">Vice</a> article
* <a href="https://www.thrillist.com/entertainment/nation/height-chart-the-bachelorette-bachelor-contestants">This article</a> on Thrillist
* The <a href="https://stoltzmaniac.shinyapps.io/TheBacheloretteApp/">Bachelorette App</a> Dashboard, accompanied by <a href="https://www.r-bloggers.com/2020/10/the-bachelorette-ep-1-every-has-its-thorn-data-analysis-in-r/">this</a> writeup
* <a href="http://www.tortureddata.com/tag/bachelorette/">Does Your Salary Influence Your Chances of Winning the Bachelor/Bachelorette?</a>
* This <a href="https://www.cnn.com/interactive/2019/05/entertainment/bachelorette-numbers/index.html">interactive dashboard</a> about roses and dates
* And extra big thanks to the Codeup data science instructors and my Darden cohort colleagues for being constant sources of knowledge, help, and motivation!
<!-- https://adashofdata.com/2015/02/18/the-data-behind-the-bachelor-the-bachelorette/ -->