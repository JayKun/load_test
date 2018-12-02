import sys, random
from locust import HttpLocust, TaskSet

def readPost(locust):
    postid = random.randint(1, 500)
    url_prefix = '/blog/cs144/'
    locust.client.get(url_prefix + str(postid), name=url_prefix)

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
    tasks = { readPost:9, writePost:1 }
    def on_start(locust):
        response = locust.client.post("/login", data={"username": "cs144", "password": "password", "redirect":"/"})
        if response.status_code != 200:
            print("Make sure server is running")
            sys.exit()

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
