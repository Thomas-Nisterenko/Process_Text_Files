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


def file_to_dict(filename):
    """
    This function takes a filename, opens its associated file,
    and produces a dictionary with the file's information.
    :param filename: string with the file's name
    :return file_dict: dictionary formatted with file information
    """

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