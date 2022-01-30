from cgitb import grey
from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")
link = StringVar()

Label(root, text = 'ENTER THE LINK:', font = 'calibri 20 bold').place(x= 180 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOAD COMPLETE', font = 'arial 20', bg='grey' ).place(x=100 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 20 bold' ,bg = 'yellow', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()