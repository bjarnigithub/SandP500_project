# S&P500vsISK

## Goal of project

-   Create a tool to check the status of an investment in the S&P 500 in Icelandic currency.
-   Compare original investment in ISK to current status in ISK based on ISK-to-dollar/dollar-to-ISK exchange rate because investments in S&P500 are made in dollars.

## Proposed features:

-   get currency exchange rate data ISK-to-dollar/dollar-to-ISK in csv format (see https://www.sedlabanki.is/hagtolur/xml-gogn/)
    -   store the data somewhere and provide code to get new more up-to-date data (and store this new data)
-   get S&P500 data (where?, what data specifically?, S&P500 index ???)
    -   store the data somewhere and provide code to get new more up-to-date data (and store this new data)
-   validate quality of data (use Great Expectations and Pandas)
    -   have tests ready to test new data that is aquired

## Implemented features:

-   ...

## Setup

-   Install necessary tools (e.g. in a conda environment):
    -   Python
    -   Pandas
    -   Great Expectations

## Structure <-???maybe-skip

-   README.md
-   main.py
-   Data/
-   QA/
    -   qa-tests.py
    -   qa-notes.txt
    -   qa-results.txt
