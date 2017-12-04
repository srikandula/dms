'''
Created on Nov 29, 2017

@author: srinivas.kandula
'''
import endpoints
import webapp2

from com.abc.dms.rest.emp.user_0 import UserInformationWebApp2
from com.abc.dms.rest.emp.user_1 import UserInformationApi_1
from com.abc.dms.rest.emp.user_2 import UserInformationApi_2
from com.abc.dms.rest.file.file_rest import FileRestWS

api_services = []
api_services.append(UserInformationApi_1)
api_services.append(UserInformationApi_2)

api_services.append(FileRestWS)
endpoint_app = endpoints.api_server(api_services)

routes = []
routes.extend(UserInformationWebApp2.routes)
webapp2_app = webapp2.WSGIApplication(routes, debug=True)