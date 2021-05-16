from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry("800x500")
root.title("YouTube Video Downloder")
Label(root,text="YouTube Video Downloder",font="arial 20 bold").pack()
link =StringVar()
Label(root,text="paste Link Here",font="arial 15 bold",).place(x=160,y=60)
Link_enter = Entry(root,width=50,textvariable=link).place(x=32,y ="90")


def downloader():
    url= YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root,text="Downloaded" ,font="arial 15").place(x=180,y =210)


Button(root,text="Download",font="arial 15 ",bg="Blue",padx=2,command=downloader).place(x= 180,y= 150)
root.mainloop()
