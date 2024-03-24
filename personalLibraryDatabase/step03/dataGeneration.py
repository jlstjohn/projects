# Create csv files to use with MySQL
import csv
import os
import random
from collections import namedtuple
import logging
import argparse

parser = argparse.ArgumentParser(description='Create csv files for Personal Library Database')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('dataGeneration.log', 'w')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.addHandler(sh)

class Book:
    def __init__(self, title, author, isbn, subject):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.subject = subject
        #logging.info('Book: init called')

    def __repr__(self):
        return f'{self.title}, {self.author}, {self.isbn}, {self.subject}'
        loggin.info('Book: magic repr called')

    def __str__(self):
        return f'{self.title} by {self.author} on {self.subject} has isbn: {self.isbn}'
        logging.info('Book: magic str called')

    def __hash__(self):
        return hash((self.title, self.author, self.isbn, self.subject))

class GetData:
    def __init__(self):
        self.data = []
        logging.info('GetData: init called')

        self._load_data()

    def __iter__(self):
        return iter(self.data)
        logging.info('GetData: iter called')

    def _load_data(self):
        logging.info('GetData: loading data')

        if not os.path.exists(f'main_dataset_revised.csv'):
            logging.debug('GetData: main_dataset_revised.csv file not found')

        print("loading")
        Record = namedtuple('Record', ['name', 'author', 'isbn', 'category'])

        with open(f'main_dataset_revised.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                #print(row)
                record = Record(*row)
                title = record.name
                author = record.author
                isbn = record.isbn
                subject = record.category

                bookData = Book(title, author, isbn, subject)
                #print(bookData)
                self.data.append(bookData)
        return self.data

def randPages(numBooks):
    logging.info('randPages: generating pages')
    pageList = []
    for i in range(numBooks):
        randPageNum = random.randint(65, 999)
        pageList.append(randPageNum)
    return pageList

def getPeople():
    logging.info('getPeople: generating people')
    nameSample = ['Alice', 'Bob', 'Charlie', 'David', 'Elsa', 'Freya', 'Gaston', 'Hercules']
    datesOutSample = ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07']
    datesReturnedSample = ['2020-03-05', '2020-10-05', '2020-01-12', '2020-02-12', '2020-02-02']
    personList = []

    for i in range(0, 2000):
        name = random.sample(nameSample,1)[0]
        dateOut = random.sample(datesOutSample,1)[0]
        dateReturned = random.sample(datesReturnedSample,1)[0]
        personSample = name + ',' + dateOut + ',' + dateReturned
        personList.append(personSample)
    for j in range(0, 250):
        name = random.sample(nameSample,1)[0]
        dateOut = random.sample(datesOutSample,1)[0]
        personSample = name + ',' + dateOut
        personList.append(personSample)
    return personList

def main():

    homeLibrary = GetData()
    #print(type(homeLibrary))
    numBooks = 0
    for book in homeLibrary:
        numBooks += 1
    print(numBooks)

    # for book in homeLibrary:
    #     print(book)

    # Create Author Database
    logging.info('Main: creating data_authors.csv')
    authorSet = set()
    for book in homeLibrary:
        author = book.author
        authorSet.add(author)
    with open(f'data_authors.csv', 'w') as file:
        for i in authorSet:
            authorCSV = i + '\n'
            file.write(authorCSV)


    # Create and generate num of pages for Book Database
    pageList = randPages(numBooks)

    logging.info('Main: creating data_books.csv')
    with open(f'data_books.csv', 'w') as file:
        p = 0
        for book in homeLibrary:
            isbn = book.isbn
            title = book.title
            pages = pageList[p]
            bookStr = isbn + ',' + title + ',' + str(pages) + '\n'
            p += 1
            file.write(bookStr)

    # Create and generate name, summaries, placement, and outOf categories for Series Database
    logging.info('Main: creating data_series.csv')
    with open(f'data_series.csv', 'w') as file:
        file.write('name' + ',' + 'summary' + ',' + 'placement' + ',' + 'outOf' + '\n')

    # # Create and generate subject and summaries for Subject Database
    logging.info('Main: creating data_subject.csv')
    with open(f'data_subject.csv', 'w') as file:
        num = 0
        for book in homeLibrary:
            subject = book.subject
            summary = book.subject + str(num)
            num += 1
            subjectStr = subject + ',' + summary + '\n'
            file.write(subjectStr)


    # Create and generate names, date outs and date returned for Person Database
    peopleSample = getPeople()
    logging.info('Main: creating data_person.csv')
    with open(f'data_person.csv', 'w') as file:
        for person in peopleSample:
            personStr = person + '\n'
            file.write(personStr)


    # Create join relation between Books and Author Database (Wrote Database), will contain isbn and author name
    logging.info('Main: creating data_wrote.csv')
    with open(f'data_wrote.csv', 'w') as file:
        for book in homeLibrary:
            isbn = book.isbn
            author = book.author
            wroteStr = isbn + ',' + author + '\n'
            file.write(wroteStr)

    # Create join relation between Books and Series Database (partOf Database), will contain isbn and series name
    logging.info('Main: creating data_partOf.csv')
    with open(f'data_partOf.csv', 'w') as file:
        file.write('isbn' + ',' + 'name' + '\n')

    # Create join relation between Books and Subject Database (isAbout Database), will contain isbn and subject
    logging.info('Main: creating data_isAbout.csv')
    with open(f'data_isAbout.csv', 'w') as file:
        for book in homeLibrary:
            isbn = book.isbn
            subject = book.subject
            isAboutStr = isbn + ',' + subject + '\n'
            file.write(isAboutStr)

    # Create join relation between Books and Person Database (Loaned Database), will contain isbn and name of person
    logging.info('Main: creating data_loaned.csv')
    loanedList = []
    while len(loanedList)<2250:
        for book in homeLibrary:
            isbn = book.isbn
            loanedList.append(isbn)
    i = 0
    with open(f'data_loaned.csv', 'w') as file:
        for person in peopleSample:
            loanedStr = loanedList[i] + ',' + person + '\n'
            i += 1
            file.write(loanedStr)

            # TO FIX: NEED TO GET RID OF DATE COLUMNS SHOWING IN CSV OUTPUT

    # Create join relation with Books Database (Read Database), will contain ibsn, timesRead, and rating
    logging.info('Main: creating data_read.csv')
    with open(f'data_read.csv', 'w') as file:
        for book in homeLibrary:
            isbn = book.isbn
            timesRead = random.randint(0, 21)
            rating = random.randint(0, 10)
            readStr = isbn + ',' + str(timesRead) + ',' + str(rating) + '\n'
            file.write(readStr)

            # TO FIX: HEADERS FOR TIMESREAD AND RATING COLUMNS IN CSV OUTPUT
            # IF TIMESREAD == 0, RATING SHOULD == 0
            # WOULD WE WANT NEGATIVE RATING FOR DO NOT READ AGAIN? OR WOULD THAT BE INCLUDED WITH 0?

main()
