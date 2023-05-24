#!/usr/bin/python3
"""gather data from an API"""


from sys import argv
import requests


if __name__ == '__main__':
    if len(argv) > 1:
        employee = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        response = requests.get("{}users/{}".format(url, employee))
        data = response.json()
        employee_name = data.get("name")
        if employee_name is not None:
            response = requests.get(
                 "{}todos?userId={}".format(url, employee))
            todos = response.json()
            completed_todos = []
            for todo in todos:
                if todo.get("completed") is True:
                    completed_todos.append(todo)
            completed = len(completed_todos)
            total = len(todos)
            print("Employee {} is done with tasks({}/{}):".format(
                employee_name, completed, total
            ))
            for todo in completed_todos:
                title = todo.get('title')
                print("\t {}".format(title))
