# library used to work with CSV files
import csv

# "with" cmakes sure our code behaves even though
# we're interacting with an outside file.
# For example, it makes sure that we close the file
# when we're done with it, without us having to close it ourselves
with open('titanic.csv') as csv_file:
    # turns the CSV into an object where we can iterate
    # over each row
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # TODO: set the counter
    count = 0
    # iterate over rows 
    for row in csv_reader:
        #TODO: if passenger is female and if she survived, increase the counter
        # NOTE: row[1] contains survival values, row[4] contains gender values
        # look over the CSV to see what to check against
        if row[4] == "female" and row[1] == "1":
            count += 1

#TODO: print the counter
    print(count)