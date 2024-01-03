#!/usr/bin/python3
"""
Export data in the CSV format
"""

from json import dumps
import requests
from sys import argv

if __name__ == "__main__":
    # Check if the ID is an integer
    try:
        empId = int(argv[1])
    except ValueError:
        exit()

    # Dummy variables from REST API
    api_url = "https://jsonplaceholder.typicode.com"
    user_uri = "{}/users/{}".format(api_url, empId)
    todo_uri = "{}/todos".format(user_uri)
    filename = "{}.json".format(empId)

    # User Response
    user_response = requests.get(user_uri).json()

    # User TODO response
    todo_response = requests.get(todo_uri).json()

    # A list of all tasks of an user
    user_tasks = list()

    for elem in todo_response:
        data = {
                'task': elem.get('title'),
                'completed': elem.get('completed'),
                'username': user_response.get('username')
                }
        user_tasks.append(data)

    # Create the new filw for the save the information
    # Filename example: {user_id}.json
    with open(filename, 'w', encoding='utf-8') as jsonFile:
        jsonFile.write(dumps({empId: user_tasks}))
