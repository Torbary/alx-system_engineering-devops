#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import sys
import requests
import csv

def export_employee_tasks_to_csv(employee_id):
    """
    Export all tasks owned by the employee in CSV format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Fetch employee data
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_response = requests.get(employee_url)

    if employee_response.status_code == 200:
        employee_data = employee_response.json()
        employee_name = employee_data['name']

        # Fetch TODO list data for the employee
        todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
        todo_response = requests.get(todo_url)

        if todo_response.status_code == 200:
            todo_data = todo_response.json()
            file_name = "{}.csv".format(employee_id)

            # Write data to CSV file
            with open(file_name, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)

                for task in todo_data:
                    task_completed = str(task['completed'])
                    task_title = task['title']
                    writer.writerow([str(employee_id), employee_name, task_completed, task_title])

            print("Data exported to {}".format(file_name))
        else:
            print("Error: Could not fetch TODO data for employee ID {}".format(employee_id))
    else:
        print("Error: Could not fetch employee data for ID {}".format(employee_id))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        export_employee_tasks_to_csv(employee_id)
