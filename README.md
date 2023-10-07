# 2020 NZ Election Results

## Party Votes by Voting Place

(includes votes not made at traditional voting places)

### Description

These scripts generate cleaned, collated CSV and HTML tabular output from a set of 72 CSVs containing party vote data by voting place for the 2020 NZ election.

The input CSVs were retrieved (by hand, grr cloudfront) from https://www.electionresults.govt.nz/electionresults_2020/statistics/votes-by-voting-place-electorate-index.html

### Data

The data is already generated and available in the [output](output) directory. For methodology and script help, see below

### Methodology

Inputs are cleaned with `clean_csvs.py`:

1. Electorate name is extracted from row 2
1. Blank lines, single column rows, and rows containing only totals for the entire electorate are discarded.
2. Column headers added for Electorate, Address 1, Address 2
2. Electorate name added to each non-header row
3. Explicit Address 1 of "Non-place" is added for lines that are not at actual places with addresses

Two cleaned input CSVs are produced: one that includes electorate total rows, and one that doesn't

**See**: [input/cleaned/](input/cleaned/) and [input/cleaned_no_totals/](input/cleaned_no_totals/) 

Cleaned inputs are read with pandas python module in `main.py`:

1. Address 1 col is filled down if blank/NaN
2. Frames are collated and concatenated to single data frame

Output CSV and HTML files are written to [output](output) with totals and without.

### Running the script

You will need: Python 3 and a git client. I've only tested on Linux - if you use Windows you might need to fix my paths for Windows directory delimiters

1. Clone this repository eg `git clone `
2. (optional) activate new or preferred virtualenv
3. Install requirements with `pip install -r requirements.txt`
4. Run `python clean_csvs.py` to clean the input CSVs and produce newly cleaned input CSVs
5. Run `python main.py` to read cleaned CSVs and produce new output CSV and HTML files

### Rights

CSVs are all open govt data and should be Public Domain / CC-0.

Code is licensed under the BSD 3-Clause license, see [LICENSE.txt](LICENSE.txt)