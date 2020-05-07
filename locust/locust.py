from locust import HttpLocust, TaskSet, between

def index(l):
    l.client.get("")

def fail(l):
    l.client.get("fail")


def referenzen(l):
    l.client.get("referenzen")


class UserBehavior(TaskSet):
    tasks = {index: 3, fail: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
