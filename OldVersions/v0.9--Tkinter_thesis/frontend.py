import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
import backend as bk
from PIL import ImageTk, Image

class Application(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "SATRAP")
        tk.Tk.geometry(self, "1000x200")
        tk.Tk.minsize(self, width=200, height=200)
        tk.Tk.iconbitmap(self, default="interface.ico")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, HelpMenu, Centrality, Accessibility, GetPoly):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)
   
    def show_frame(self, cont=None):
      if cont is None:
        # show last frame
        cont = self.lastcont
      frame = self.frames[cont]
      frame.tkraise()
      if cont != HelpMenu:
        self.lastcont = cont

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        tk.Frame.update(self)
        tk.Frame.grid_columnconfigure(self, 0, weight=1)
        tk.Frame.grid_columnconfigure(self, 1, weight=1)
        tk.Frame.grid_columnconfigure(self, 2, weight=1)
        tk.Frame.grid_columnconfigure(self, 3, weight=1)
        tk.Frame.grid_columnconfigure(self, 4, weight=1)
        tk.Frame.grid_columnconfigure(self, 5, weight=1)
#        self.createCanvasImage()
        
        methodLabel = tk.Label(self, text="Choose Method", font=("Verdana", 11))
        methodLabel.grid(row=3, column=2)
        
        centButton = ttk.Button(self, text="Centrality Analysis",
                            command=lambda: controller.show_frame(Centrality))
        centButton.grid(row=4, column=2)
        
        accessButton = ttk.Button(self, text="Accessibility Analysis",
                            command=lambda: controller.show_frame(Accessibility))
        accessButton.grid(row=5, column=2)
        
        getStudyAreabutton = ttk.Button(self, text="Get Study Area",
                            command=lambda: controller.show_frame(GetPoly))
        getStudyAreabutton.grid(row=0, column=0)
        
#    def createCanvasImage(self):
#        canvas = tk.Canvas(self, width=1000, height=200)
#        canvas.grid(row=0, column=0, rowspan=10, columnspan=7)
#         = Image.open(r"C:\Users\OmrAkn\Desktop\YuksekLisansTezUygulama\SATRAP\s5uaze.png")
#        canvas.image = ImageTk.PhotoImage(img)
#        canvas.create_image(0, 0, image=canvas.image, anchor=tk.NW)

class GetPoly(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        tk.Frame.update(self)
        tk.Frame.grid_columnconfigure(self, 0, weight=1)
        tk.Frame.grid_columnconfigure(self, 1, weight=1)
        tk.Frame.grid_columnconfigure(self, 2, weight=1)
        tk.Frame.grid_columnconfigure(self, 3, weight=1)
        tk.Frame.grid_columnconfigure(self, 4, weight=1)
        tk.Frame.grid_columnconfigure(self, 5, weight=1)
        tk.Frame.grid_columnconfigure(self, 6, weight=1)
        tk.Frame.grid_columnconfigure(self, 7, weight=1)
#        self.createCanvasImage()
        
        backButton = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        backButton.grid(row=0, column=0, sticky=tk.W)
        
        helpButton = ttk.Button(self, text="Help",
                           command=lambda: controller.show_frame(HelpMenu))
        helpButton.grid(row=0, column=2, sticky=tk.E) 
        
        tk.Label(self, text="Region Name / Result Number").grid(row=1, sticky=tk.E)
        tk.Label(self, text="Shapefile Output Folder").grid(row=2, sticky=tk.E)
        tk.Label(self, text="Shapefile Output Name").grid(row=3, sticky=tk.E)
        self.placeName = tk.StringVar(self)
        self.e2 = tk.Entry(self, width=35, font="Times 9", textvariable=self.placeName)
        self.e2.grid(row=1, column=1, sticky=tk.W) 
        self.saveName = tk.StringVar(self)
        self.e3 = tk.Entry(self, width=40, font="Times 9", textvariable=self.saveName)
        self.e3.grid(row=3, column=1, sticky=tk.W)
        self.whichResult = tk.StringVar(self)
        self.e4 = tk.Entry(self, width=5, font="Times 9", textvariable=self.whichResult)
        self.e4.grid(row=1, column=1, sticky=tk.E)
        ttk.Button(self, text="Browse", command=self.SaveFile).grid(row=2, column=2, sticky=tk.W)
        self.shpOutput = tk.Text(self, height=1, width=40, font="Times 9")
        self.shpOutput.grid(row=2, column=1, sticky=tk.W)
        ttk.Button(self, text="Execute", width=12, command=self.getPoly).grid(row=4, column=1)
                
    def SaveFile(self):
        global shpLocation
        shpLocation = askdirectory(initialdir="\\",
                                  title = "Choose output folder for shapefiles")
        self.shpOutput.delete("1.0", tk.END)
        self.shpOutput.insert(tk.END, shpLocation)
        
    def getPoly(self):
        if len(self.whichResult.get()) > 0:
            bk.getPolyData(self.placeName.get(), self.shpOutput.get("1.0",'end-1c'), self.saveName.get(), whichResult=self.whichResult.get())
        elif not self.whichResult.get():
            bk.getPolyData(self.placeName.get(), self.shpOutput.get("1.0",'end-1c'), self.saveName.get())
            
#    def createCanvasImage(self):
#        canvas = tk.Canvas(self, width=1000, height=200)
#        canvas.grid(row=0, column=0, rowspan=10, columnspan=7)
#        img = Image.open(r"C:\Users\OmrAkn\Desktop\YuksekLisansTezUygulama\SATRAP\s5uaze.png")
#        canvas.image = ImageTk.PhotoImage(img)
#        canvas.create_image(0, 0, image=canvas.image, anchor=tk.NW)
          
class HelpMenu(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
#        self.createCanvasImage()
        
        ttk.Button(self, text="Back", command=lambda: controller.show_frame()).grid(row=0, column=0, sticky=tk.W)
               
        tk.Label(self, text="1) Input polygon boundary data should be in polygon shapefile format and origins or destinations data should be in point shapefile format.\n\
2) Region name should be checked first on https://nominatim.openstreetmap.org. If there is no region name on the website search, region's network is unaccessible.\n\
3) User should choose the path where the road network of the area of interest and the result of the analysis is stored in shapefile format via 'Shapefile Output Folder' \n\
Optional Selections; \n\
4) Available transportation modes on OSM database are;\n\
        'drive' - get drivable public streets (but not service roads)\n\
        'drive_service' - get drivable public streets, including service roads\n\
        'walk' - get all streets and paths that pedestrians can use (this network type ignores one-way directionality)\n\
        'bike' - get all streets and paths that cyclists can use\n\
        'all' - download all (non-private) OSM streets and paths\n\
        'all_private' - download all OSM streets and paths, including private-access ones\n\
5) User could choose the path where the webmap that is generated by the result of analysis is stored.", font=("Verdana", 8), justify=tk.LEFT).grid(row=1, sticky=tk.E)
            
#    def createCanvasImage(self):
#        canvas = tk.Canvas(self, width=1000, height=200)
#        canvas.grid(row=0, column=0, rowspan=10, columnspan=7)
#        img = Image.open(r"C:\Users\OmrAkn\Desktop\YuksekLisansTezUygulama\SATRAP\s5uaze.png")
#        canvas.image = ImageTk.PhotoImage(img)
#        canvas.create_image(0, 0, image=canvas.image, anchor=tk.NW)
        
class Centrality(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        tk.Frame.update(self)
        tk.Frame.grid_columnconfigure(self, 0, weight=1)
        tk.Frame.grid_columnconfigure(self, 1, weight=1)
        tk.Frame.grid_columnconfigure(self, 2, weight=1)
        tk.Frame.grid_columnconfigure(self, 3, weight=1)
        tk.Frame.grid_columnconfigure(self, 4, weight=1)
        tk.Frame.grid_columnconfigure(self, 5, weight=1)
#        self.createCanvasImage()
        
        backButton = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        backButton.grid(row=0, column=0, sticky=tk.W)
        
        helpButton = ttk.Button(self, text="Help",
                           command=lambda: controller.show_frame(HelpMenu))
        helpButton.grid(row=0, column=5, sticky=tk.E) 
        
        # Alghoritms
        optionlist = ["Degree", "Betweenness", "Closeness"]
        self.dropvar = tk.StringVar(self)
        self.dropvar.set("Degree")
        tk.Label(self, text="Analysis method").grid(row=3, column=5, columnspan=2)
        dropmenu = tk.OptionMenu(self, self.dropvar, *optionlist)
        dropmenu.grid(row=4, column=5, columnspan=2)
        
        # Data Acquisiton Method
        optionlist2 = ["From boundary", "From region name"]
        self.dropvar2 = tk.StringVar(self)
        self.dropvar2.set("From boundary")
        tk.Label(self, text="Data input method").grid(row=3, column=3, columnspan=2)
        dropmenu2 = tk.OptionMenu(self, self.dropvar2, *optionlist2)
        dropmenu2.grid(row=4, column=3, columnspan=2)
        self.dropvar2.trace("w", self.chgdrp)

        # Buttons & Labes
        tk.Label(self, text="Polygon Boundary of area").grid(row=2, sticky=tk.E)
        tk.Label(self, text="Region Name / Result Number").grid(row=3, sticky=tk.E)
        tk.Label(self, text="Transportation Mode (Optional)").grid(row=4, sticky=tk.E)
        tk.Label(self, text="Webmap Output Path (Optional)").grid(row=5, sticky=tk.E)
        tk.Label(self, text="Shapefile Output Folder").grid(row=6, sticky=tk.E)
        self.browseButton = ttk.Button(self, text="Browse", command=self.OpenFile)
        self.browseButton.grid(row=2, column=2, sticky=tk.W)
        ttk.Button(self, text="Browse", command=self.SaveFile).grid(row=5, column=2, sticky=tk.W)
        ttk.Button(self, text="Browse", command=self.SaveFile2).grid(row=6, column=2, sticky=tk.W)
        ttk.Button(self, text="Execute", width=12, command=self.returnedFunction).grid(row=8, column=5, columnspan=2)
        self.shpInput = tk.Text(self, height=1, width=40, font="Times 9")
        self.shpInput.grid(row=2, column=1, sticky=tk.W)
        self.webmapOutput = tk.Text(self, height=1, width=40, font="Times 9")
        self.webmapOutput.grid(row=5, column=1, sticky=tk.W)
        self.shpOutput = tk.Text(self, height=1, width=40, font="Times 9")
        self.shpOutput.grid(row=6, column=1, sticky=tk.W)
        self.placeName = tk.StringVar(self)
        self.e2 = tk.Entry(self, width=35, font="Times 9", textvariable=self.placeName)
        self.e2.config(state="disabled")
        self.e2.grid(row=3, column=1, sticky=tk.W)
        self.networkType = tk.StringVar(self)
        self.e3 = tk.Entry(self, width=40, font="Times 9", textvariable=self.networkType)
        self.e3.grid(row=4, column=1, sticky=tk.W)
        self.whichResult = tk.StringVar(self)
        self.e4 = tk.Entry(self, width=5, font="Times 9", textvariable=self.whichResult)
        self.e4.config(state="disabled")
        self.e4.grid(row=3, column=1, sticky=tk.E)

    # Choosing function based on user selection
    def returnedFunction(self):
        funcs = {"Degree": self.degreeCentrality,
                 "Betweenness": self.betweennessCentrality,
                 "Closeness": self.closenessCentrality}
        function = funcs[self.dropvar.get()]
        return function()

    # Getting Network
    def findG(self):
        if self.dropvar2.get() == "From boundary":
            if len(self.networkType.get()) > 0:
                G = bk.networkFromPolygon(self.shpInput.get("1.0",'end-1c'), self.networkType.get())
            else:
                G = bk.networkFromPolygon(self.shpInput.get("1.0",'end-1c'))
        elif self.dropvar2.get() == "From region name":
            if len(self.networkType.get()) > 0 and len(self.whichResult.get()) > 0:
                G = bk.networkFromPlaceName(self.placeName.get(), networkType=self.networkType.get(), whichResult=self.whichResult.get())
            elif len(self.networkType.get()) > 0 and not self.whichResult.get():
                G = bk.networkFromPlaceName(self.placeName.get(), networkType=self.networkType.get())
            elif len(self.networkType.get()) == 0 and self.whichResult.get():
                G = bk.networkFromPlaceName(self.placeName.get(), whichResult=self.whichResult.get())
            else:
                G = bk.networkFromPlaceName(self.placeName.get())
        return G

    def degreeCentrality(self):
        print("Calculating Degree Centrality..")
        G = self.findG()
        if len(self.webmapOutput.get("1.0",'end-1c')) > 0:
            bk.degreeCentrality(G, self.shpOutput.get("1.0",'end-1c'), self.webmapOutput.get("1.0",'end-1c'))
        else:
            bk.degreeCentrality(G, self.shpOutput.get("1.0",'end-1c'))
            
    def betweennessCentrality(self):
        print("Calculating Betweenness..")
        G = self.findG()
        if len(self.webmapOutput.get("1.0",'end-1c')) > 0:
            bk.betweennessCentrality(G, self.shpOutput.get("1.0",'end-1c'), self.webmapOutput.get("1.0",'end-1c'))
        else:
            bk.betweennessCentrality(G, self.shpOutput.get("1.0",'end-1c'))
        
    def closenessCentrality(self):
        print("Calculating Closeness..")
        G = self.findG()
        if len(self.webmapOutput.get("1.0",'end-1c')) > 0:
            bk.closenessCentrality(G, self.shpOutput.get("1.0",'end-1c'), self.webmapOutput.get("1.0",'end-1c'))
        else:
            bk.closenessCentrality(G, self.shpOutput.get("1.0",'end-1c'))
        
    def chgdrp(self, *args):
        if self.dropvar2.get() == "From boundary":
            self.browseButton.config(state="normal")
            self.e2.config(state="disabled")
            self.e4.config(state="disabled")
            self.shpInput.config(state="normal")
        elif self.dropvar2.get() == "From region name":
            self.browseButton.config(state="disabled")
            self.e2.config(state="normal")
            self.e4.config(state="normal")
            self.shpInput.config(state="disabled")

    def OpenFile(self):
        shpLocation = askopenfilename(initialdir="\\", filetypes =(("Shapefile", "*.shp"),("All Files","*.*")),
                               title = "Choose origin shapefile")
        self.shpInput.delete("1.0", tk.END)
        self.shpInput.insert(tk.END, shpLocation)
    
    def SaveFile(self):
        webmapLocation = asksaveasfilename(initialdir="\\", filetypes=(("Html Files", "*.html"),("All Files","*.*")),
                                  title = "Choose output path for webmap")
        if webmapLocation[-5:] == ".html":
            pass
        else:
            webmapLocation += ".html"
        self.webmapOutput.delete("1.0", tk.END)
        self.webmapOutput.insert(tk.END, webmapLocation)
        
    def SaveFile2(self):
        shpOutputLocation = askdirectory(initialdir="\\",
                                  title = "Choose output folder for shapefiles")
        self.shpOutput.delete("1.0", tk.END)
        self.shpOutput.insert(tk.END, shpOutputLocation)

#    def createCanvasImage(self):
#        canvas = tk.Canvas(self, width=1000, height=200)
#        canvas.grid(row=0, column=0, rowspan=10, columnspan=7)
#        img = Image.open(r"C:\Users\OmrAkn\Desktop\YuksekLisansTezUygulama\SATRAP\s5uaze.png")
#        canvas.image = ImageTk.PhotoImage(img)
#        canvas.create_image(0, 0, image=canvas.image, anchor=tk.NW)
        
class Accessibility(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.grid_columnconfigure(self, 0, weight=1)
        tk.Frame.grid_columnconfigure(self, 1, weight=1)
        tk.Frame.grid_columnconfigure(self, 2, weight=1)
        tk.Frame.grid_columnconfigure(self, 3, weight=1)
        tk.Frame.grid_columnconfigure(self, 4, weight=1)
        tk.Frame.grid_columnconfigure(self, 5, weight=1)
        tk.Frame.grid_columnconfigure(self, 6, weight=1)
        tk.Frame.grid_columnconfigure(self, 7, weight=1)
#        self.createCanvasImage()
        
        backButton = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        backButton.grid(row=0, column=0, sticky=tk.W)
        
        helpButton = ttk.Button(self, text="Help",
                           command=lambda: controller.show_frame(HelpMenu))
        helpButton.grid(row=0, column=3, sticky=tk.E)
        
        tk.Label(self, text="Origins").grid(row=2, sticky=tk.E)
        tk.Label(self, text="Destinations").grid(row=3, sticky=tk.E)
        tk.Label(self, text="Webmap Output Path (Optional)").grid(row=5, sticky=tk.E)
        tk.Label(self, text="Transportation Mode (Optional)").grid(row=4, sticky=tk.E)
        tk.Label(self, text="Shapefile Output Folder").grid(row=6, sticky=tk.E)
        tk.Label(self, text="Distance Threshold (m)").grid(row=7, sticky=tk.E)
        ttk.Button(self, text="Browse", command=self.OpenFile1).grid(row=2, column=2, sticky=tk.W)
        ttk.Button(self, text="Browse", command=self.OpenFile2).grid(row=3, column=2, sticky=tk.W)
        ttk.Button(self, text="Browse", command=self.SaveFile).grid(row=5, column=2, sticky=tk.W)
        ttk.Button(self, text="Browse", command=self.SaveFile2).grid(row=6, column=2, sticky=tk.W)
        ttk.Button(self, text="Execute", width=12, command=self.returned_func).grid(row=6, column=3)
        self.originInput = tk.Text(self, height=1, width=40, font="Times 9")
        self.originInput.grid(row=2, column=1, sticky=tk.W)
        self.destInput = tk.Text(self, height=1, width=40, font="Times 9")
        self.destInput.grid(row=3, column=1, sticky=tk.W)
        self.webmapOutput = tk.Text(self, height=1, width=40, font="Times 9")
        self.webmapOutput.grid(row=5, column=1, sticky=tk.W)
        self.shpOutput = tk.Text(self, height=1, width=40, font="Times 9")
        self.shpOutput.grid(row=6, column=1, sticky=tk.W) 
        self.networkType = tk.StringVar(self)
        self.e1 = tk.Entry(self, width=40, font="Times 9", textvariable=self.networkType)
        self.e1.grid(row=4, column=1, sticky=tk.W)
        self.threshold = tk.StringVar(self)
        self.e2 = tk.Entry(self, width=40, font="Times 9", textvariable=self.threshold)
        self.e2.config(state="disabled")
        self.e2.grid(row=7, column=1, sticky=tk.W)
        
        optionlist = ["Potential Accessibility", "Daily Accessibility"]
        self.dropvar = tk.StringVar(self)
        self.dropvar.set("Potential Accessibility")
        tk.Label(self, text="Analysis method").grid(row=2, column=3)
        dropmenu = tk.OptionMenu(self, self.dropvar, *optionlist)
        dropmenu.grid(row=3, column=3)
        self.dropvar.trace("w", self.chgdrp)
        
    def returned_func(self):
        funcs = {"Potential Accessibility": self.potentialAccessibility,
                 "Daily Accessibility": self.dailyAccessibility}
        function = funcs[self.dropvar.get()]
        return function() 
    
    def origdest(self):
        if len(self.networkType.get()) > 0:
            route_geom, nodes, G_proj = bk.origindestination(self.originInput.get("1.0",'end-1c'), self.destInput.get("1.0",'end-1c'),
                                                             self.networkType.get())
        else:
            route_geom, nodes, G_proj = bk.origindestination(self.originInput.get("1.0",'end-1c'), self.destInput.get("1.0",'end-1c'))
        return route_geom, nodes, G_proj      
    
    def potentialAccessibility(self):
        route_geom, nodes, G_proj = self.origdest()
        if len(self.webmapOutput.get("1.0",'end-1c')) > 0:
            bk.potentialAccessibility(route_geom, nodes, G_proj, self.shpOutput.get("1.0",'end-1c'),
                                      self.webmapOutput.get("1.0",'end-1c'))
        else:
            bk.potentialAccessibility(route_geom, nodes, G_proj, self.shpOutput.get("1.0",'end-1c'))
            
    def dailyAccessibility(self):
        route_geom, nodes, G_proj = self.origdest()
        if len(self.threshold.get()) > 0 and len(self.webmapOutput.get("1.0",'end-1c')) > 0:
            bk.dailyAccessibility(route_geom, nodes, G_proj, self.shpOutput.get("1.0",'end-1c'), self.threshold.get(),
                                  self.webmapOutput.get("1.0",'end-1c'))
        elif len(self.threshold.get()) > 0 and len(self.webmapOutput.get("1.0",'end-1c')) > 0:
            bk.dailyAccessibility(route_geom, nodes, G_proj, self.shpOutput.get("1.0",'end-1c'), self.threshold.get())
        elif len(self.threshold.get()) == 0 and len(self.webmapOutput.get("1.0",'end-1c')) == 0:
            bk.dailyAccessibility(route_geom, nodes, G_proj, self.shpOutput.get("1.0",'end-1c'), 3000,
                                  self.webmapOutput.get("1.0",'end-1c'))
        else:
            bk.dailyAccessibility(route_geom, nodes, G_proj, self.shpOutput.get("1.0",'end-1c'))

    def chgdrp(self, *args):
        if self.dropvar.get() == "Potential Accessibility":
            self.e2.config(state="disabled")
        elif self.dropvar.get() == "Daily Accessibility":
            self.e2.config(state="normal")
            
    def OpenFile1(self):
        originLocation = askopenfilename(initialdir="\\", filetypes =(("Shapefile", "*.shp"),("All Files","*.*")),
                               title = "Choose origin shapefile")
        self.originInput.delete("1.0", tk.END)
        self.originInput.insert(tk.END, originLocation)

    def OpenFile2(self):
        destinationLocation = askopenfilename(initialdir="\\", filetypes =(("Shapefile", "*.shp"),("All Files","*.*")),
                               title = "Choose destination shapefile")
        self.destInput.delete("1.0", tk.END)
        self.destInput.insert(tk.END, destinationLocation)
        
    def SaveFile(self):
        webmapLocation = asksaveasfilename(initialdir="\\", filetypes=(("Html Files", "*.html"),("All Files","*.*")),
                                  title = "Choose output path for webmap")
        if webmapLocation[-5:] == ".html":
            pass
        else:
            webmapLocation += ".html"
        self.webmapOutput.delete("1.0", tk.END)
        self.webmapOutput.insert(tk.END, webmapLocation)
        
    def SaveFile2(self):
        shpOutputLocation = askdirectory(initialdir="\\",
                                  title = "Choose output folder for shapefiles")
        self.shpOutput.delete("1.0", tk.END)
        self.shpOutput.insert(tk.END, shpOutputLocation)

#    def createCanvasImage(self):
#        canvas = tk.Canvas(self, width=1000, height=200)
#        canvas.grid(row=0, column=0, rowspan=10, columnspan=7)
#        img = Image.open(r"C:\Users\OmrAkn\Desktop\YuksekLisansTezUygulama\SATRAP\s5uaze.png")
#        canvas.image = ImageTk.PhotoImage(img)
#        canvas.create_image(0, 0, image=canvas.image, anchor=tk.NW)
            
app = Application()
app.mainloop()