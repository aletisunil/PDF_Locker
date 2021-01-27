import tkinter as tk
from tkinter import messagebox
import PyPDF2
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title("PDF Locker")

canvas =  tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3)

#logo
logo = Image.open('./logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1,row=0)

#instructions
instructions=tk.Label(root,text="Enter a password and select a pdf to encrypt\n")
instructions.grid(columnspan=3,column=0,row=1)

#password input
password=tk.Entry(root,show="*",width=15)
password.grid(column=1,row=2)

def open_file():
    file=askopenfile(parent=root,mode="rb",title="choose a file",filetypes=[("PDF Files"," *.pdf")])
    FileName=file.name.split(".")[0]
    if file is not None:
        print(password.get())
        print("file selected")
        pdf_file = file
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        pdf_writer.encrypt(password.get())
        encryptedFile=FileName+"_Encrypted.pdf"
        result_pdf = open(encryptedFile,'wb')  
            
        pdf_writer.write(result_pdf)
        result_pdf.close()
        password.delete(0, 'end')
        #root.withdraw()
        messagebox.showinfo("Success","File encrypted successfully")
    else:
        print("failed")



browse_btn=tk.Button(root,text="Browse file",command=lambda:open_file(),width="15",height="2")
browse_btn.grid(column=1,row=4)

canvas=tk.Canvas(root,width=600,height=250)
canvas.grid(columnspan=3)



root.mainloop()
