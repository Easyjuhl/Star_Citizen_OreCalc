import tkinter as tk

class OreCalc(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        #Creating labels
        LbMass = tk.Label(self, text = "Mass")
        LbQu = tk.Label(self, text = "Quantainium")
        LbBex = tk.Label(self, text = "Bexalite")
        LbTa = tk.Label(self, text = "Taranite")
        LbBo = tk.Label(self, text = "Borase")
        LbLa = tk.Label(self, text = "Laranite")
        LbAg = tk.Label(self, text = "Agricium")
        LbHe = tk.Label(self, text = "Hephaestanite")
        LbTi = tk.Label(self, text = "Titanium")
        LbDi = tk.Label(self, text = "Diamond")
        LbGo = tk.Label(self, text = "Gold")
        LbCop = tk.Label(self, text = "Copper")
        LbBer = tk.Label(self, text = "Beryl")
        LbTu = tk.Label(self, text = "Tungsten")
        LbCor = tk.Label(self, text = "Corundum")
        LbQz = tk.Label(self, text = "Quartz")
        LbAl = tk.Label(self, text = "Aluminium")
        
        PriQu = 44.045
        PriBex = 20.24
        PriTa = 16.22
        PriBo = 16.225
        PriLa = 15.12
        PriAg = 13.44
        PriHe = 7.33
        PriTi = 4.33
        PriDi = 3.59
        PriGo = 3.16
        PriCop = 2.85
        PriBe = 2.15
        PriTu = 2.005
        PriCor = 1.33
        PriQz = 0.75
        PriAl = 0.64

        #Collecting data
        self.EntMass = tk.Entry(self)
        self.EntQu = tk.Entry(self)
        self.EntBex = tk.Entry(self)
        self.EntTa = tk.Entry(self)
        self.EntBo = tk.Entry(self)
        self.EntLa = tk.Entry(self)
        self.EntAg = tk.Entry(self)
        self.EntHe = tk.Entry(self)
        self.EntTi = tk.Entry(self)
        self.EntDi = tk.Entry(self)
        self.EntGo = tk.Entry(self)
        self.EntCop = tk.Entry(self)
        self.EntBer = tk.Entry(self)
        self.EntTu = tk.Entry(self)
        self.EntCor = tk.Entry(self)
        self.EntQz = tk.Entry(self)
        self.EntAl = tk.Entry(self)

        fEntMass = float(self.EntMass.get())
        try:
            fEntQu = float(self.EntQu.get())
        except ValueError:
            fEntQu = 0.0
        try:
            fEntBex = float(self.EntBex.get())
        except ValueError:
            fEntBex = 0.0
        try:
            fEntTa = float(self.EntTa.get())
        except ValueError:
            fEntTa = 0.0
        try:
            fEntBo = float(self.EntBo.get())
        except ValueError:
            fEntBo = 0.0
        try:
            fEntLa = float(self.EntLa.get())
        except ValueError:
            fEntLa = 0.0
        try:
            fEntAg = float(self.EntAg.get())
        except ValueError:
            fEntAg = 0.0
        try:
            fEntHe = float(self.EntHe.get())
        except ValueError:
            fEntHe = 0.0
        try:
            fEntTi = float(self.EntTi.get())
        except ValueError:
            fEntTi = 0.0
        try:
            fEntDi = float(self.EntDi.get())
        except ValueError:
            fEntDi = 0.0
        try:
            fEntGo = float(self.EntGo.get())
        except ValueError:
            fEntGo = 0.0
        try:
            fEntCop = float(self.EntCop.get())
        except ValueError:
            fEntCop = 0.0
        try:
            fEntBer = float(self.EntBer.get())
        except ValueError:
            fEntBer = 0.0
        try:
            fEntTu = float(self.EntTu.get())
        except ValueError:
            fEntTu = 0.0
        try:
            fEntCor = float(self.EntCor.get())
        except ValueError:
            fEntCor = 0.0
        try:
            fEntQz = float(self.EntQz.get())
        except ValueError:
            fEntQz = 0.0
        try:
            fEntAl = float(self.EntAl.get())
        except ValueError:
            fEntAl = 0.0

        #Button!
        CalcButt = tk.Button(self, text = "Calculate", command = self.CalcCom)

        #Output field
        self.Output = tk.Text(self)
        
        #Grid
        LbMass.grid(row = 0, column = 0)
        LbQu.grid(row = 1, column = 0)
        LbBex.grid(row = 2, column = 0)
        LbTa.grid(row = 3, column = 0)
        LbBo.grid(row = 4, column = 0)
        LbLa.grid(row = 5, column = 0)
        LbAg.grid(row = 6, column = 0)
        LbHe.grid(row = 7, column = 0)
        LbTi.grid(row = 8, column = 0)
        LbDi.grid(row = 9, column = 0)
        LbGo.grid(row = 10, column = 0)
        LbCop.grid(row = 11, column = 0)
        LbBer.grid(row = 12, column = 0)
        LbTu.grid(row = 13, column = 0)
        LbCor.grid(row = 14, column = 0)
        LbQz.grid(row = 15, column = 0)
        LbAl.grid(row = 16, column = 0)

        self.EntMass.grid(row = 0, column = 1)
        self.EntQu.grid(row = 1, column = 1)
        self.EntBex.grid(row = 2, column = 1)
        self.EntTa.grid(row = 3, column = 1)
        self.EntBo.grid(row = 4, column = 1)
        self.EntLa.grid(row = 5, column = 1)
        self.EntAg.grid(row = 6, column = 1)
        self.EntHe.grid(row = 7, column = 1)
        self.EntTi.grid(row = 8, column = 1)
        self.EntDi.grid(row = 9, column = 1)
        self.EntGo.grid(row = 10, column = 1)
        self.EntCop.grid(row = 11, column = 1)
        self.EntBer.grid(row = 12, column = 1)
        self.EntTu.grid(row = 13, column = 1)
        self.EntCor.grid(row = 14, column = 1)
        self.EntQz.grid(row = 15, column = 1)
        self.EntAl.grid(row = 16, column = 1)

        CalcButt.grid(row = 17, column = 0, columnspan = 2)
        self.Output.grid(row = 18, column = 0, columnspan = 2)

        self.pack()
    
    def Calccom(self):
        MassQu = fEntMass*fEntQu
        MassBex = fEntMass*fEntBex
        MassTa = fEntMass*fEntTa
        MassBo = fEntMass*fEntBo
        MassLa = fEntMass*fEntLa
        MassAg = fEntMass*fEntAg
        MassHe = fEntMass*fEntHe
        MassTi = fEntMass*fEntTi
        MassDi = fEntMass*fEntDi
        MassGo = fEntMass*fEntGo
        MassCop = fEntMass*fEntCop
        MassBer = fEntMass*fEntBer
        MassTu = fEntMass*fEntTu
        MassCor = fEntMass*fEntCor
        MassQz = fEntMass*fEntQz
        MassAl = fEntMass*fEntAl

        

prg = OreCalc()
prg.master.title('Ore Calculator')
prg.mainloop()