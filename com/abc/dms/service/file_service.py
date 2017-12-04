'''
Created on Nov 28, 2017

@author: srinivas.kandula
'''
from com.abc.dms.vo.file_vo import File

class FileService(object):
        
    def get(self, file_id):
        File_1 = File(name               = "2016-2017-Audit Report.xls",
                        file_id          = "101",
                        is_sepcial       = "False",
                        folder_id        = "23",
                        repo_id          = "1111111",
                        description      = "2016 2017 Audit Report",
                        icon             = "http://www.test.pjng",
                        mimeType         = "XLS",
                        sequence         = 1,
                        size             = 2000,
                        status           = "Active",
                        type             = "XLS",
                        createdBy        = "Srini",
                        createdOn        = "2017 No 23")

        File_2 = File(name             = "Summary Report.xls",
                        file_id          = "102",
                        is_sepcial       = "False",
                        folder_id        = "01",
                        repo_id          = "1111111",
                        description      = "Summary Dashboard",
                        icon             = "http://www.summaryjng",
                        mimeType         = "XLS",
                        sequence         = 2,
                        size             = 2000,
                        status           = "Active",
                        type             = "XLS",
                        createdBy        = "Srini",
                        createdOn        = "2017 Jan 23")

        File_3 = File(name               = "ABC Audit Reports",
                        file_id          = "103",
                        is_sepcial       = "False",
                        folder_id        = "01",
                        repo_id          = "1111111",
                        description      = "ABV Audit Report",
                        icon             = "http://www.audit.pdf",
                        mimeType         = "pdf",
                        sequence         = 3,
                        size             = 2000,
                        status           = "Active",
                        type             = "PDF",
                        createdBy        = "Srini",
                        createdOn        = "2017 Dec 02")
        store = {            
                    "101" : File_1,
                    "102" : File_2,
                    "103" : File_3
                }
        return store.get(file_id)
        
