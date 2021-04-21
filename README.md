# service-assessment-data

Scrapes service assessment data from gov.uk

### Requirements

Python 3.7.0

packages as per requirements.txt

If you want to restore the performance platform data you need docker too probably.


### Scraping the service assessment data

Is fiddly. Basically for each service assessment we want the stage (alpha, beta, etc),
 the date of assessment, whether it passed the assessment or not, and a breakdown of
 each item in the criteria that passed or failed.

 This is made difficult as there are multiple formats for each assessment report
 e.g

 https://www.gov.uk/service-standard-reports/share-a-concern-make-a-complaint-on-care-alpha-assessment

It's made doubly difficult as the service assessment criteria have changed over time. We make an effort to select
the correct set of criteria, but it's not 100% accurate.


### Restoring the performance platform data

The performance platform data is available as a big mongodb dump (ask Zach if you want it) .

The easiest way is to use docker to create a mongodb instance.
the instructions are here: https://github.com/ukgovdatascience/govuk-mongodb-content

In our case we need to restore multiple collections so need this command

Say we have put all the .bson and .json files in a folder called back drop within data/db in our container

`mongorestore -drop -d performance-platform --nsInclude 'performance-platform.*' data/db/backdrop/`

Where `-drop` drops a previous instance, `-d performance-platform` is the name of our new database

`--nsInclude 'performance-platform.*` means restore all the files (aka collections) within the specificied
directory  `data/db/backdrop`

This restores every collection within the specified folder

This is some odd error when you try to restore (at least on mongo 4.4.1) that seems to be caused
by the .json metadata files. I think it's fixed by deleting the options field within those files.
There is a script to do this in:

 `src.utils.json_functions.py`

Nonetheless, many files fail to restore! Oh well
