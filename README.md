# service-assessment-data

Scrapes service assessment data from gov.uk

### Requirements

Python 3.7.0

packages as per requirements.txt


### Scraping the data

Is fiddly. Basically for each service assessment we want the stage (alpha, beta, etc),
 the date of assessment, whether it passed the assessment or not, and a breakdown of
 each item in the criteria that passed or failed.

 This is made difficult as there are multiple formats for each assessment report
 e.g

 https://www.gov.uk/service-standard-reports/share-a-concern-make-a-complaint-on-care-alpha-assessment

It's made double difficult as the service assessment criteria have changed over time. We make an effort to select
the correct set of criteria, but it's not 100% accurate.
