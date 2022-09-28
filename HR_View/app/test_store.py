from django.core.files import File
from models import test_store_files

def store_files(request):
    f=open('media/lafafa.dcox','w')
    store_file=File(f)
    tst=test_store_files(file=store_file)
    tst.save()

store_files()