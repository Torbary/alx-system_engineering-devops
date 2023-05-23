#!/usr/bin/python3
"""FAST API"""

import json
import requests


def export_all_employees_todo_json():
    """
    Export TODO list data for all employees in JSON format.

    Returns:
        None
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)

    if users_response.status_code == 200:
        users_data = users_response.json()

        json_data = {}
        for user in users_data:
            employee_id = user['id']
            employee_username = user['username']

            todo_url = "https://jsonplaceholder.typicode.com/todos?" \
                "userId={}".format(employee_id)
            todo_response = requests.get(todo_url)
            if todo_response.status_code == 200:
                todo_data = todo_response.json()

                json_data[str(employee_id)] = []
                for task in todo_data:
                    json_data[str(employee_id)].append({
                        "username": employee_username,
                        "task": task['title'],
                        "completed": task['completed']
                    })

        filename = "todo_all_employees.json"
        with open(filename, 'w') as json_file:
            json.dump(json_data, json_file)

        print("JSON file '{}' has been created.".format(filename))
    else:
        print("Error: Could not fetch employee data.")


if __name__ == "__main__":
    export_all_employees_todo_json()
