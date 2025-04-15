import os
from appJar import gui
from bin.fileManager import Extractor




class Application(gui):
    

    def __init__(self, title: str = '', size: str = "1200x800"):
        
        super().__init__(title, size)
        
        self.mainColour = 'lightblue'
        self.secondColour = 'black'
        self.extractingFile = ''
    
        self.setFont(16)        
        self.showSplash("MBOX File Extractor", fill=self.mainColour, stripe=self.secondColour, fg="white", font=44)
        
        self.setBg(self.mainColour)
        
        
        

        
        self._inputFileFrame()
        
        
        self.go()
        
        
    
    
    def _inputFileFrame(self):
        self.startLabelFrame("Seleziona file di input", colspan=1)
        self.addLabel("l1", "Percorso file:", row=0)
        self.addFileEntry("inputPath", row=0, column=1)
        self.addButton("Estrai", self._extractEmail, row=0, column=2)
    
    def _extractEmail(self, btn):
        if btn == 'Estrai':
            path = self.getEntry("inputPath")
            if os.path.exists(path) and path.endswith('.mbox'):
                
                
                path = os.path.abspath(path)
                e = Extractor(path)
                
                
                self._analyzer(e)             
                
                self.popUp("procComplete", "Estrazione email completata")
                self.clearEntry("inputPath")
            
            else:
                self.errorBox("File non valido", "Il percorso selezionato non porta a un file MBOX valido")
    
    
    def _analyzer(self, e: Extractor):
        for email in e.analyzeEmails():
            pass
    

        
        
    