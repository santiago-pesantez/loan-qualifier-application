# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csv_path, data):
    """ Writes a CSV file containing the arg data in the csv_path especified

    Args:
        csv_path (Path): File path to create the file.
        data (list): Data that will be written into the csv file.
    """        
    with open(csv_path, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file)
        for row in data:
            csvwriter.writerow(row)