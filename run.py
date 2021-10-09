#!usr/bin/env python3

"""
Author: Thomas Cascais Nisterenko
Date: 2021-10-09
Purpose: This python script takes user reviews written in .txt files
         inside a directory, parses the contents of the files in
         dictionaries and posts them to a website.
"""

import os
import requests


def get_txtfiles(dir_path):
    """
    This function gets all files from a sepcified directory
    and produces a list with them.
    :param dir_path: string with path to directory
    :return txtfiles: list with  filenames of txt files
    """

    # txtfiles is initialized as an empty list
    txtfiles = []

    # traverses the specified directory and appends only the
    # .txt files to the list
    for file in os.listdir(dir_path):
        if file.endswith(".txt"):
            txtfiles.append(file)
    
    return txtfiles


def file_to_dict(filename):
    """
    This function takes a filename, opens its associated file,
    and produces a dictionary with the file's information.
    :param filename: string with the file's name
    :return file_dict: dictionary formatted with file information
    """

    # file_dict is intialized as an empty dictionary
    file_dict = {}

    # opens file in read mode
    with open(filename, "r") as review_file:
        # first three lines get the fields title, name, and date
        file_dict["title"] = review_file.readline().strip()
        file_dict["name"] = review_file.readline().strip()
        file_dict["date"] = review_file.readline().strip()

        # remaining lines are joined together and assigned to feedback key
        file_dict["feedback"] = "".join(review_file.readlines()).strip()
    
    return file_dict


def post_dict(review_dict, address):
    """
    This function takes a dictionary and posts its contents to the webpage.
    :param review_dict: dictionary with review information
    :param address: string with the webpage's address
    :return: None
    """


def main():
    """
    main function that takes care of the program's overall logic and calls
    other functions.
    """
    pass


if __name__ == "__main__":
    main()