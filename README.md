# Hotel_Managment

<a href="https://jithendra1798.pythonanywhere.com/"><h1 align = "center">Generic Library Managment</h1></a>

## Members
||Name|Roll No|Email|
|---:|:---|:---:|:---|
|1.| Jithendra Puppala | 191CS237 | <jithendra.191cs237@nitk.edu.in> |
|2.| Vamshikrishna M | 191CS261 | <vamshikrishnam.191cs261@nitk.edu.in>|
|3.| Mahadev Hatti  | 191CS133 |<mahadev.191cs133@nitk.edu.in>|
|4.| Keerthana Patil | 191CS231 |<patilkeerthana.191cs231@nitk.edu.in>|
|5.| Harshita | 191CS120 |<harshita.191cs120@nitk.edu.in>|

## Roadmap of the Project
![Roadmap of Hotel Management project image](https://raw.githubusercontent.com/jithendra1798/SE-Project/main/assets/Library%20Roadmap.jpg)

## Project Description
* As the project name suggests automation in which the human input can be minimised and makes the work of librarian a lot easier and experience of user a lot simpler.
* This has some new features like requesting book from other students, buying books from catalogue, if available for sale and reviewing and rating books and feedback of experience etc.  
* We can also track the history of users (books user has taken before and now).  
* We can also track history of books (users who took the book previously and now).  
* It makes library user and librarian work very simpler and easier.  

## Project Design Flow
![Project Design Flow](https://github.com/jithendra1798/SE-Project/blob/main/assets/Project%20Design%20Flow.png)


## Project Requirements/Features

### 1. Admin
 * Add books
 * Confirm registration of user
 * Can see all user details
 * Remove/add users
 * Make others admin
 * Can see the books taken by user
 * Can track history of book (Users used)


### 2. User
> There are 3 types of users
 
|New registration|Active user|Old user|
|:---|:---|:---|
|Registration yet to approve|Registration Approved|User in break/due fine|
|Shows Registration Pending|Can Access completely|Limited access|

#### Active user features :
- Can lend max of 4 books.
- Request other user, if he needs a book taken by other user.
- Pays fine, if he lost the book or delays renewal of book.
- History of books he took.
- Can buy a book, if availabe to sale by another user or by library.
- Can generate and use the Library ID card in PDF
- Can give Feedback of experience while taking books

### 3. Other Features
- Automated emails to users, reminding for renewal of books
- Users can search books in the catalogue
- Lending/Taking books is of 3 categories
    - Take book from Library
    - Take book from other user
    - Buy book, if available for sale
- Automated emails on registration approval/banning/termination
- Automated generation of Library ID cards
- Different types of subscriptions for users

## Software Specifications
|Backend|Frontend|
|:---|:---|
|Django (Python)|HTML|
MySQL(Database)|CSS|
|   |JS|

## Non-Functional Requirements
- Scalability and reliability is taken care by django, as it is simple, highly scalable and flexible.
- Security of the sensitive data transmission of users is taken care by django.
- We designed the database with high data integrity.
- The performance of the application will be good with the optimised queries in MySQL.
- Maintainability and Manageability of the application will be good, as we are following the best Software principles.
- MySQL is capable enough to scale the project to even higher.
- The portability of the application is high, as we are using one of the most popular framework.


## Objectives of Software Engineering: 

1. Maintainability – We are following best software engineering practices. So, it is feasible for the software to evolve to meet changing requirements.
2. Efficiency – The software should not make wasteful use of computing devices such as memory, processor cycles, etc.
3. Correctness – A software product is correct if the different requirements as specified in the SRS document have been correctly implemented.
4. Reusability – A software product has good reusability if the different modules of the product can easily be reused to develop new products.
5. Testability – Here software facilitates both the establishment of test criteria and the evaluation of the software with respect to those criteria.
6. Reliability – It is an attribute of software quality. The extent to which a program can be expected to perform its desired function, over an arbitrary time period.
7. Portability – In this case, the software can be transferred from one computer system or environment to another.
8. Adaptability – In this case, the software allows differing system constraints and the user needs to be satisfied by making changes to the software.
9. Interoperability – Capability of 2 or more functional units to process data cooperatively.


## Hardware Requirements : 
- The following table lists the minimum and recommended hardware requirements for the web application.

|Component|Minimum|Recommended|
|:---|:---|:---|
|Processor|1.9 gigahertz (GHz) x86- or x64-bit dual core processor with SSE2 instruction set|3.3 gigahertz (GHz) or faster 64-bit dual core processor with SSE2 instruction set|
|Memory|2-GB RAM|4-GB RAM or more|
|Display|Super VGA with a resolution of 1024 x 768|Super VGA with a resolution of 1024 x 768|

- The Software application can run in any of the following web browsers running on the specified operating systems:
- Microsoft Edge (latest publicly-released version) running on Windows 10, Window 8.1, Windows 8, Windows 7
- Mozilla Firefox (latest publicly-released version) running on Windows 10, Windows 8.1, Windows 8, or Windows 7, Linux debian distros

- Google Chrome
    - Google Chrome (latest publicly-released version) running on Windows 10, Windows 8.1, Windows 8, Windows 7, Linux debian distros
    - Google Chrome (latest publicly-released version) running on the two latest publicly-release Mac OS versions
- Apple Safari (latest publicly-released version) running on the two latest publicly-release Mac OS versions, or Apple iPad

## Activity Flow Diagram
![Activity Flow Diagram](https://raw.githubusercontent.com/jithendra1798/SE-Project/main/assets/Dataflow1.png)



## Links and Documents
### 1. [Schema Diagram PDF](https://github.com/jithendra1798/SE-Project/blob/main/assets/Tables%20Schema1.pdf)
### 2. [Schema Diagram Document](https://docs.google.com/document/d/1f0tBZoOreObHvXWhmM2hPPdkngzHdIXYdW9x57JuSEk/edit)
### 3. [Schema variables Document](https://docs.google.com/document/d/1xRhhgMQ8qZG436_hzpF3xj-nXgE0rf1wI6bEavzY5KE/edit)
### 4. [Library Project Design Flow](https://whimsical.com/library-8khLqftvQHyXJhb3m7ecsL)
### 5. [Reference e-Library](https://www.edigitallibrary.com/)
### 6. [Embed MySQL in Python/Django](https://www.tutorialspoint.com/python_data_access/python_mysql_introduction.htm)
### 7. [Dynamic Search Field - Django](https://betterprogramming.pub/how-to-make-search-fields-dynamic-in-django-rest-framework-72922bfa1543)
### 8. [Dynamic Search Field 2 - Django](https://openfolder.sh/django-tutorial-as-you-type-search-with-ajax)
### 9. [Python MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)
### 10. [Override Admin Django](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#admin-overriding-templates)
### 11. [Django Messages and Mails](https://www.ordinarycoders.com/blog/article/django-messages-framework)
