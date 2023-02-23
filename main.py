import tempfile
from PIL import Image
import PyPDF2
import streamlit as st
import pandas as pd
from functionforDownloadButtons import download_button
from pdf2image import convert_from_path
import pytesseract
from PyPDF2 import PdfFileReader, PdfFileWriter
import base64
import tempfile
from pathlib import Path
from transformers import pipeline
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_icon="✂️", page_title="Logo or Not Logo")


c2, c3 = st.columns([6, 1])


with c2:
    c31, c32 = st.columns([12, 2])
    with c31:
        st.caption("")
        st.title("Logo or Not Logo")
    with c32:
        st.image(
            "images/logo.png",
            width=200,
        )


def show_pdf(file_path:str):
    """Show the PDF in Streamlit
    That returns as html component

    Parameters
    ----------
    file_path : [str]
        Uploaded PDF file path
    """

    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

    st.title("PDF file uplodaer")
    uploaded_file = st.file_uploader("Choose your .pdf file", type="pdf")

    if uploaded_file is not None:
        # Make temp file path from uploaded file
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            st.markdown("## Original PDF file")
            fp = Path(tmp_file.name)
            fp.write_bytes(uploaded_file.getvalue())
            st.write(show_pdf(tmp_file.name))

            imgs = convert_from_path(tmp_file.name)

            st.markdown(f"Converted images from PDF")
            st.image(imgs)

        st.stop()

    def pdf_checker(question_):
        nlp = pipeline(
            "document-question-answering",
            model="impira/layoutlm-document-qa",
        )

    '''result = nlp(
        "page.jpg",
        question_
    )
    return (result)

form = st.form(key="annotation")
with form:
    question_ = st.text_input()

    submitted = st.form_submit_button(label="Submit")


if submitted:

    answer = pdf_checker(question_)


c29, c30, c31 = st.columns([1, 1, 2])

with c29:
    st.write(answer)'''
