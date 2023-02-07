import tkinter as tk
from tkinter import ttk
import os,pygame,keyboard,time
pygame.mixer.init()
pygame.mixer.set_num_channels(10)
#global variables
global setw,main,audiow,selectwindow,keylist,songlist,audiolist,ogtime,stor
songlist=(os.listdir("./sound_files"))
ogtime=time.time()

keylist=["num 0","num 1","num 2","num 3","num 4","num 5","num 6","num 7","num 8","num 9"]
#opening files
with open("config.txt","r+",encoding="utf8") as config: 
    configfile=config.read()
with open("interact.txt","r+",encoding="utf8") as interact: 
    interactfile=interact.read()
with open("interact.txt","w+",encoding="utf8") as interact: 
    with open("start.txt","r+",encoding="utf8") as start: 
        x=start.read()
    interact.write(x)

#multiple variable storage
stor={"config":configfile,"interact":interactfile}


#functions
def locate(file,item,no): #file is which file to check,item is parameter, no is number of parameters
    para=stor[file]
    b=para.find(item+"=")+len(item)+1
    c=0
    for i in range(0,no):
        if i==0:
            a=(para.find("|;",para.find(item+"=")))
        elif i>0:
            a=(para.find("|;",b))
        if i==no-1:
            c=para[b:a]
        b=a+2
    return c

def replacing(file,item,no,word): #file is which file to check,item is parameter, no is number of parameters,word is what is goning to replace the og

    para=stor[file]
    b=para.find(item+"=")+len(item)+1
    for i in range(0,no):
        if i==0:
            a=(para.find("|;",para.find(item+"=")))
        elif i>0:
            a=(para.find("|;",b))
        if i==no-1:
            stor[file]=stor[file][:b]+stor[file][b:a].replace(para[b:a],word)+stor[file][a:]
            if file=="config":
                with open("config.txt","w+",encoding="utf8") as config:
                    config.write(stor[file])
            if file=="interact":
                with open("interact.txt","w+",encoding="utf8")as config:
                    config.write(stor[file])
                    print(stor[file])
            

        b=a+2
    if no==-1:
        a=len(stor[file][:b])+stor[file][b:].index("|;;")
        stor[file]=stor[file][:b]+stor[file][b:a].replace(para[b:a],word)+stor[file][a:]
        if file=="config":
            
            with open("config.txt","w+",encoding="utf8") as config:
                config.write(stor[file])


    pass

def size():
    global audiow
    print(audiow.winfo_height())
    print(audiow.winfo_width())
    audiow.after(30,size)

def mainht(percent,window):
    global main,setw,audiow,selectwindow

    if window=="main":
        x=main.winfo_height()
    elif window=="setw":
        x=setw.winfo_height()
    elif window=="audiow":
        x=audiow.winfo_height()
    
    a=percent*(x/100)
    return a

def mainwt(percent,window):
    global main,setw,audiow,selectwindow

    if window=="main":
        x=main.winfo_width()
    elif window=="setw":
        x=setw.winfo_width()
    elif window=="audiow":
        x=audiow.winfo_width()
    


    a=percent*(x/100)
    return a

def mainbt():
    r=mainwt(81.6,"main")
    t=mainht(10,"main")
    frame7.place(x=r-164,y=t)
    frame8.place(x=r-82,y=t)
    frame9.place(x=r,y=t)
    frame4.place(x=r-164,y=t+94)
    frame5.place(x=r-82,y=t+94)
    frame6.place(x=r,y=t+94)
    frame1.place(x=r-164,y=t+188)
    frame2.place(x=r-82,y=t+188)
    frame3.place(x=r,y=t+188)
    
    textframe7.place(x=r-164,y=t+60)
    textframe8.place(x=r-82,y=t+60)
    textframe9.place(x=r,y=t+60)
    textframe4.place(x=r-164,y=t+154)
    textframe5.place(x=r-82,y=t+154)
    textframe6.place(x=r,y=t+154)
    textframe1.place(x=r-164,y=t+248)
    textframe2.place(x=r-82,y=t+248)
    textframe3.place(x=r,y=t+248)

    b0.bt.place(x=r-84,y=t+280)
    b1.bt.pack(side="top")
    b2.bt.pack(side="top")
    b3.bt.pack(side="top")
    b4.bt.pack(side="top")
    b5.bt.pack(side="top")
    b6.bt.pack(side="top")
    b7.bt.pack(side="top")
    b8.bt.pack(side="top")
    b9.bt.pack(side="top")
    slabel1.lb.pack(side="bottom",padx=0)
    slabel2.lb.pack(side="bottom")
    slabel3.lb.pack(side="bottom")
    slabel4.lb.pack(side="bottom")
    slabel5.lb.pack(side="bottom")
    slabel6.lb.pack(side="bottom")
    slabel7.lb.pack(side="bottom")
    slabel8.lb.pack(side="bottom")
    slabel9.lb.pack(side="bottom")
    b1.lb.pack(side="bottom")
    b2.lb.pack(side="bottom")
    b3.lb.pack(side="bottom")
    b4.lb.pack(side="bottom")
    b5.lb.pack(side="bottom")
    b6.lb.pack(side="bottom")
    b7.lb.pack(side="bottom")
    b8.lb.pack(side="bottom")
    b9.lb.pack(side="bottom")
    
    #setb.bt.place(x=5,y=5)
    main.after(30,mainbt)

def playsnd(channelnum,file,fxn):
    if fxn=="play":
        pygame.mixer.Channel(channelnum).play(pygame.mixer.Sound(file))
    elif fxn=="pause":
        pygame.mixer.Channel(channelnum).pause()
    elif fxn=="unpause":
        pygame.mixer.Channel(channelnum).unpause()

def butt(number):
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    if number==1:
        return b1.bt
    elif number==2:
        return b2.bt
    elif number==3:
        return b3.bt
    elif number==4:
        return b4.bt
    elif number==5:
        return b5.bt
    elif number==6:
        return b6.bt
    elif number==7:
        return b7.bt
    elif number==8:
        return b8.bt
    elif number==9:
        return b9.bt
    
def mus(fxn,channel,file):
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    with open("interact.txt","r+",encoding="utf8") as interact: 
        z=interact.read()
        if locate("interact","connected",1)=="False" and (locate("interact","status",1)[0:7]=="offline" or locate("interact","status",1)=="starting"):
            if fxn=="play":
                playsnd(channel,"sound_files/"+file,"play")
                butt(channel).config(image=pauseimg,command=lambda:mus("pause",channel,file))
            elif fxn=="pause":
                playsnd(channel,"sound_files/"+file,"pause")
                butt(channel).config(image=playimg,command=lambda:mus("unpause",channel,file))
            elif fxn=="unpause":
                playsnd(channel,"sound_files/"+file,"unpause")
                butt(channel).config(image=pauseimg,command=lambda:mus("pause",channel,file))
        
        elif locate("interact","connected",1)=="True" and locate("interact","status",1)[0:6]=="online":
            if fxn=="play":
                if locate("interact","playstate",1)=="False":
                    replacing("interact","player",1,fxn)
                    replacing("interact","player",2,file)
                    replacing("interact","player",3,str(channel))
                    replacing("interact","player",4,"1")
                
                    butt(channel).config(image=pauseimg,command=lambda:mus("pause",channel,file))
                
            elif fxn=="pause":
                replacing("interact","player",1,fxn)
                replacing("interact","player",2,file)
                replacing("interact","player",3,str(channel))
                replacing("interact","player",4,"1")
                
                butt(channel).config(image=playimg,command=lambda:mus("unpause",channel,file))
            elif fxn=="unpause":
                if locate("interact","player",2)==file:
                    replacing("interact","player",1,fxn)
                    replacing("interact","player",2,file)
                    replacing("interact","player",3,str(channel))
                    replacing("interact","player",4,"1")
                else:
                    replacing("interact","player",1,"play")
                    replacing("interact","player",2,file)
                    replacing("interact","player",3,str(channel))
                    replacing("interact","player",4,"1")
                
                butt(channel).config(image=pauseimg,command=lambda:mus("pause",channel,file))

        

def musicstop():
    pygame.mixer.stop()
    b1.bt.config(image=playimg,command=lambda:mus("play",1,audiolist[0]))
    b2.bt.config(image=playimg,command=lambda:mus("play",2,audiolist[1]))
    b3.bt.config(image=playimg,command=lambda:mus("play",3,audiolist[2]))
    b4.bt.config(image=playimg,command=lambda:mus("play",4,audiolist[3]))
    b5.bt.config(image=playimg,command=lambda:mus("play",5,audiolist[4]))
    b6.bt.config(image=playimg,command=lambda:mus("play",6,audiolist[5]))
    b7.bt.config(image=playimg,command=lambda:mus("play",7,audiolist[6]))
    b8.bt.config(image=playimg,command=lambda:mus("play",8,audiolist[7]))
    b9.bt.config(image=playimg,command=lambda:mus("play",9,audiolist[8]))

    #pygame.mixer.init()
    #pygame.mixer.set_num_channels(10)

def test():
    global stor
    with open("interact.txt","r+",encoding="utf8") as interact:
            interactfile=interact.read()
            stor={"config":configfile,"interact":interactfile}
    
    if locate("interact","test",1)=="0":
        
        replacing("interact","test",1,"1")

def makeaudlist():
    global audiolist
    r=""
    for i in range(1,10):
        
        r+=(locate("config","AudioFiles",i)+",")
    r=r[:-1]+"]"
    audiolist=list(eval(r))

def songfinder(self,num):
    try:
        a=songlist.index(audiolist[num-1])
        return self.cb.current(a)
    except:
        return self.cb.set("SAVED FILE NOT FOUND")

def framer(i):
    if i==1:
        return frame1
    elif i==2:
        return frame2
    elif i==3:
        return frame3
    elif i==4:
        return frame4
    elif i==5:
        return frame5
    elif i==6:
        return frame6
    elif i==7:
        return frame7
    elif i==8:
        return frame8
    elif i==9:
        return frame9

def textframer(i):
    if i==1:
        return textframe1
    elif i==2:
        return textframe2
    elif i==3:
        return textframe3
    elif i==4:
        return textframe4
    elif i==5:
        return textframe5
    elif i==6:
        return textframe6
    elif i==7:
        return textframe7
    elif i==8:
        return textframe8
    elif i==9:
        return textframe9
    
def audframer(i):
    global audframe1,audframe2,audframe3,audframe4,audframe5,audframe6,audframe7,audframe8,audframe9,audframe10
    if i==1:
        return audframe1
    elif i==2:
        return audframe2
    elif i==3:
        return audframe3
    elif i==4:
        return audframe4
    elif i==5:
        return audframe5
    elif i==6:
        return audframe6
    elif i==7:
        return audframe7
    elif i==8:
        return audframe8
    elif i==9:
        return audframe9
    elif i==10:
        return audframe10
    
def checkwhetersaved():
    global audiolist,songbox1,songbox2,songbox3,songbox4,songbox5,songbox6,songbox7,songbox8,songbox9,saveaud1,saveaud2,saveaud3,saveaud4,saveaud5,saveaud6,saveaud7,saveaud8,saveaud9,saveall
    c1=songbox1.cb.get()!=audiolist[songbox1.nb-1]
    c2=songbox2.cb.get()!=audiolist[songbox2.nb-1]
    c3=songbox3.cb.get()!=audiolist[songbox3.nb-1]
    c4=songbox4.cb.get()!=audiolist[songbox4.nb-1]
    c5=songbox5.cb.get()!=audiolist[songbox5.nb-1]
    c6=songbox6.cb.get()!=audiolist[songbox6.nb-1]
    c7=songbox7.cb.get()!=audiolist[songbox7.nb-1]
    c8=songbox8.cb.get()!=audiolist[songbox8.nb-1]
    c9=songbox9.cb.get()!=audiolist[songbox9.nb-1]
    

    if songbox1.cb.get()!=audiolist[songbox1.nb-1]:
        saveaud1.bt.config(text="SAVE") 
    if songbox2.cb.get()!=audiolist[songbox2.nb-1]:
        saveaud2.bt.config(text="SAVE") 
    if songbox3.cb.get()!=audiolist[songbox3.nb-1]:
        saveaud3.bt.config(text="SAVE") 
    if songbox4.cb.get()!=audiolist[songbox4.nb-1]:
        saveaud4.bt.config(text="SAVE") 
    if songbox5.cb.get()!=audiolist[songbox5.nb-1]:
        saveaud5.bt.config(text="SAVE") 
    if songbox6.cb.get()!=audiolist[songbox6.nb-1]:
        saveaud6.bt.config(text="SAVE") 
    if songbox7.cb.get()!=audiolist[songbox7.nb-1]:
        saveaud7.bt.config(text="SAVE") 
    if songbox8.cb.get()!=audiolist[songbox8.nb-1]:
        saveaud8.bt.config(text="SAVE") 
    if songbox9.cb.get()!=audiolist[songbox9.nb-1]:
        saveaud9.bt.config(text="SAVE") 
    if c1 or c2 or c3 or c4 or c5 or c6 or c7 or c8 or c9:
        saveall.bt.config(text="SAVE")

    main.after(30,checkwhetersaved)
pygame.init()


def DetectKeyPress():
    global ogtime,keylist
    currenttime=time.time()
    

def whichkey():
    global keylist
    if keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt"):
        if keyboard.is_pressed(keylist[0]):
            time.sleep(0.25)
            b0.bt.invoke()
        elif keyboard.is_pressed(keylist[1]):
            time.sleep(0.25)
            b1.bt.invoke()
        elif keyboard.is_pressed(keylist[2]):
            time.sleep(0.25)
            b2.bt.invoke()
        elif keyboard.is_pressed(keylist[3]):
            time.sleep(0.25)
            b3.bt.invoke()
        elif keyboard.is_pressed(keylist[4]):
            time.sleep(0.25)
            b4.bt.invoke()
        elif keyboard.is_pressed(keylist[5]):
            time.sleep(0.25)
            b5.bt.invoke()
        elif keyboard.is_pressed(keylist[6]):
            time.sleep(0.25)
            b6.bt.invoke()
        elif keyboard.is_pressed(keylist[7]):
            time.sleep(0.25)
            b7.bt.invoke()
        elif keyboard.is_pressed(keylist[8]):
            time.sleep(0.25)
            b8.bt.invoke()
        elif keyboard.is_pressed(keylist[9]):
            time.sleep(0.25)
            b9.bt.invoke()
  
    main.after(30,whichkey)
        
def disconnector():
    global stor
    with open("interact.txt","r+",encoding="utf8") as interact:
            interactfile=interact.read()
            stor={"config":configfile,"interact":interactfile}
    if locate("interact","status",1)=="offline0":
        replacing("interact","status",1,"online1")
        #if locate("interact","connected",1)=="True":
        #    disbut.bt.config(text="Discord\nConnected",bg="green")
        #elif locate("interact","connected",1)=="False":
        #    print("sssss")
        #    disbut.bt.config(text="Discord\nConnecting",bg="blue",fg="white")
        #    main.update()
            

            

        
    elif locate("interact","status",1)=="online0":
        replacing("interact","status",1,"offline1")
        disbut.bt.config(text="Discord\nDisconnected",bg="red")
    
def conditionchecker():
    global stor
    with open("interact.txt","r+",encoding="utf8") as interact:
        interactfile=interact.read()
        stor={"config":configfile,"interact":interactfile}
    if locate("interact","connected",1)=="True" and locate("interact","status",1)[0:6]=="online":
            disbut.bt.config(text="Discord\nConnected",bg="green")
    elif locate("interact","connected",1)=="False" and locate("interact","status",1)[0:6]=="online":
            disbut.bt.config(text="Discord\nis connecting",bg="blue",fg="white")
    elif locate("interact","connected",1)=="False" and locate("interact","status",1)[0:7]=="offline":
            disbut.bt.config(text="Discord\nDisconnected",bg="red")
    elif locate("interact","connected",1)=="True" and locate("interact","status",1)[0:7]=="offline":
            time.sleep(0.3)
            disbut.bt.config(text="Error",bg="black",fg="white")
    if locate("interact","status",1)=="starting":
            disbut.bt.config(text="Bot\nOffline",bg="black",fg="white")
    
    main.after(30,conditionchecker)
        
   

class musbut:
    def __init__(self,name,window,number=0):
        global audiolist,songlist
        if window=="m":
            self.bt=tk.Button(main,text=name,height=5,width=10)    
            self.lb=tk.Label(main,text=name)

        elif window=="s":
            self.bt=tk.Button(setw,text=name,height=2,width=20) 
            self.lb=tk.Label(setw,text=name)
            
        elif window=="aud":
            self.bt=tk.Button(audframer(number),text=name,height=1,width=10) 
            self.lb=tk.Label(audframer(number),text=name,fg="white",height=1)
            self.cb=tk.ttk.Combobox(audframer(number),values=songlist,width=35)
        elif window=="playsnd":
            self.bt=tk.Button(framer(number),image=playimg,text=name,height=39,width=70) 
            self.lb=tk.Label(framer(number),text=name,fg="black",width=10)
        elif window=="textframe":
            self.bt=tk.Button(textframer(number),image=playimg,text=name,height=39,width=70) 
            self.lb=tk.Label(textframer(number),text=name,fg="black",width=10)
        
        self.nb=number

        




#window config
main=tk.Tk()
main.title("SoundBar")
main.geometry((locate("config","GeoSize",2))+"x"+locate("config","GeoSize",1)+"+30+30")
main.config(bg="#1E1E1E")
#bg=tk.PhotoImage(file="resources/dark_grey_bg.png")
#bg=bg.zoom(25)
#back=tk.Label(main,image=bg)
#back.place(x=0, y=0, relwidth=1, relheight=1)

main.update()

main.after(0,mainbt)

#resources
pixelVirtual = tk.PhotoImage(width=1, height=1)
gear=tk.PhotoImage(file="resources/gear.png")
playimg=tk.PhotoImage(file="resources/play.png")
playimg=playimg.subsample(7)
pauseimg=tk.PhotoImage(file="resources/pause.png")
pauseimg=pauseimg.subsample(7)


makeaudlist()

 
        

def setf():
    global setw
    setw=tk.Toplevel()
    setw.title("Settings")
    setw.geometry((locate("config","SetSize",2))+"x"+(locate("config","SetSize",1)))
    setw.config(bg="#3C3C3C")
    viewsave=0

    def view():
        nonlocal viewsave
        viewsave.bt.place(x=mainwt(51,"setw"),y=mainht(76,"setw"))
        main.after(30,view)

    
    o1=musbut("1","s")
    o2=musbut("2","s")
    o3=musbut("3","s")
    o3.bt.config(text="View",command=view)
    viewsave=musbut("s","s")
    viewsave.bt.config(text="SAVE")
        
    def setbt():
        
        o1.bt.place(x=0,y=0)
        o2.bt.place(x=0,y=40)
        o3.bt.place(x=0,y=80)
        main.after(30,setbt)
    
    view()

    
    main.after(0,setbt)
    setw.mainloop()

def audioass():
    global audiow,keylist,songlist,audiolist,audframe1,audframe2,audframe3,audframe4,audframe5,audframe6,audframe7,audframe8,audframe9,audframe10,songbox1,songbox2,songbox3,songbox4,songbox5,songbox6,songbox7,songbox8,songbox9,saveaud1,saveaud2,saveaud3,saveaud4,saveaud5,saveaud6,saveaud7,saveaud8,saveaud9,saveall
    audiow=tk.Toplevel()
    audiow.title("Audio Assign")
    audiow.geometry((locate("config","AudioAss",2))+"x"+(locate("config","AudioAss",1)))
    audiow.config(bg="#3C3C3C")
    
    audframe1=tk.Frame(audiow,bg="#3c3c3c")
    audframe2=tk.Frame(audiow,bg="#3c3c3c")
    audframe3=tk.Frame(audiow,bg="#3c3c3c")
    audframe4=tk.Frame(audiow,bg="#3c3c3c")
    audframe5=tk.Frame(audiow,bg="#3c3c3c")
    audframe6=tk.Frame(audiow,bg="#3c3c3c")
    audframe7=tk.Frame(audiow,bg="#3c3c3c")
    audframe8=tk.Frame(audiow,bg="#3c3c3c")
    audframe9=tk.Frame(audiow,bg="#3c3c3c")
    audframe10=tk.Frame(audiow,bg="#3c3c3c")
    
    space=musbut(" "*30,"aud",10)

    aud1=musbut(keylist[1],"aud",1)
    aud2=musbut(keylist[2],"aud",2)
    aud3=musbut(keylist[3],"aud",3)
    aud4=musbut(keylist[4],"aud",4)
    aud5=musbut(keylist[5],"aud",5)
    aud6=musbut(keylist[6],"aud",6)
    aud7=musbut(keylist[7],"aud",7)
    aud8=musbut(keylist[8],"aud",8)
    aud9=musbut(keylist[9],"aud",9)
    aud10=musbut("SAVE ALL","aud",10)
    

    songbox1=musbut("1","aud",1)
    songbox2=musbut("2","aud",2)
    songbox3=musbut("3","aud",3)
    songbox4=musbut("4","aud",4)
    songbox5=musbut("5","aud",5)
    songbox6=musbut("6","aud",6)
    songbox7=musbut("7","aud",7)
    songbox8=musbut("8","aud",8)
    songbox9=musbut("9","aud",9)    
        
    songfinder(songbox1,1)
    songfinder(songbox2,2)
    songfinder(songbox3,3)
    songfinder(songbox4,4)
    songfinder(songbox5,5)
    songfinder(songbox6,6)
    songfinder(songbox7,7)
    songfinder(songbox8,8)
    songfinder(songbox9,9)
    
        
    saveaud1=musbut("SAVED","aud",1)
    saveaud2=musbut("SAVED","aud",2)
    saveaud3=musbut("SAVED","aud",3)
    saveaud4=musbut("SAVED","aud",4)
    saveaud5=musbut("SAVED","aud",5)
    saveaud6=musbut("SAVED","aud",6)
    saveaud7=musbut("SAVED","aud",7)
    saveaud8=musbut("SAVED","aud",8)
    saveaud9=musbut("SAVED","aud",9)
    saveall=musbut("SAVED","aud",10)
    def saveallthesongs():
        global audiow,keylist,songlist,audiolist,audframe1,audframe2,audframe3,audframe4,audframe5,audframe6,audframe7,audframe8,audframe9,audframe10,songbox1,songbox2,songbox3,songbox4,songbox5,songbox6,songbox7,songbox8,songbox9,saveaud1,saveaud2,saveaud3,saveaud4,saveaud5,saveaud6,saveaud7,saveaud8,saveaud9
    
        saveall.bt.config(text="SAVED")
        setasaud(0,songbox1.cb.get())
        setasaud(1,songbox2.cb.get())
        setasaud(2,songbox3.cb.get())
        setasaud(3,songbox4.cb.get())
        setasaud(4,songbox5.cb.get())
        setasaud(5,songbox6.cb.get())
        setasaud(6,songbox7.cb.get())
        setasaud(7,songbox8.cb.get())
        setasaud(8,songbox9.cb.get())


    saveaud1.bt.config(command=lambda:setasaud(0,songbox1.cb.get()))
    saveaud2.bt.config(command=lambda:setasaud(1,songbox2.cb.get()))
    saveaud3.bt.config(command=lambda:setasaud(2,songbox3.cb.get()))
    saveaud4.bt.config(command=lambda:setasaud(3,songbox4.cb.get()))
    saveaud5.bt.config(command=lambda:setasaud(4,songbox5.cb.get()))
    saveaud6.bt.config(command=lambda:setasaud(5,songbox6.cb.get()))
    saveaud7.bt.config(command=lambda:setasaud(6,songbox7.cb.get()))
    saveaud8.bt.config(command=lambda:setasaud(7,songbox8.cb.get()))
    saveaud9.bt.config(command=lambda:setasaud(8,songbox9.cb.get()))
    saveall.bt.config(command=lambda:saveallthesongs())
    
    


    def setasaud(listnum,file):
        global audiolist
        if listnum==0:
            x=songbox1.cb.get()
            saveaud1.bt.config(text="SAVED")
        elif listnum==1:
            x=songbox2.cb.get()
            saveaud2.bt.config(text="SAVED")
        elif listnum==2:
            x=songbox3.cb.get()
            saveaud3.bt.config(text="SAVED")
        elif listnum==3:
            x=songbox4.cb.get()
            saveaud4.bt.config(text="SAVED")
        elif listnum==4:
            x=songbox5.cb.get()
            saveaud5.bt.config(text="SAVED")
        elif listnum==5:
            x=songbox6.cb.get()
            saveaud6.bt.config(text="SAVED")
        elif listnum==6:
            x=songbox7.cb.get()
            saveaud7.bt.config(text="SAVED")
        elif listnum==7:
            x=songbox8.cb.get()
            saveaud8.bt.config(text="SAVED")
        elif listnum==8:
            x=songbox9.cb.get()
            saveaud9.bt.config(text="SAVED")
    
        audiolist[listnum]=x
        p="["
        for i in audiolist:
            p=p+"\""+i+"\"|;"
        p+="]"
        replacing("config","AudioFiles",-1,str(p))
        slabel1.lb.config(text=audiolist[0])
        slabel2.lb.config(text=audiolist[1])
        slabel3.lb.config(text=audiolist[2])
        slabel4.lb.config(text=audiolist[3])
        slabel5.lb.config(text=audiolist[4])
        slabel6.lb.config(text=audiolist[5])
        slabel7.lb.config(text=audiolist[6])
        slabel8.lb.config(text=audiolist[7])
        slabel9.lb.config(text=audiolist[8])
        
    def audbt():
        r=mainwt(1,"audiow")
        t=mainht(2,"audiow")
        i=max(len(keylist[1]),len(keylist[2]),len(keylist[3]),len(keylist[4]),len(keylist[5]),len(keylist[6]),len(keylist[7]),len(keylist[8]),len(keylist[9]))
        
        audframe1.place(x=r,y=t)
        audframe2.place(x=r,y=t+43)
        audframe3.place(x=r,y=t+86)
        audframe4.place(x=r,y=t+129)
        audframe5.place(x=r,y=t+172)
        audframe6.place(x=r,y=t+215)
        audframe7.place(x=r,y=t+258)
        audframe8.place(x=r,y=t+301)
        audframe9.place(x=r,y=t+344)
        audframe10.place(x=r,y=t+387)
        

        aud1.lb.config(bg="#3C3C3C",text=keylist[1]+"  ")
        aud2.lb.config(bg="#3C3C3C",text=keylist[2]+"  ")
        aud3.lb.config(bg="#3C3C3C",text=keylist[3]+"  ")
        aud4.lb.config(bg="#3C3C3C",text=keylist[4]+"  ")
        aud5.lb.config(bg="#3C3C3C",text=keylist[5]+"  ")
        aud6.lb.config(bg="#3C3C3C",text=keylist[6]+"  ")
        aud7.lb.config(bg="#3C3C3C",text=keylist[7]+"  ")
        aud8.lb.config(bg="#3C3C3C",text=keylist[8]+"  ")
        aud9.lb.config(bg="#3C3C3C",text=keylist[9]+"  ")
        aud10.lb.config(bg="#3C3C3C",text="SAVE ALL")
        space.lb.config(bg="#3c3c3c")
        
        
    
        saveaud1.bt.grid(row=1,column=4)
        saveaud2.bt.grid(row=2,column=4)
        saveaud3.bt.grid(row=3,column=4)
        saveaud4.bt.grid(row=4,column=4)
        saveaud5.bt.grid(row=5,column=4)
        saveaud6.bt.grid(row=6,column=4)
        saveaud7.bt.grid(row=7,column=4)
        saveaud8.bt.grid(row=8,column=4)
        saveaud9.bt.grid(row=9,column=4)
        saveall.bt.grid(row=10,column=4)
        

        songbox1.cb.grid(row=1,column=2)
        songbox2.cb.grid(row=2,column=2)
        songbox3.cb.grid(row=3,column=2)
        songbox4.cb.grid(row=4,column=2)
        songbox5.cb.grid(row=5,column=2)
        songbox6.cb.grid(row=6,column=2)
        songbox7.cb.grid(row=7,column=2)
        songbox8.cb.grid(row=8,column=2)
        songbox9.cb.grid(row=9,column=2)
        
        
        aud1.lb.grid(row=1,column=1)
        aud2.lb.grid(row=2,column=1)
        aud3.lb.grid(row=3,column=1)
        aud4.lb.grid(row=4,column=1)
        aud5.lb.grid(row=5,column=1)
        aud6.lb.grid(row=6,column=1)
        aud7.lb.grid(row=7,column=1)
        aud8.lb.grid(row=8,column=1)
        aud9.lb.grid(row=9,column=1)
        aud10.lb.grid(row=10,column=2)
        space.lb.grid(row=10,column=1)

        audiow.grid_columnconfigure(1, minsize=3000)
        audiow.grid_columnconfigure(2, minsize=100)
        audiow.grid_columnconfigure(3, minsize=100)
        audiow.grid_columnconfigure(4, minsize=100)
        
        main.after(30,audbt)

    

    
    
    main.after(0,checkwhetersaved)
    main.after(0,audbt)
    #audiow.after(0,size)
    audiow.mainloop()

#class calls

frame1=tk.Frame(main)
frame2=tk.Frame(main)
frame3=tk.Frame(main)
frame4=tk.Frame(main)
frame5=tk.Frame(main)
frame6=tk.Frame(main)
frame7=tk.Frame(main)
frame8=tk.Frame(main)
frame9=tk.Frame(main)
textframe1=tk.Frame(main)
textframe2=tk.Frame(main)
textframe3=tk.Frame(main)
textframe4=tk.Frame(main)
textframe5=tk.Frame(main)
textframe6=tk.Frame(main)
textframe7=tk.Frame(main)
textframe8=tk.Frame(main)
textframe9=tk.Frame(main)

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
frame5.pack()
frame6.pack()
frame7.pack()
frame8.pack()
frame9.pack()
textframe1.pack()
textframe2.pack()
textframe3.pack()
textframe4.pack()
textframe5.pack()
textframe6.pack()
textframe7.pack()
textframe8.pack()
textframe9.pack()



b0=musbut(keylist[0],"m")
b1=musbut(keylist[1],"playsnd",1)
b2=musbut(keylist[2],"playsnd",2)
b3=musbut(keylist[3],"playsnd",3)
b4=musbut(keylist[4],"playsnd",4)
b5=musbut(keylist[5],"playsnd",5)
b6=musbut(keylist[6],"playsnd",6)
b7=musbut(keylist[7],"playsnd",7)
b8=musbut(keylist[8],"playsnd",8)
b9=musbut(keylist[9],"playsnd",9)
#setb=musbut("s","m")
slabel1=musbut(audiolist[0],"textframe",1)
slabel2=musbut(audiolist[1],"textframe",2)
slabel3=musbut(audiolist[2],"textframe",3)
slabel4=musbut(audiolist[3],"textframe",4)
slabel5=musbut(audiolist[4],"textframe",5)
slabel6=musbut(audiolist[5],"textframe",6)
slabel7=musbut(audiolist[6],"textframe",7)
slabel8=musbut(audiolist[7],"textframe",8)
slabel9=musbut(audiolist[8],"textframe",9)


b0.bt.config(command=musicstop)
b1.bt.config(command=lambda:mus("play",1,audiolist[0]))
b2.bt.config(command=lambda:mus("play",2,audiolist[1]))
b3.bt.config(command=lambda:mus("play",3,audiolist[2]))
b4.bt.config(command=lambda:mus("play",4,audiolist[3]))
b5.bt.config(command=lambda:mus("play",5,audiolist[4]))
b6.bt.config(command=lambda:mus("play",6,audiolist[5]))
b7.bt.config(command=lambda:mus("play",7,audiolist[6]))
b8.bt.config(command=lambda:mus("play",8,audiolist[7]))
b9.bt.config(command=lambda:mus("play",9,audiolist[8]))
slabel1.lb.config(anchor="w")
slabel2.lb.config(anchor="w")
slabel3.lb.config(anchor="w")
slabel4.lb.config(anchor="w")
slabel5.lb.config(anchor="w")
slabel6.lb.config(anchor="w")
slabel7.lb.config(anchor="w")
slabel8.lb.config(anchor="w")
slabel9.lb.config(anchor="w")



#setb.bt.configure(height=50,width=50,image=gear,command=setf)

       

spbut=musbut("Assign Audio","m")
spbut.bt.config(command=audioass)
spbut.bt.place(x=0,y=90)

disbut=musbut("Discord\nNot connected","m")
disbut.bt.config(command=disconnector,height=2,bg="red",width=12)
disbut.bt.place(x=680,y=00)



testbut=musbut("Test","m")
#testbut.bt.config(command=test)
#testbut.bt.place(x=0,y=180)

#main.destroy()
#setf()
#audioass()

#---------active code?--------------
main.after(0,whichkey)
main.after(0,conditionchecker)
#DetectKeyPress() 
main.mainloop()