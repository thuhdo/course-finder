# course-search-fandm

A simple web application that provides multiple course search options for students at Franklin & Marshall College, reducing the need to scroll back and forth and manually search for words in a PDF.

<img src="https://i.imgur.com/yPSonyu.png" width=300>

## The problem
The current steps that students take to look at courses involves downloading and scrolling through a large PDF file. This file gets frequently updated, which requires the students to re-download to see the changes. This has proven to be inconvenient and aggravating the already stressful registering process.

## The solution
A centralized web application where students have multiple searching options to choose from.

<img src="https://i.imgur.com/aCacPwj.jpg" width=300>

## Developed using
- MAMP: provides a simple local web development solution which integrates phpMyAdmin 
- phpMyAdmin: an administration tool for SQL and MariaDB
- HTML & CSS: used to build the web interface
- Python Flask: a micro web framework 

## Walkthrough

### Homepage
Presents a dropdown menu from which the user can specify their searching criteria. The user can navigate to the homepage by clicking on the page title "Course Finder" presented in all child pages.

<img src="https://i.imgur.com/N1davQL.png" width=200>

### Search pages
All of the search pages except for the General Education Requirements one provide the user with fields to input their search values, some of which require the user to input a non-empty string before proceeding, some don’t. All fields have placeholder texts that suggest reasonable values to the user.

<img src="https://i.imgur.com/S1GUkxZ.png" width=100>

#### General Education Requirements page

For the General Education Requirements page, the web presents the user with a dropdown menu instead of text fields due to their complex/nonconforming names and the limited number of options. 

<img src="https://i.imgur.com/YGruSMK.png" width=150>




