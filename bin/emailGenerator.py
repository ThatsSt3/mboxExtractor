from mailbox import mboxMessage
from email import generator


class Generator:
    
    def __init__(self, rawMessage: mboxMessage, path: str, filename:str):
        self.rawMessage = rawMessage
        self.path = path
        self.filename = filename
        self.saveFile()
    
    def saveFile(self):
        
        msg = self.rawMessage
        
        
        with open(self.path + f'\\{self.filename}', 'w') as f:
            gen = generator.Generator(f)
            gen.flatten(msg)