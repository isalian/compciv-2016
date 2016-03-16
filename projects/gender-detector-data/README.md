# Gender Detector Project:
# A Gendered Analysis of Federal Judge Data
---

This project aims to analyze data on U.S. federal judges since 1789 to find interesting statistics about the gender distribution of the federal judiciary.

## Introduction

The data being is used a publicly available file from the Federal Judicial Center. It represents all presidentially-appointed judges who have served on a federal court between 1789-present. Federal courts include: U.S. District Courts, the U.S. Courts of Appeals, the Supreme Court of the United States, former U.S. Circuit Courts, and courts of special jurisdiction.

Since the dataset also included information on the race/ethnicity of the judicial appointees and the political party of the president who appointed them, I wanted to analyze how these variables interact. I hypothesized that there will be much fewer females than males in the judiciary overall, and fewer minorities than white judges. I also wanted to test my hypothesis that amongst the minority judges, the gender gap would still exist. I was also curious to find out whether there would be more female judges appointed by Democrats than by Republicans.

Each of these hypothesis was confirmed in the below analysis: only 14% of federal judges since 1789 have been female, while just 3% have been both female and minorities (10% of the total judges were minorities). And Democratic presidents have appointed twice as many female judges as Republican presidents. 

## Methodology and Caveats

This dataset came from the [Federal Judicial Center](http://www.fjc.gov/history/home.nsf/page/about_judges.html) in the form of a CSV file, which you can view [here](http://www.fjc.gov/history/export/jb.txt). The dataset is of roughly 4,000 data records, and this project uses the entire set.

The dataset has a large number of data fields, some messier than other, which are pared down in one of this repo's scripts. The original data includes full name, birth year, death year, date of various judicial appointments, gender, race/ethnicity, Senate vote information, court name, and party affiliation of the president who appointed the judge, among many more.

While the public dataset already includes gender data for federal judges, an imperfect gender classification function has been used to determine which judges' names are male or female. By comparing the detected gender data with the already available data, I determined that the program in this repo was 94% accurate on this datset.

Since the dataset already separated out each judge's name into first, middle, and last name, I simply had to access the "First Name" field of the CSV to find a usable name for the gender detector to read. There were a couple challenges, listed below, so those entries were excluded from the analysis (a total of 158 entries).

The analysis was limited to judges with a full first name listed, not just a first initial (ex. "J.L." instead of "James Lawrence"). It was also limited by excluding names of individuals who went by their first initial but had full first name entries. Those entries were formatted like so: `J[ames]`. With more time and expertise, I would have deleted the brackets and extracted a usable name that way, but for the purposes of this analysis those names are filtered out of the dataset. 

## Past Research and Articles

One only has to look at the Supreme Court of the United States to see that the judicial branch has a gender bias--[one that may not be changing anytime soon](http://lawnewz.com/high-profile/white-house-down-to-three-candidates-for-supreme-court/), according to President Obama's supposed nominee list for Justice Scalia's replacement. Not to mention Republican congressmen's vow to [block any new SCOTUS nominee by Obama](http://www.pfaw.org/press-releases/2016/03/edit-memo-not-just-supreme-court-republicans-blockade-judicial-nominees-start), whoever he or she may be.

This isn't just a problem with judges, it's [prevalent in the field of law](https://bol.bna.com/big-law-gender-parity-initiative-picks-up-momentum/) generally. But there's better data on judges, so that's what we'll analyze here.

Despite the fact that [women's representation in law school student bodies has approached 50%](http://nwlc.org/resources/women-federal-judiciary-still-long-way-go/), the federal bench is much less diverse--presenting challenges in cases that impact the lives of women and girls, such as issues of sex discrimination, birth control, and abortion. 

It should be noted that [Obama has appointed several women to federal courts](http://nwlc.org/resources/women-federal-judiciary-still-long-way-go/), including women of color, who are especially poorly represented on judicial benches. But nationwide, [minorities remain a fraction of the members on judicial benches](http://netnebraska.org/article/news/947196/number-gender-court-appointments-part-heineman-judicial-legacy).

In 2014, there were [328 women on the federal bench compared to 442 men](http://www.thegazette.com/2011/10/23/judicial-branch-lacks-gender-diversity). With today's judicial statistics still catching up to gender bias, I was interested to see what overall statistics looked like--since the judiciary has been around since 1789, _long_ before women could even vote.

## How to Use It

To clone this repo from GitHub, run this:

`git clone https://github.com/isalian/compciv-2016/tree/master/projects/gender-detector-data`

It will create a folder named `gender-detector-data`. Run the following scripts from that folder in this order:

### fetch_data.py

Fetches the biographical data of all federal judges since 1789 as a CSV, saves in a `tempdata` folder.

### wrangle_data.py

Creates a new CSV of wrangled data, cleaning up the number of data fields so it only includes: `firstname`, `lastname`, `birthyear`, `gender`, `race`, `party`. 

### fetch_gender_data.py

Downloads and unzips baby name data from the [Social Security administration](https://www.ssa.gov/oact/babynames/limits.html) into the `tempdata` directory.

### wrangle_gender_data.py

Selects baby  name records for every 10 years between 1950 and 2010, and adds the 2014 records. Stores these records in both CSV and JSON form, with the following data fields for each name: `name`, `gender` , `females', `males`, `ratio` , `total`

### classify.py

Extracts usable first names from the wrangled_data.csv using the `firstname` field. Runs the `detect_gender()` function on all names except those where the `firstname` field contains simply a first initial or a name in this format: `x[abcdef]`. 

Produces a new classified_data.csv identical to the wrangled_data.csv with the addition of 3 columns:

* `detected_gender`: 
* `usable_name`: the extracted name used by the `detect_gender` function
* `ratio`: the ratio of girls vs. boys with a given name

### analyze.py

Reads the classified data to compile statistics on three fronts: overall gender ratio, gender and minority ratio, and gender percentages for Democratic and Republican appointees.

### Other files

The following supporting file doesn't have to be run, but is called by other scripts in the repo.

### gender.py

Contains a `detect_gender()` function which uses the wrangled gender data created in the previous script.

## Analysis

The following statists were calculated using the gender data as well as two additional variables in the data set-- race/ethnicity and political party affiliation.

* Overall gender ratio
* Gender and minority ratios
* Gender ratio per party affiliation

Between 1789 and today, the gender detector found that just **427 females** have served on a federal bench, compared to **2989 males**.

When looking at data on minorities (non-Whites) on federal courts, roughly **10% of federal judges in history have been of a minority race/ethnicity**. Only **3% have been both female and a minority**, and thus a gender gap still exists within the minority federal judges--**27% of minority judges have been female**.

Federal judges are all appointed by the president. Since 1789, **8% of Republican judicial appointees have been female**, half the rate of **female Democratic judicial appointees: 16%**.

The script also compared the datasets's gender data against this repo's imperfect gender detector, and found it was inaccurate or unable to conduct a gender analysis on 6% of names, resulting in a 94% accuracy rate.

Here is a copy of the results printed by **analyze.py**:

```
-----------------
Total gender ratio for judges:
F: 427 M: 2989 NA: 158
14% of federal judges since 1789 have been female
-----------------
Minority judges by gender:
F: 95 M: 251
Total non-White judges since 1789: 346 out of 3574
3% of federal judges since 1789 have been female minorities
27% of federal _minority_ judges since 1789 have also been female
-----------------
Gender ratio for judges by president's political party:
16% of Democratic judicial appointees since 1789 have been famle
8% of Republican judicial appointees since 1789 have been female
-----------------
Accuracy of this program:
There were 207 total incorrect gender reading sby this program
This program was 94% accurate at detecting a judge's gender`
```