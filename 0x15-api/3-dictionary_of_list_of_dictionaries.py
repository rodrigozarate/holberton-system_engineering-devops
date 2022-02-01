"""Some kind of words regarding https://jsonplaceholder.typicode.com"""
#!/usr/bin/python3
import json
import request


if __name__ == '__main__':
    filename = "todo_all_employees.json"
    req = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    req_id = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    with open(filename, "w") as dictfile:
        dataset = {j.get("id"): [{'username': j.get('username'),
                   'task': i.get('title'), 'completed': i.get('completed')}
             for i in req
             if j.get("id") == i.get('userId')] for j in req_id}
        json.dump(dataset, dictfile)
