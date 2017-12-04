'''
Created on Dec 3, 2017

@author: srinivas.kandula
'''

import endpoints
from protorpc import remote

from com.abc.dms.vo.file_vo import SearchFile, File
from com.abc.dms.service.file_service import FileService
import logging as log


@endpoints.api(name='dms', version='v1')
class FileRestWS(remote.Service):
    
    @endpoints.method(
        SearchFile,
        File,
        name='file',
        path='info',
        http_method='GET'
        )
    def get(self, search_file):
        
        #Receive inputs
        _id = search_file.file_id
        
        #Process input
        log.info('v1...Received employee id : {0}............type : {1}'.format(_id, 'API'))
        file = FileService().get(_id)
        
        #Prepare response
        return file
    
