import tkinter as tk

class OreCalc(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        #Creating labels
        LbMass = tk.Label("Mass")
        LbQu = tk.Label("Quantainium")
        LbBex = tk.Label("Bexalite")
        LbTa = tk.Label("Taranite")
        LbBo = tk.Label("Borase")
        LbLa = tk.Label("Laranite")
        LbAg = tk.Label("Agricium")
        LbHe = tk.Label("Hephaestanite")
        LbTi = tk.Label("Titanium")
        LbDi = tk.Label("Diamond")
        LbGo = tk.Label("Gold")
        LbCop = tk.Label("Copper")
        LbBer = tk.Label("Beryl")
        LbTu = tk.Label("Tungsten")
        LbCor = tk.Label("Corundum")
        LbQz = tk.Label("Quartz")
        LbAl = tk.Label("Aluminium")
        LbIm = tk.Label("Inert Material")
        
        #Collecting data
        EntMass = tk.Entry(self)
        EntQu = tk.Entry(self)
        EntBex = tk.Entry(self)
        EntTa = tk.Entry(self)
        EntBo = tk.Entry(self)
        EntLa = tk.Entry(self)
        EntAg = tk.Entry(self)
        EntHe = tk.Entry(self)
        EntTi = tk.Entry(self)
        EntDi = tk.Entry(self)
        EntGo = tk.Entry(self)
        EntCop = tk.Entry(self)
        EntBer = tk.LabelEntry(self)
        EntTu = tk.Entry(self)
        EntCor = tk.Entry(self)
        EntQz = tk.Entry(self)
        EntAl = tk.Entry(self)
        EntIm = tk.Entry(self)

        #Button!
        CalcButt = tk.Button(self, text = "Calculate", command = self.CalcCom)

        #Output field
        self.Output = tk.Text(self)




