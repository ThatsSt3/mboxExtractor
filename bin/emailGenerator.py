from mailbox import mboxMessage
from email import generator
from datetime import datetime
import os

class Generator:
    
    
    
    def __init__(self, rawMessage: mboxMessage, path: str):
        self.rawMessage = rawMessage
        self.path = path
        self.monthTranslator = {
        'Jan': 'Gennaio',
        'Feb': 'Febbraio',
        'Mar': 'Marzo',
        'Apr': 'Aprile',
        'May': 'Maggio',
        'Jun': 'Giugno',
        'Jul': 'Luglio',
        'Aug': 'Agosto',
        'Sep': 'Settembre',
        'Oct': 'Ottobre',
        'Nov': 'Novembre',
        'Dec': 'Dicembre'
    }
    
    def saveFile(self) -> str:
        
        msg = self.rawMessage
        
        date = msg['date']
        if date[:3] in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
            date = date[5:]
        date = datetime.strptime(date[:19], "%d %b %Y %H:%M:%S")
        dateName = date.strftime("%d-%m-%Y")
        sender = msg['from']
        receiver = msg['to']
        if receiver and len(receiver.split(',')) > 1:
            receiver = receiver.split(',')[0]
        
        sender = self._cleanup(sender) if sender else ''
        receiver = self._cleanup(receiver) if receiver else ''
            
        filename = f"{dateName} {sender} {receiver}"
        thisMonth = self.monthTranslator[date.strftime("%b")]
        thisYear = date.strftime("%Y")
        folderName = f"{thisMonth} {thisYear}"
        newPath = f"{self.path}\\{folderName}"
        
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        
        target = newPath + '\\' + filename + '.eml'
        
          
        with open(target, 'w') as f:
            gen = generator.Generator(f)
            gen.flatten(msg)
        
        return filename + '.eml'
    
    
    def _cleanup(self, s: str) -> str:
        res = ''
        try:
            findAdd = s.split('@')
            add1 = findAdd[0].split(' ')[-1]
            add2 = findAdd[1].split(' ')[0]
            
            add = add1 + '@' + add2
        except:    
            add = s
        
        finally:
            for ch in add:
                if ch.isalnum() or ch in '-_.':
                    res += ch
        
            return res