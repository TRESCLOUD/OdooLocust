from OdooLocust import OdooLocust
from OdooLocust import OdooTaskSet


class Seller(OdooLocust.OdooLocust):
    host = "127.0.0.1"
    database = "testdb"
    #Deprecado en las ultimas version de locust
    #min_wait = 100
    #max_wait = 1000
    #
    #ahora se utiliza el siguente parametro
    wait_time = 0.5
    weight = 3
    
    task_set = OdooTaskSet.OdooGenericTaskSet
