import json

import webapp2
import logging as log
from com.abc.dms.rest.emp.user_info import EmployeeDB


''' Webapp2 way of exposing rest web services 
'''    
class UserInformationWebApp2(webapp2.RequestHandler):    
    
    def get(self):
        
        #Receive inputs
        _id = self.request.get("id")
        
        #Process input
        log.info('2...Received employee id : {0}....type : {1}'.format(_id, 'WebApp2'))
        db_emp = EmployeeDB().get(_id)
        emp = {'id':_id,
                'first_name':db_emp.get('first_name'), 
                'last_name':db_emp.get('last_name'),
                'Company':db_emp.get('company'),
                'role':db_emp.get('role'),
                'type':'WebApp2'}
        
        #Prepare response
        self.response.content_type = 'application/json'        
        self.response.write(json.dumps(emp))


    routes  = []
    routes.append(webapp2.Route(r'/dms/user', 
                      methods=['GET'],
                      handler='com.abc.dms.rest.user.UserInformationWebApp2:get', 
                      name='get'))