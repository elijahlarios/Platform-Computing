# Metric Tracker with Database

This project tasked us with duplicating our Assignment 2 project and removing the export to csv related functions in the Metric_tracker folder. We then initialize a database to store metrics gathered from our selenium code from the same file. Deliverables include a new readme[^1], images, and all code for the project.

Time spent: **2** hours spent in total

## Features

The following **required** features are completed:

- [X] Organize Github projects for Assignment 3 (2 pts)
- [X] Complete SQL Mystery Walkthrough and take a screenshot or print to PDF the webpage (2 pts)
- [X] Complete Interactive MongoDB Tutorial and take a screenshot or print to PDF the webpage  (2 pts)
- [X] Choose a SQL or NoSQL Database and set up a server[^2] (4 pts)
- [X] Modify your metric_tracker file so that the metrics are saved onto a database (5 pts)

The following **bonus** features are implemented:

- [X] Retrieve values from the database (1 pt).
- [ ] Create separate Tables (SQL) or Documents (NoSQL) for each metric and relate them via user (2 pt).
    - Can be implemented later, but I was unsure of what this fully meant.  
- [X] DESCRIBE ANY OTHER FEATURES HERE.
    - Currently records timestamp of entrance and exit for each user, with metrics for each timestamp.
        - Final timestamp "EXIT" features more information about the webpage, like paragprah contents.

## Screenshot and/or Video Walkthrough
| Description | Image |
| --- | --- |
| SQL Mystery 1 | ![SQL Mystery 1](https://github.com/elijahlarios/Platform-Computing/blob/main/Assignment_3_Database/Images/sql%20mystery%201.png) |
| SQL Mystery 2 | ![SQL Mystery 2](https://github.com/elijahlarios/Platform-Computing/blob/main/Assignment_3_Database/Images/sql%20mystery%202.png) |
| MongoDB | ![MongoDB](https://github.com/elijahlarios/Platform-Computing/blob/main/Assignment_3_Database/Images/mongodb%20tutorial.png) |
| DB Results on Entrance | ![DB Results on Entrance](https://github.com/elijahlarios/Platform-Computing/blob/main/Assignment_3_Database/Images/raw%20results%200.png) |
| DB Results (General) | ![DB Results (General)](https://github.com/elijahlarios/Platform-Computing/blob/main/Assignment_3_Database/Images/raw%20results%201.png) |
| DB Results On Exit | ![DB Results On Exit](https://github.com/elijahlarios/Platform-Computing/blob/main/Assignment_3_Database/Images/raw%20results%202.png) |

### Notes
[^1]: This file was renamed to README.md from A3_Readme.md so that github can parse the file when viewing the Repo
[^2]: The NoSQL database I implemented was Firebase. Each document is an actual timestamp, placed inside of a timestamp collection
