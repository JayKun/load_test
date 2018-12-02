import sys, random
from locust import HttpLocust, TaskSet


def readPost(locust):
    postid = random.randint(1, 500)
    url_prefix = '/editor/post?action=open&username=cs144&postid='
    locust.client.get(url_prefix + str(postid), name=url_prefix)

def writePost(locust):
    postid = random.randint(1, 500)
    url_prefix = '/editor/post?action=save'
    title = 'Loading%20Test'
    body = '***Hello%20World!***'
    data = {
            'username': 'cs144',
            'postid': str(postid),
            'title': title,
            'body': body
    }

    locust.client.post(url_prefix, data=data, name=url_prefix)

class MyTaskSet(TaskSet):
    tasks = {readPost: 9, writePost: 1}

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
