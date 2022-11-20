import pandas as pd

# Import DictWriter class from CSV module
from csv import DictWriter
#takes in input the a list that contains the name of the "property", the threshold and finally the recommandations.
def addline(lstadd):
    d = {"name":lstadd[0],"threshold":lstadd[1],"recommandations":lstadd[2]}
    with open('/Users/alchambron/Documents/Coding_Project/hackatton/sanassist/sanassist/home/ThreshDB.csv', 'a') as f_object:
        field_names = ["name","threshold","recommandations"]
            # Pass the file object and a list
        # of column names to DictWriter()
        # You will get a object of DictWriter
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        dictwriter_object.writerow(d)
         # Close the file object
        f_object.close()

b =["Nitrate", 50, "Eau non potable, cancérigène, risque de problèmes sur l'oxygénation du sang"]
a = ["Nitrite", 3, "Eau non potable, cancérigène, risque de problèmes sur l'oxygénation du sang"]
addline(a)
addline(b)
        


