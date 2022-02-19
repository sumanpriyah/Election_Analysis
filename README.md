# Election_Analysis

## Overview of Election Audit
In this project we need to deliver election results in form of below information as asked by a  Colorado Board of Elections employees for the election Audit of a recent local election.

1	Total number of votes cast

2	A complete list of candidates who received votes

3	Total number of votes each candidate received

4	Percentage of votes each candidate won

5	The winner of the election based on popular vote

6	The voter turnout for each county

7	The percentage of votes from each county out of the total count

8	The county with the highest turnout


## Election-Audit Results
### Total votes cast by candidates for this congressional election were 369,711.

### The number of votes and percentage for each county is below:

Jefferson : 38,855 (10.5%)

Denver : 306,055 (82.8%)

Arapahoe : 24,801 (6.7%)

Denver county has the largest turnout votes with 82.8%  with 306,055 total votes.The lowest percentage votes are in Arapahoe county only 6.7% with 24,801 votes. 

### The total vote count for each candidates and percentage is below:

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

Diana DeGette was the winning candidate with 73.8% and 272892 votes. 

**The election results are attached as png file in Election_Analysis folder.

## Resources

Data Source :election_results.csv

Software:Python 3.9.7, Visula Studiao Code, 1.64.2

## Election-Audit Summary
A) The same script can be used to find out the total votes cast, winning county and winning candiate with number of votes and persentage by changing the path and file names in below places in same script. The below piece of code should have same file 
and  files name provided for any other election data. 

-Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

-Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

B) The other place may be need to make change depending upon csv file provided - candidate name and county name in which row the data is provided. In this case the county name was in row 1 and candiadate name was in row 2 as indext starts from 0

-Get the candidate name from each row.

candidate_name = row[2]

-Extract the county name from each row.

county_name = row[1]
