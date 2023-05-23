#!/usr/bin/python3
"""Export to JSON"""


import sys
import json
import requests


def export_employee_todo_json(employee_id):
    """
    Export employee's TODO list data in JSON format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_response = requests.get(employee_url)

    if employee_response.status_code == 200:
        employee_data = employee_response.json()
        employee_name = employee_data['username']

        todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
        todo_response = requests.get(todo_url)
        if todo_response.status_code == 200:
            todo_data = todo_response.json()

            json_data = {str(employee_id): []}
            for task in todo_data:
                json_data[str(employee_id)].append({
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": employee_name
                })

            filename = "{}.json".format(employee_id)
            with open(filename, 'w') as json_file:
                json.dump(json_data, json_file)

            print("JSON file '{}' has been created.".format(filename))
        else:
            print("Error: Could not fetch TODO data for employee ID {}".format(employee_id))
    else:
        print("Error: Could not fetch employee data for ID {}".format(employee_id))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        export_employee_todo_json(employee_id)
