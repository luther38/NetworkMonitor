
from networkmonitor.src.configuration import *
from networkmonitor.src.collections import Nodes

def test_JsonRead():
    # Add info into interface
    i = IConfig("example.json")

    # Generate our context that will handle the work
    c = ContextConfig(i)
    c.ReadConfig()

    if c.Nodes.__len__() >= 1:
        assert True
    pass

def test_JsonContainsSleepInterval():
    i = IConfig("example.json")
    c = ContextConfig(i)
    c.ReadConfig()

    if c.SleepInterval >= 0:
        assert True

def test_JsonNodesContainNames():
    # Each node needs to contain a Name:
    i = IConfig("example.json")
    c = ContextConfig(i)
    c.ReadConfig()

    for item in c.Nodes:
        if item.name == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True

def test_JsonNodesContainAddress():
    # Each node needs to contain a Name:
    i = IConfig("example.json")
    c = ContextConfig(i)
    c.ReadConfig()

    for item in c.Nodes:
        if item.address == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True

def test_JsonNodesContainProtocol():
    # Each node needs to contain a Name:
    i = IConfig("example.json")
    c = ContextConfig(i)
    c.ReadConfig()

    for item in c.Nodes:
        if item.protocol == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True