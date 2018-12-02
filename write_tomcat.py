import sys, random
from locust import HttpLocust, TaskSet

'''
In this file, we are simulating the scenario where all requests from users
are read intensive. The user whose name is cs144 would randomly open one of
his posts via /editor/post?action=open&username=cs144&postid={num}, where
{num} is a random postid.

Note: In this file, use /editor/post?action=open as the name of the requests.
Also, make sure that postid that user opens should be between 1 and 500.
Since our user 'cs144' only has 500 posts, he will get nothing otherwise.
'''
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
    tasks = [writePost]

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
