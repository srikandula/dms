import endpoints
from protorpc import messages
from protorpc import remote

from com.abc.dms.rest.emp.user_info import EmployeeDB
import logging as log


class EmployeeRequest(messages.Message):
    id          = messages.IntegerField(1)

    
class EmployeeResponse(messages.Message):
    id          = messages.IntegerField(1)
    user        = messages.StringField(2)
    last_name   = messages.StringField(3)
    first_name  = messages.StringField(4)
    company     = messages.StringField(5)
    role        = messages.StringField(6)
    type        = messages.StringField(7)

@endpoints.api(name='employee', version='v2')
class UserInformationApi_2(remote.Service):
     
    @endpoints.method(
        EmployeeRequest,
        EmployeeResponse,
        name='employee',
        path='search',
        http_method='GET'
        )
    def get(self, request):
         
        #Receive inputs
        _id = request.id
         
        #Process input
        log.info('v2...Received employee id : {0}....type : {1}'.format(_id, 'API'))
        db_emp = EmployeeDB().get(_id)
        emp = EmployeeResponse(id=_id,
                               first_name=db_emp.get('first_name'),
                               last_name=db_emp.get('last_name'), 
                               company=db_emp.get('company'), 
                               role=db_emp.get('role'),
                               type='API')
         
        #Prepare response
        return emp