# Writing CSV files in python

import csv

with open('Files_Directories/model_performance.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Model Version', 'Accuracy', 'Response Time (ms)', 'Tokens'])

    models = [
        ('GPT-4', 98.7, 45, 300),
        ('GPT-4o', 99.7, 42, 350)
    ]

    for model in models:
        writer.writerow(model)