import os


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'files')
PDF_PATH = os.path.join(PROJECT_ROOT_PATH, 'files', 'duck.pdf')
TXT_PATH = os.path.join(PROJECT_ROOT_PATH, 'files', 'bar.txt')
XLS_PATH = os.path.join(PROJECT_ROOT_PATH, 'files', 'about tests runs.xls')
XLSX_PATH = os.path.join(PROJECT_ROOT_PATH, 'files', 'about tests.xlsx')
TMP_PATH_ROOT = os.path.split(PROJECT_ROOT_PATH)
TMP_PATH = os.path.join(TMP_PATH_ROOT[0], 'tmp')

