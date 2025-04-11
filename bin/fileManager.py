import mailbox
import os
import shutil
from alive_progress import alive_bar
from bin.emailGenerator import Generator

class Extractor:
    
    def __init__(self, path: str, folderName: str = 'Output'):
        try:
            self.mbox = mailbox.mbox(path)
        except Exception:
            print("Errore nell'apertura del file mbox")
            raise  Exception("MBOX File not found")
        
        path_back = '\\'.join(path.split('\\')[:-1])
        
        self.path = self._createOutputFolder(path_back, folderName)
    
    def analyzeEmails(self):
        with alive_bar(self.mbox.keys()[-1] + 1) as b:
            for i, email in enumerate(self.mbox):
                Generator(email, self.path)
                b()
            
    
    def _createOutputFolder(self, path: str, folderName: str) -> str:
        newPath = path + '\\' + folderName
        
        try:
            if os.path.exists(newPath):
                shutil.rmtree(newPath)
            os.makedirs(newPath)
        except:
            print('Error in creating folder')
            raise Exception('Folder create')
        
        return newPath
    
    
    
            
    
            
        