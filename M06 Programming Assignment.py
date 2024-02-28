# -*- coding: utf-8 -*-
"""
Armando Cedano
M04 Programming Assignment
This code is the answers to the 13.1-13.3 and 15.1 of Things To Do questions.
"""

import datetime
import random
import multiprocessing
import time

def write_date_to_file():
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Write current date to the file today.txt
    with open("today.txt", "w") as file:
        file.write(current_date)

def read_date_from_file():
    # Read the text file today.txt
    with open("today.txt", "r") as file:
        today_string = file.read()
    
    return today_string

def parse_date(today_string):
    # Parse the date from today_string
    parsed_date = datetime.datetime.strptime(today_string, "%Y-%m-%d")
    
    return parsed_date

def print_current_time():
    # Print the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Current time: {current_time}")

def process_function():
    # Wait for a random number of seconds between 0 and 1
    wait_time = random.random()
    time.sleep(wait_time)
    
    # Print the current time
    print_current_time()

if __name__ == "__main__":
    # Task 13.1: Write the current date to the file today.txt
    write_date_to_file()
    
    # Task 13.2: Read the text file today.txt into the string today_string
    today_string = read_date_from_file()
    
    # Task 13.3: Parse the date from today_string
    parsed_date = parse_date(today_string)
    print("Parsed date:", parsed_date)
    
    # Task 15.1: Use multiprocessing to create three separate processes
    processes = []
    for _ in range(3):
        process = multiprocessing.Process(target=process_function)
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
