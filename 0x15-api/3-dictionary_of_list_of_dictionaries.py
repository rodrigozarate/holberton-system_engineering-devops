#!/usr/bin/python3
"""
Some kind of words regarding https://jsonplaceholder.typicode.com
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ac convallis ex,
sed euismod nisl. Sed laoreet volutpat imperdiet. Proin at lacinia diam.
Nunc suscipit vulputate tristique. Nam ac mauris dolor. Donec tincidunt vehicula
pellentesque. Praesent lobortis urna vitae sem condimentum iaculis.
Nullam posuere eros nec justo accumsan dictum. Cras ex quam, congue a aliquet et,
porta a mi. Nunc varius feugiat dui, sit amet sodales lorem laoreet quis.
Donec ornare nunc cursus posuere lacinia. Etiam eu mauris mi. Vivamus sit amet
volutpat libero, vel pretium nulla. Maecenas tempus magna vitae finibus congue.
Sed vehicula fringilla scelerisque. Nam blandit ultricies vestibulum.
"""

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
