import os.path, shutil, pytest, csv
from zipfile import ZipFile
from pypdf import PdfReader
from openpyxl import load_workbook

@pytest.fixture
def folders():
    if not os.path.exists('resources'):
        os.mkdir('resources')
    if not os.path.exists('tmp'):
        os.mkdir('tmp')

@pytest.fixture
def archiving():
    if not os.path.exists('resources/test_archive.zip'):
        shutil.make_archive('test_archive', 'zip', 'tmp')
        shutil.move('test_archive.zip', 'resources/test_archive.zip')


def test_csv(folders, archiving):
    with ZipFile('resources/test_archive.zip') as zip_file:
        file = zip_file.read('ubuntu.csv')

def test_pdf(folders, archiving):
    with ZipFile('resources/test_archive.zip') as zip_file:
        file = zip_file.read('Storytelling.pdf')
