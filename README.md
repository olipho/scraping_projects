# Summary of scripts

## running_data
To extract my (and others') data from a well known Saturday morning running event. Creates a dataframe following scraping from multiple pages and pulling in various other elements to label graphs of data and calculate summary statistics. The reason I decided to start this project is because I have completed a large number of events and wanted to view my data in a way that was interesting to me.

This script has already had a major reworking after I originally scraped the data from a summary page as part of my profile which showed my best time for each event.  I realised that taking summary statistics of only my best times was meaningless and so needed to rework it. This followed another project where I learned to scrape several pages at once.

### Summary of features
- Uses a simple input to enter a parkrun id and then scraping that profile page creates a list which takes all of the URLs for each different parkrun they've done (you've done 3 parkruns so that's 3 links in the list)
- Loops through the list and scrapes the person's data from each page, including their name and run data, formatting it from the unstructured soup into a dataframe. I've done this mostly by converting the data into lists and then converting into dataframe form.
- Converts time to seconds to allow some statistical calculations such as mean and standard deviation then converts back to minutes and seconds
- Plots a box and whisker diagram
- I created a query on the dataframe to pick out runs which I did with my son (running with a buggy is slow so it's all the ones over a certain time and after the date he was born) although this doesn't make sense on someone else's data, hence why it's currently empty)
- Creating a summary table of all the person's run data (a bit like parkrun do already but I wanted to do it myself and show what data I wanted). This also involved a simple join of two tables.
- I've then created a bar chart showing how many parkruns have been done at each venue, overlaying it with the best time for each course. 

### Historic versions
The earlier version of this used a script called parkrun_soup.py which did a rough scrape which was saved to a csv file. parkrun1.csv was then cleaned before being imported into event_summary.py after which some viualisations and summary statistics were generated. 

Modules: beautifulsoup, soupstrainer, requests, pandas, re, from itertools import repeat, matplotlib, numpy, datetime, time

How to run (!) - currently in Jupyter Notebooks it's split into cells. I *assume* this will run as a single script in any other normal IDE but this needs to be checked. 

### Challenges in developing the script
- I needed to create a tuple of parkrun years to allow me to remove the \xa0\n and \n tags from the raw data. Moreover, this then allowed me to konw where one row on the table ended and the next started, the year being used to identify when the last element in a row.  
- CSS selectors were tricky as often tables would have the same tags, meaning that two or three tables on the same page. This meant scraping tables with irrelevant data and then looping through to remove the elements in the created list that are not needed.
- The event header at the top of the page shared CSS tags with several other elements on the page. The names of the events needed to be extracted from the footer of the event page, parsing the text from a string. 
- Time data is captured as a string and changing this to a usable format was difficult in finding the right library that would work on the hh:mm:ss format.
- I wanted to reuse the function (DRY) I created to convert seconds and minutes but have not resolved that yet.
- I get a 403 forbidden error when I query my own data because too many pages need to be accessed. It gets picked up as a bot after about 25 requests and I need it to do about ten more. Next step is to learn how to throttle (?) / vary the page request speed so it does not block me every time. 

If I had more time I would resolved some of the bugs I have detailed below, including
- fixing the axis labelling on the graphs involving time which has been a continual challenge
- I would like to be able to scrape all of the pages on my own profile, rather than getting a 403 error after 25 or so pages
- A big thing would be to present this in a front end. I have played around with web frameworks (simple Flask and even simpler Django) but a free hosting service which seemed promising would only allow me to scrape from whitelisted sites. To be continued? However, Jupyter Notebooks in Github currently gives me exactly what I need in terms of sharing my output.

## review_scores
Created to learn how to scrape from multiple pages and put into a single dataframe. The purpose of this scrape allows me to see the most recent Pitchfork review scores showing artist and album title without having to load each page. 

This was the first project I did where I successfully scraped URLs into a list and then looped through the list to scrape each page in turn. It created some (what were at the time) interesting challenges in creating different dataframe columns from data on differing pages. As with the running_data script, extracting the correct elements from a page was tricky at times, but more straight forward here in this case. 

Modules: beautifulsoup, requests, pandas, ...

## Wikipedia
This was an early attempt to get data from a web page. It takes some elements from a table and converts them into a list.





