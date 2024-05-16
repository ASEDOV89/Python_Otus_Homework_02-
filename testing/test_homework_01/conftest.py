# from utils import add_homework_path
#
# add_homework_path(__file__)
def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 5:
        session.exitstatus = 10 # Any arbitrary custom status you want to return```