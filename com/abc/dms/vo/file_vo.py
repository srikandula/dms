'''
Created on Dec 3, 2017

@author: srinivas.kandula
'''
from protorpc import messages
        
        
class SearchFile(messages.Message):
    file_id          = messages.StringField(1)

class File(messages.Message):
    name             = messages.StringField(1)
    file_id          = messages.StringField(2)
    is_sepcial       = messages.StringField(3)
    folder_id        = messages.StringField(4)
    repo_id          = messages.StringField(5)
    description      = messages.StringField(6)
    icon             = messages.StringField(7)
    mimeType         = messages.StringField(8)
    sequence         = messages.IntegerField(9)
    size             = messages.IntegerField(10)
    status           = messages.StringField(11)
    type             = messages.StringField(12)
    createdBy        = messages.StringField(13)
    createdOn        = messages.StringField(14)
