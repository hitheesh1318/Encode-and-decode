from tkinter import *
import base64
root=Tk()
root.geometry("600x400")
root.title("project message encode and decode")
Label(root,text='ENCODE and DECODE', font='arial 20 bold').pack()
Label(root,text='TECHNOOBS',font='Times 24 bold italic').pack(side=BOTTOM)

Text=StringVar()
private_key=StringVar()
mode=StringVar()
result=StringVar()

def Encode(key,message):
    enc=[]
    
    for i in range(len(message)):
        key_c=key[i%len(key)]
        enc.append(chr((ord(message[i])+ord(key_c))%256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def Decode(key,message):
    dec=[]
    mesaage=base64.urlsafe_b64decode(message).decode()
    
    for i in range(len(message)):
        key_c=key[i%len(key)]
        dec=(chr((256+ord(message[i])-ord(key_c))%256))
    return "".join(dec)
def Mode():
    if(mode.get()=='e'):
        result.set(Encode(private_key.get(),Text.get()))
    elif(mode.get()=='d'):
        result.set(Decode(private_key.get(),Text.get()))
    else:
        result.set('invalid')
def Exit():
    root.destroy()
def reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    result.set("")

Label(root,font='Helvetica 16' ,text='MESSAGE').place(x=60,y=60)
Entry(root,font='arial 10',textvariable=Text,bd= 10,bg='white').place(x=310,y=60)

Label(root,font='Helvetica 16' ,text='KEY').place(x=60,y=100)
Entry(root,font='arial 10',textvariable=private_key,bd=10,bg='white').place(x=310,y=100)

Label(root,font='Helvetica 16',text='MODE(e-encode,d-decode)').place(x=60,y=140)
Entry(root,font='arial 10',textvariable=mode,bd=10,bg='white').place(x=310,y=140)

Label(root,font='Helevetica 16',text='RESULT').place(x=60,y=180)
Entry(root,font='arial 10',textvariable=result,bd=10,bg='white').place(x=310,y=180)

Button(root,font='arial 10 bold',text='RESULT',padx=18,bg='LimeGreen',command=Mode).place(x=100,y=240)
Button(root,font='arial 10 bold',text='RESET',width=6,command=reset,bg='LightGray',padx=18).place(x=200,y=240)
Button(root,font='arial 10 bold',text='EXIT',width=6,command=Exit,bg='OrangeRed',padx=18,).place(x=300,y=240)
root.mainloop()
