import csv, os
from summaryDashboard.models import College
from tqdm import tqdm

def run():
    file_path = './static/csv/world-universities.csv'
    file_size = os.path.getsize(file_path)
    College.objects.all().delete()
    
    with open(file_path) as f:
        read_size = 0
        with tqdm(total=file_size) as pbar:
            for row in f:
                obj, created = College.objects.get_or_create(code = row[0], name = row[1], link = row[2])
                read_size += len(row.encode('utf-8'))
                pbar.update(read_size)