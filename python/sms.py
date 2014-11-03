from array import *

class sms():

    def __init__(self, modelname):        
        if modelname.find("T1bbbb") != -1: self.T1bbbb()
        if modelname.find("T5gg") != -1: self.T5gg()
        if modelname.find("GGM") != -1: self.GGM()

    def GGM(self):
        # model name
        self.modelname = "GGM"
        # decay chain
        self.label= " Razor - GGM Bino-like #chi^{0}_{1}"
        self.exclusion= "        NLO Exclusion"
        self.topology=" "
        self.selection="#geq 2#gamma #geq 1j"
        #self.label= "pp#rightarrow#tilde{g}#tilde{g}/#tilde{q}#tilde{q}#rightarrow 2#tilde{#chi}^{0}_{1}+jet(s)";
        # scan range to plot
        self.Xmin = 1200
        self.Xmax = 2000
        self.Ymin = 1200
        self.Ymax = 2250
        # produce sparticle
        self.sParticle = "m_{#tilde{q}} (GeV)"
        # LSP
        self.LSP = "m_{#tilde{g}} (GeV)"        
        # diagonal position: mLSP = mgluino - 2mtop 
        self.diagX = array('d',[0, 0])
        self.diagY = array('d',[0, 0])        

    def T5gg(self):
        # model name
        self.modelname = "T5gg"
        # decay chain
        self.topology = "pp #rightarrow #tilde{g}#tilde{g}, #tilde{g} #rightarrow (#tilde{#chi}^{0}_{1} #rightarrow #tilde{G}#gamma) + 2j"
        self.selection="#geq 2#gamma #geq 1j"
        self.label= " Razor - T5gg SMS"
        self.exclusion= "NLO+NLL Exclusion"
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
