import PyPDF2
import streamlit as st
import base64


st.title("PDF Locker")
st.header("Lock your pdf's safely with a password")
st.subheader("Upload pdf")
pdf=st.file_uploader("",type=["pdf"])
password = st.text_input("Enter Password",type="password")
confrmPassword = st.text_input("Re enter your Password",type="password")
if st.button("Submit"):
    if pdf is not None:
        pdfFileName=pdf.name.split(".")[0]
        if password==confrmPassword:
            pdf_file = pdf
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            pdf_writer = PyPDF2.PdfFileWriter()
            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
            pdf_writer.encrypt(password)
            
            
            result_pdf = open('Lockedfile.pdf','wb')  # create a pdf file and make it in wb mode
            
            pdf_writer.write(result_pdf)
            result_pdf.close()
            
            

            

        else:
            st.error("Please re-enter your password")
            password=st.empty()
            confrmPassword=st.empty()
    else:
        st.error("please upload pdf")
