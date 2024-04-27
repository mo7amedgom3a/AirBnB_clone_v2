
from fabric.api import task
@task
def hello(who="world"):

    print 
    "Hello who!".format(who=who)
hello()