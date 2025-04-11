import mailbox
import os
import shutil
from collections.abc import Iterator
from bin.emailGenerator import Generator
from bin.progress import Progress

class Extractor:
    
    
    def __init__(self, path: str, folderName: str = 'Output'):
        try:
            self.mbox = mailbox.mbox(path)
        except Exception:
            print("Errore nell'apertura del file mbox")
            raise  Exception("MBOX File not found")
        
        path_back = '\\'.join(path.split('\\')[:-1])
        
        self.path = self._createOutputFolder(path_back, folderName)
    
    def analyzeEmails(self) -> Iterator[Progress]:
        for i, email in enumerate(self.mbox):
            yield Progress(i + 1, self.mbox.keys()[-1] + 1, Generator(email, self.path).saveFile())

            
    
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
    
    
    
            
    
            
        