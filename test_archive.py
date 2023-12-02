import os.path, shutil, pytest

from script_os import TMP_DIR
from zipfile import ZipFile

@pytest.fixture
def folders():
    if not os.path.exists('resources'):
        os.mkdir('resources')
    if not os.path.exists('tmp'):
        os.mkdir('tmp')

def test_archive(folders):
    with ZipFile('tmp/test_archive.zip', 'w') as zip_file:
        zip_file.write('tmp/Storytelling.pdf')
        zip_file.write('tmp/ubuntu.csv')
        zip_file.write('tmp/clinics.xlsx')

    shutil.move('tmp/test_archive.zip', 'resources/test_archive.zip')

    with ZipFile('resources/test_archive.zip'):
        zip_file.