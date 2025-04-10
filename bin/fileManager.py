import mailbox

class Extractor:
    
    def __init__(self, path: str):
        try:
            self.mbox = mailbox.mbox(path)
        except Exception:
            print("Errore nell'apertura del file mbox")
            
        