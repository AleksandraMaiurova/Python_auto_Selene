from zipfile import ZipFile
import os
from utils import XLSX_PATH, XLS_PATH, TXT_PATH, PDF_PATH


def test_we_have_pdf(archive_maker):
    pdf_size_real = os.path.getsize(PDF_PATH)
    pdf_name_real = os.path.basename(PDF_PATH)
    with ZipFile(file='tmp/archive.zip', mode='a') as z:
        z.write(filename=PDF_PATH, arcname='duck.pdf')
    with ZipFile(file='tmp/archive.zip', mode='r') as z:
        pdf_info = z.getinfo('duck.pdf')
        pdf_name = pdf_info.filename
        pdf_size = pdf_info.file_size
        assert pdf_name == pdf_name_real
        assert pdf_size == pdf_size_real

def test_we_have_txt(archive_maker):
    txt_size_real = os.path.getsize(TXT_PATH)
    txt_name_real = os.path.basename(TXT_PATH)
    with ZipFile(file='tmp/archive.zip', mode='a') as z:
        z.write(filename=TXT_PATH, arcname='bar.txt')
    with ZipFile(file='tmp/archive.zip', mode='r') as z:
        txt_info = z.getinfo('bar.txt')
        txt_name = txt_info.filename
        txt_size = txt_info.file_size
        with z.open('bar.txt') as txt:
            assert 'Тестировщик' in txt.read().decode('utf-8')
    assert txt_name == txt_name_real
    assert txt_size == txt_size_real



def test_we_have_xlsx(archive_maker):
    xlsx_size_real = os.path.getsize(XLSX_PATH)
    xlsx_name_real = os.path.basename(XLSX_PATH)
    with ZipFile(file='tmp/archive.zip', mode='a') as z:
        z.write(filename=XLSX_PATH, arcname='about tests.xlsx')
    with ZipFile(file='tmp/archive.zip', mode='r') as z:
        xlsx_info = z.getinfo('about tests.xlsx')
        xlsx_name = xlsx_info.filename
        xlsx_size = xlsx_info.file_size
    assert xlsx_name == xlsx_name_real
    assert xlsx_size == xlsx_size_real

def test_we_have_xls(archive_maker):
    xls_size_real = os.path.getsize(XLS_PATH)
    xls_name_real = os.path.basename(XLS_PATH)
    with ZipFile(file='tmp/archive.zip', mode='a') as z:
        z.write(filename=XLS_PATH, arcname='about tests runs.xls')
    with ZipFile(file='tmp/archive.zip', mode='r') as z:
        xls_info = z.getinfo('about tests runs.xls')
        xls_name = xls_info.filename
        xls_size = xls_info.file_size
    assert xls_name == xls_name_real
    assert xls_size == xls_size_real




