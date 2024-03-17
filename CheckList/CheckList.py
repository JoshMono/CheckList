from ast import Delete
from cgitb import text
from textwrap import fill
from tkinter import *
from tkinter.messagebox import askquestion
from tkinter.ttk import Treeview
from tkinter.ttk import Style
from turtle import left, width
from typing import Type
import sv_ttk



# Fuctions


def ClearCancel():
    global comfirmClear
    comfirmClear = False
    
    EditBTN.config(text='Edit', bg='chocolate1', command=lambda: EditValue())
    AddBTN.config(bg='spring green', command=lambda: AddNewTask())
    DeleteBTN.config(text='Delete', bg='red2', command=lambda: DeleteValue())
    
    ClearBTN.config(text='Clear', bg='turquoise2', command=lambda: Clear())
    SaveBTN.config(text='Save', bg='slateblue2', command=lambda: None)


comfirmClear = False
def Clear():
    global comfirmClear
    if comfirmClear == False:
        comfirmClear = True
        ClearBTN.config(text="Cancel", bg="red2", command=lambda: ClearCancel())
        SaveBTN.config(text="Ok", bg="spring green", command=lambda: Clear())
        
        AddBTN.config(bg='gray62', command=lambda: None)
        EditBTN.config(bg='gray62', command=lambda: None)
        DeleteBTN.config(bg='gray62', command=lambda: None)
        
    else:
        for i in CheckList.get_children():
            CheckList.delete(i)
            
        ClearCancel()
        


def CancelAdd():
    global EntryField
    global inAddMode
    
    inAddMode = False
    EntryField.destroy()
    
    EditBTN.config(text='Edit', bg='chocolate1', command=lambda: EditValue())
    AddBTN.config(bg='spring green', command=lambda: AddNewTask())
    DeleteBTN.config(text='Delete', bg='red2', command=lambda: DeleteValue())


inAddMode = False
EntryField = None

def AddNewTask():
    global inAddMode
    global EntryField
    
    if inAddMode == False:
        EntryField = Text(menuFrame)
        EntryField.place(relx=0.5,rely=0.25,relwidth=0.95, relheight=0.1, anchor='center')
        
        AddBTN.config(bg='gray62', command=lambda: None)
        DeleteBTN.config(text='Cancel',bg='red2', command=lambda: CancelAdd())
        EditBTN.config(text='Save', bg='spring green', command=lambda: AddNewTask())
        
        inAddMode = True

    else:
        text = EntryField.get(1.0 , END)
        if text == '\n':
            AddBTN.config(text="Needs A Letter", bg="white")
            AddBTN.place(relx=0.5,rely=0.4,relwidth=0.95, relheight=0.08, anchor='center')
        else:
            inAddMode = False
            CheckList.insert("", 'end', values=text.replace(" ", "\ "))
            EntryField.destroy()
            
            EditBTN.config(text='Edit', bg='chocolate1', command=lambda: EditValue())
            AddBTN.config(text='Add', bg='spring green', command=lambda: AddNewTask())
            AddBTN.place(relx=0.5,rely=0.4,relwidth=0.6, relheight=0.08, anchor='center')
            DeleteBTN.config(text='Delete', bg='red2', command=lambda: DeleteValue())


def CancelEdit():
    global inEditMode
    global EntryField
    global tempFocus
    inEditMode = False
    EntryField.destroy()
    CheckList.selection_remove(tempFocus)
    tempFocus = None
    
    EditBTN.config(text='Edit', bg='chocolate1', command=lambda: EditValue())
    AddBTN.config(text='Add', bg='spring green', command=lambda: AddNewTask())
    DeleteBTN.config(text='Delete', bg='red2', command=lambda: DeleteValue())
    



inEditMode = False
tempFocus = None


def EditValue():
    global inEditMode
    global tempFocus
    global EntryField
    if inEditMode == False:
        try:
            
            tempFocus = CheckList.selection()[0]
            print()
            if tempFocus != '':
                
                DeleteBTN.config(text='Cancel',bg='red2', command=lambda: CancelEdit())
                EditBTN.config(text='Save', bg='spring green')
                
                item = CheckList.item(tempFocus)
                text = item.get('values')[0]
                print(item.get('values'))
                AddBTN.config(text=f"{text}", bg='white', command=lambda: None)
                AddBTN.place(relx=0.5,rely=0.4,relwidth=0.95, relheight=0.08, anchor='center')
                EntryField = Text(menuFrame)
                EntryField.place(relx=0.5,rely=0.25,relwidth=0.95, relheight=0.1, anchor='center')
                EntryField.delete(1.0, END)
                EntryField.insert(1.0 ,text)
                inEditMode = True
        except:
            pass
            
    else:
        inEditMode = False
        text = EntryField.get(1.0 , END)
        tempBool = False        
        CheckList.item(tempFocus, text="", values=text.replace(" ", "\ "))
        EntryField.destroy()
        CheckList.selection_remove(tempFocus)
        tempFocus = None
        EditBTN.config(text='Edit', bg='chocolate1')
        AddBTN.config(text='Add', bg='spring green', command=lambda: AddNewTask())
        AddBTN.place(relx=0.5,rely=0.4,relwidth=0.6, relheight=0.08, anchor='center')
        DeleteBTN.config(text='Delete', bg='red2', command=lambda: DeleteValue())
        

def ConfirmDelete(comfirmed, tempRecord):
    if comfirmed:
        global comfirmDelete
        comfirmDelete = True
        DeleteBTN.config(command=lambda: DeleteValue())
        tempRecord = CheckList.selection()[0]   
        CheckList.delete(tempRecord)
        AddBTN.config(text='Add', bg='spring green', command=lambda: AddNewTask())
        AddBTN.place(relx=0.5,rely=0.4,relwidth=0.6, relheight=0.08, anchor='center')
        DeleteBTN.config(text='Delete', bg='red2', command=lambda: DeleteValue())
        EditBTN.config(text='Edit', bg='chocolate1', command=lambda: EditValue())
        comfirmDelete = False
    else:
        CheckList.selection_remove(tempRecord)
        AddBTN.config(text='Add', bg='spring green', command=lambda: AddNewTask())
        AddBTN.place(relx=0.5,rely=0.4,relwidth=0.6, relheight=0.08, anchor='center')
        DeleteBTN.config(text='Delete', bg='red2', command=lambda: DeleteValue())
        EditBTN.config(text='Edit',bg='chocolate1', command=lambda: EditValue())
        comfirmDelete = False


comfirmDelete = False
def DeleteValue():
    global comfirmDelete
    try:
        tempRecord = CheckList.selection()[0]
        item = CheckList.item(tempRecord)
        text = item.get('values')[0]
        if comfirmDelete == False:
            AddBTN.config(text=f"{text}", bg='white', command=lambda: None)
            AddBTN.place(relx=0.5,rely=0.4,relwidth=0.95, relheight=0.08, anchor='center')
            EditBTN.config(text='Ok', bg='spring green', command=lambda: ConfirmDelete(True, tempRecord))
            DeleteBTN.config(text='Cancel', bg='red2', command=lambda: ConfirmDelete(False, tempRecord))
            
    except:
        pass      


# Initialize 
root = Tk()
root.geometry('600x400')


# Style Config
style = Style()



# Frames 
menuFrame = Frame(root, bg='gray88')
mainFrame = Frame(root)

menuFrame.place(x=0,y=0,relwidth=0.2, relheight=1)
mainFrame.place(relx=0.2,rely=0, relwidth=.8, relheight=1)


# Menu Frame
Title = Label(menuFrame, text='Check List', bg='gray88')    
AddBTN = Button(menuFrame, text="Add", bg='spring green',  command=lambda: AddNewTask())
EditBTN = Button(menuFrame, text="Edit", bg='chocolate1', command=lambda: EditValue())
DeleteBTN = Button(menuFrame, text="Delete", bg='red2', command=lambda: DeleteValue())

SaveBTN = Button(menuFrame, text="Save", bg='slateblue2', command=lambda: None)
ClearBTN = Button(menuFrame, text="Clear", bg='turquoise2', command=lambda: Clear())


Title.place(relx=0,rely=0,relwidth=1, relheight=0.1)


SaveBTN.place(relx=0.5,rely=0.8,relwidth=0.6, relheight=0.08, anchor='center')
ClearBTN.place(relx=0.5,rely=0.9,relwidth=0.6, relheight=0.08, anchor='center')

AddBTN.place(relx=0.5,rely=0.4,relwidth=0.6, relheight=0.08, anchor='center')
EditBTN.place(relx=0.5,rely=0.5,relwidth=0.6, relheight=0.08, anchor='center')
DeleteBTN.place(relx=0.5,rely=0.6,relwidth=0.6, relheight=0.08, anchor='center')


# Main Frame
CheckList = Treeview(mainFrame, selectmode='browse')
CheckList.pack(fill='both', expand=True)
CheckList['columns'] = ("1")
CheckList['show'] = 'headings'
CheckList.column('1', anchor='w')
CheckList.heading('1', text='Tasks')

root.mainloop()