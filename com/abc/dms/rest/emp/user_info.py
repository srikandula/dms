'''
Created on Nov 28, 2017

@author: srinivas.kandula
'''

class EmployeeDB(object):
        
    def get(self, _id):
        store = {            
                    1 : {
                        "company": "PwC",
                        "first_name": "Ryan",
                        "id": 1,
                        "last_name": "Edley",
                        "role": "Director",
                        "type": "API"
                    },
                    2 : {
                        "company": "Infosys",
                        "first_name": "Srinivas",
                        "id": 2,
                        "last_name": "Kandula",
                        "role": "Senior Technology Architect",
                        "type": "API"
                    },
                    3 : {
                        "company": "Infosys",
                        "first_name": "Sangamesh",
                        "id": 3,
                        "last_name": "Ranjanagi",
                        "role": "Technical Project Manager",
                        "type": "API"
                    },
                    4 : {
                        "company": "Infosys",
                        "first_name": "Kishore",
                        "id": 3,
                        "last_name": "Naga",
                        "role": "Technology Expert",
                        "type": "API"
                    }
            
            }
        return store.get(_id)
        
