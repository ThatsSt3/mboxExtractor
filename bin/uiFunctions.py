import os
from appJar import gui
from bin.fileManager import Extractor
from bin.progress import Progress



class Application(gui):
    

    def __init__(self, title: str = '', size: str = "1200x800"):
        
        super().__init__(title, size)
        
        self.mainColour = 'lightblue'
        self.secondColour = 'black'
        self.extractingFile = ''
    
        self.setFont(16)        
        self.showSplash("MBOX File Extractor", fill=self.mainColour, stripe=self.secondColour, fg="white", font=44)
        
        self.setBg(self.mainColour)
        
        
        self.initExtractingWindow()
        

        
        self.inputFileFrame()
        
        
        self.go()
        
        
    
    
    def inputFileFrame(self):
        self.startLabelFrame("Seleziona file di input", colspan=1)
        self.addLabel("l1", "Percorso file:", row=0)
        self.addFileEntry("inputPath", row=0, column=1)
        self.addButton("Estrai", self.extractEmail, row=0, column=2)
    
    def extractEmail(self, btn):
        if btn == 'Estrai':
            path = self.getEntry("inputPath")
            if os.path.exists(path) and path.endswith('.mbox'):
                
                
                path = os.path.abspath(path)
                e = Extractor(path)
                
                self.showSubWindow("extractionPage")
                
                self.thread(self.analyzer, e)
                self.hideSubWindow("extractionPage")                
                
                self.popUp("procComplete", "Estrazione email completata")
                self.clearEntry("inputPath")
            
            else:
                self.errorBox("File non valido", "Il percorso selezionato non porta a un file MBOX valido")
    
    
    def analyzer(self, e: Extractor):
        self.openSubWindow("extractionPage")
        
        
        for email in e.analyzeEmails():
            self.extractingFile = email.filename
            self.queueFunction(self.setLabel, "fileInProgress", f"Extracting: {self.extractingFile}")
        
        self.extractingFile = ''
    
    def initExtractingWindow(self):
        self.startSubWindow("extractionPage")
        self.setSize("800x600")
        self.label("fileInProgress", "Extracting: ")
        self.setBg(self.mainColour)
        self.stopSubWindow()
        
        
    