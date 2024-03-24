# This program uses the mysql connector to utilize python coding in order to add, edit, or
# delete entries in the Subject table of the homelibrary database I have been working with
# through the semester. Output of the code is shown at the bottom of this document.

import mysql.connector
import logging
import argparse

parser = argparse.ArgumentParser(description='Update Summary Table for Personal Library Database')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('Assign08.log', 'w')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.addHandler(sh)

# set up the mysql connection
mydb = mysql.connector.connect(
    user = 'root',
    passwd = '****',
    database = 'homelibrary',
    host = '127.0.0.1',
    allow_local_infile = '1'
)

# set up the cursor
myc = mydb.cursor()

# make sure we are using the correct database
myc.execute("use homelibrary")
logging.info('Program Started')

# Create a while loop that will return the user to the begining once program completes.
# If user input is no, program will quit.
while True:

    # Ask user if they would like to make any changes to the subject table
    userProgRunInput = str(input("Would you like to make any changes within 'Subject'? ")).lower()

    # If yes, user will be asked what kind of changes they would like to make. Add, delete, or edit.
    if userProgRunInput == "yes":
        logging.info('Change request acknowledged.')
        userInputQuestion = str(input("Would you like to add, delete, or edit a subject? ")).lower()

        # Option for adding a subject by entering requested information.
        if userInputQuestion == "add":
            logging.info('Add request acknowledged.')
            userInputAdd1 = str(input("Please enter the new subject: ")).lower().capitalize()
            userInputAdd2 = str(input("Please enter the new subject summary, up to 140 characters: "))
            myc.execute("Insert Into Subject Values (%s,%s)", (userInputAdd1, userInputAdd2,))
            print("Please see the update: ")
            myc.execute("Select * From Subject S Where S.Subject = %s", (userInputAdd1,))
            for x in myc:
                print(x)

        # Option for editing a subject. Asks user to select which subject to change.
        if userInputQuestion == "edit":
            logging.info('Edit request acknowledged.')
            userInputSubjSelct = str(input("Please enter the subject which you would like to edit: "))

            # Prints the selected subject information.
            myc.execute("Select * From Subject S Where S.Subject = %s", (userInputSubjSelct,))
            for x in myc:
                print(x)

            # Asks user to select which subject attribute they wish to update.
            userInputAttrSelct = str(input("Please enter the attribute you would like to edit. Your choices are: Subject, Summary. ")).lower()
            if userInputAttrSelct == "subject":
                userInputSubjEdit = str(input("Please enter the new subject entry so it gets changed, up to 20 characters: "))
                myc.execute("Update Subject SET Subject = %s where Subject.subject = %s", (userInputSubjEdit, userInputSubjSelct,))
                print("Please see the update: ")
                myc.execute("Select * From Subject S Where S.Subject = %s", (userInputSubjEdit,))
                for x in myc:
                    print(x)
            elif userInputAttrSelct == "summary":
                userInputSumEdit = str(input("Please enter the new summary for the selected subject so it gets changed, up to 140 characters. "))
                myc.execute("Update Subject SET summary = %s Where Subject.subject = %s", (userInputSumEdit, userInputSubjSelct,))
                print("Please see the update: ")
                myc.execute("Select * From Subject S Where S.Subject = %s", (userInputSubjSelct,))
                for x in myc:
                    print(x)
            else:
                break

        # Option for deleting a subject by typing in the subject.
        if userInputQuestion == "delete":
            logging.info('Delete request acknowledged.')
            userInputDeletion = str(input("Please enter the subject you wish to delete: "))
            myc.execute("Delete from Subject S Where S.Subject = %s", (userInputDeletion,))
            print("Subject has been deleted.")

        else:
            logging.info('Invalid input recieved.')
            userInputQuestion = str(input("Not a valid option. Please answer add/delete/edit: ")).lower()

    # If no, user will be thanked and program will quit.
    elif userProgRunInput == "no":
        logging.info('Change request declined.')
        print("Thank you.")
        break

    # If invalid input used, user will be prompted again for proper input.
    else:
        logging.info('Invalid input recieved.')
        userProgRunInput = str(input("Not a valid option. Please answer yes/no. "))

mydb.commit()
mydb.close()


### OUTPUT ###

# First run through, testing invalid option and option no.
# C:\Users\farrj\Documents\Scripts\COMP3421\Week08>python Assign08.py
# package: mysql.connector.plugins
# plugin_name: caching_sha2_password
# AUTHENTICATION_PLUGIN_CLASS: MySQLCachingSHA2PasswordAuthPlugin
# Program Started
# Would you like to make any changes within 'Subject'? huh              # invalid input
# Invalid input recieved.
# Not a valid option. Please answer yes/no. no                          # option 'no'
# Would you like to make any changes within 'Subject'? no
# Change request declined.
# Thank you.

# Second run through, testing add, edit, and delete options.
# C:\Users\farrj\Documents\Scripts\COMP3421\Week08>python Assign08.py
# package: mysql.connector.plugins
# plugin_name: caching_sha2_password
# AUTHENTICATION_PLUGIN_CLASS: MySQLCachingSHA2PasswordAuthPlugin
# Program Started
# Would you like to make any changes within 'Subject'? yes                  # option 'yes'
# Change request acknowledged.
# Would you like to add, delete, or edit a subject? add                     # option 'add'
# Add request acknowledged.
# Please enter the new subject: test66                                      # adding new subject: "test66"
# Please enter the new subject summary, up to 140 characters: test66summary     # new summary: "test66summary"
# Please see the update:
# ('Test66', 'test66summary')
# Invalid input recieved.                                                       # need to fix looping here
# Not a valid option. Please answer add/delete/edit: edit
# Would you like to make any changes within 'Subject'? yes
# Change request acknowledged.
# Would you like to add, delete, or edit a subject? edit                        # option 'edit'
# Edit request acknowledged.
# Please enter the subject which you would like to edit: test66                 # selecting "test66" to edit
# ('Test66', 'test66summary')
# Please enter the attribute you would like to edit. Your choices are: Subject, Summary. summary
# Please enter the new summary for the selected subject so it gets changed, up to 140 characters. summary66 for test66      # new summary for test66
# Please see the update:
# ('Test66', 'summary66 for test66')
# Invalid input recieved.                                                       # need to fix looping here as well
# Not a valid option. Please answer add/delete/edit:
# Would you like to make any changes within 'Subject'? yes
# Change request acknowledged.
# Would you like to add, delete, or edit a subject? delete                      # option 'delete'
# Delete request acknowledged.
# Please enter the subject you wish to delete: test66                           # selecting "test66" to delete
# Subject has been deleted.
# Would you like to make any changes within 'Subject'? yes
# Change request acknowledged.
# Would you like to add, delete, or edit a subject? edit
# Edit request acknowledged.
# Please enter the subject which you would like to edit: test66
# Please enter the attribute you would like to edit. Your choices are: Subject, Summary. summary
# Please enter the new summary for the selected subject so it gets changed, up to 140 characters. will this work?
# Please see the update:
# Invalid input recieved.                                                       # response to trying to update a deleted, and therefore nonexistant,
# Not a valid option. Please answer add/delete/edit: no                         # entry
# Would you like to make any changes within 'Subject'? no
# Change request declined.
# Thank you.
