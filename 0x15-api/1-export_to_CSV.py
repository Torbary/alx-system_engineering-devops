#!/usr/bin/python3
"""export data as"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        employee = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        response = requests.get("{}users/{}".format(url, employee))
        data = response.json()
        username = data.get("username")
        response = requests.get(
             "{}todos?userId={}".format(url, employee))
        todos = response.json()

        with open("{}.csv".format(employee), 'w') as csvfile:
            content = []
            for todo in todos:
                completed = todo.get("completed")
                title = todo.get("title")
                line = '"{}","{}","{}","{}"'.format(
                    employee, username, completed, title
                )
                content.append(line)

            csvfile.write("\n".join(content))
