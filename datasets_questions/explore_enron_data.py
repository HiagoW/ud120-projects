#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
from math import isnan

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#Number of peoples
print(len(enron_data))

#Number of features
print(len(enron_data[(list(enron_data.keys())[0])]))

#Number of pois
print(sum(p['poi']=='' for p in enron_data.values()))

print(enron_data["PRENTICE JAMES"]['total_stock_value'])
print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])
print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])

print(enron_data["FASTOW ANDREW S"]['total_payments'])
print(enron_data["LAY KENNETH L"]['total_payments'])
print(enron_data["SKILLING JEFFREY K"]['total_payments'])

#Number of known salaries and email addresses
print(sum(p['salary']!='NaN' for p in enron_data.values()))
print(sum(p['email_address']!='NaN' for p in enron_data.values()))