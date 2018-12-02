import sys, random, json
from locust import HttpLocust, TaskSet

def writePost(locust):
    postid = random.randint(1, 500)
    url_prefix = '/api/cs144/'
    title = 'Loading Test'
    body = '***Hello World!***'
    res = locust.client.put(
            url_prefix + str(postid),
            data={'title': title, 'body': body},
            name=url_prefix)

class MyTaskSet(TaskSet):
    tasks = [writePost]
    def on_start(locust):
        data = {'username': 'cs144', 'password': 'password', 'redirect':'/'}
        response = locust.client.post('/login', data=data)
        print(response.status_code)

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
