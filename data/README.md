# Data set folder

This directory contains the following data.

## SNB Money-market Rate Data

- File Name:  snb-data-zimoma-en-all-20200901_1437.csv
- Data: Money market rates, breakdown by term and exchange
- Source: https://data.snb.ch/en/topics/ziredev#!/cube/zimoma
- Date downloaded: 16 Sep 2020, 19:15
- Used in: 
    - day 1, Ex 1 and 2.
    - day 2, Ex 1.


Data on the money-market rates over various terms, including: overnight (SARON), call money rate (1TGT), 1, 3, 6, and 12-month CHF-denominated loans (1M, 3M0, 6M, 12M, respectively), and USD, JPY, GBP, and EUR-denominated loans (3M1, 3M2, 3M3, and 3M4, respectively). 


- **SARON (Swiss Average Rate Overnight)**: overnight interest rate of the secured funding market for the Swiss Franc.
- **Call money rate**: rate at which short term funds are borrowed and lent in the money market. 
- **USD**: United States of America dollars
- **JPY**: Japanese yen
- **GBP**: British pound sterling
- **EUR**: Euro

## MPG (Mileage per gallon) performances of various cars dataset

Data about a selection of automobiles in two years: 1999 and 2008. 
Includes information about the manufacturer and model of each car, as well as data on the type of car (class), 
the size of the engine (displ, cyl), the type of transmission (trans), 
and city and highway fuel efficiency (cty, hwy) in miles/gallon of fuel units. 


- file name: mpg.csv
- Data: Car fuel efficiency
- Source: https://raw.githubusercontent.com/tidyverse/ggplot2/master/data-raw/mpg.csv
- Used in: 
    - day 1, Ex 3, 4, 5.
    - day 2, Ex 2, 3.

## Antibiotics Data

Data on the dosage of antibiotic (mic or minimum inhibitory concentration in 𝜇g/ml) necessary to kill various bacteria, 
and the gram-type of each bacterium.


- File Name: burtin.json
- Data: Antibiotics Efficacy
- Source: https://mbostock.github.io/protovis/ex/antibiotics-burtin.html
- Import: pd.read_json('burtin.json', orient='records')
- Used in: day 1, Ex 4, 5, 6.


# Anscombe's Quartet


Synthetic data with some strange properties, made up of four data sets. Contains three columns, dataset, to identify which dataset each row belongs to, and x, and y values.

- File Name: anscombe.csv
- Data: Anscombe's Quartet
- Source: From Seaborn
- Structure: 3 columns -- dataset, x, y
- used in: day 2,  Ex 4.

# Mortality Data


Data on the daily number of deaths in France from 1 Jan, 2000 to 18 May, 2020. The columns month and day are the month and day of the data, the columns 2000-2020 are the data for those years.

- File Name: morts_2020-05-18.csv
- Data: Count of daily deaths in France from 1 Jan 2000 to 18 May 2020
- Source: http://coulmont.com/blog/2020/04/24/2020-une-mortalite-specifique/
- Used in: day 2, Ex 5.