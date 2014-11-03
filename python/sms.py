from array import *

class sms():

    def __init__(self, modelname):        
        if modelname.find("T1bbbb") != -1: self.T1bbbb()
        if modelname.find("T5gg") != -1: self.T5gg()


    def T5gg(self):
        # model name
        self.modelname = "T5gg"
        # decay chain
        self.label= "pp#rightarrow#tilde{g}#tilde{g}, #tilde{g}#rightarrow q#bar{q} #tilde{#chi}^{0}_{1}";
        self.label= "T5gg";
        # scan range to plot
        self.Xmin = 800
        self.Xmax = 1500
        self.Ymin = 0
        self.Ymax = 2000
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{#chi}^{0}_{1}} (GeV)"        
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 0
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        
    def T1bbbb(self):
        # model name
        self.modelname = "T1bbbb"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow b #bar{b} #tilde{#chi}^{0}_{1}";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 400
        self.Xmax = 1600
        self.Ymin = 0
        self.Ymax = 1200
        # produce sparticle
        self.sParticle = "m_{gluino} (GeV)"
        # LSP
        self.LSP = "m_{LSP} (GeV)"
        # diagonal position: mLSP = mgluino - 2mtop
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[0, 20000])
