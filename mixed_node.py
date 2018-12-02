import sys, random
from locust import HttpLocust, TaskSet

def readPost(locust):
    postid = random.randint(1, 500)
    url_prefix = '/blog/cs144/'
    locust.client.get(url_prefix + str(postid), name=url_prefix)

def writePost(locust):
    postid = random.randint(1, 500)
    url_prefix = '/blog/cs144/'
    title = 'Loading Test'
    body = '***Hello World!***'
    locust.client.post(url_prefix,
            data={'title': title, 'body': body, postid: str(postid)},
            name=url_prefix)

class MyTaskSet(TaskSet):
    tasks = [readPost]
    def on_start(locust):
        response = locust.client.post("/login", data={"username": "cs144", "password": "password"})
        if response.status_code != 200:
            print("Make sure server is running")
            sys.exit()

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
