import csv, os, mmap
from summaryDashboard.models import College
from tqdm import tqdm

def run():
    file_path = './static/csv/world-universities.csv'
    file_size = os.path.getsize(file_path)
    College.objects.all().delete()
    
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=',')
        for row in tqdm(reader, total=get_num_lines(file_path)):
            obj, created = College.objects.get_or_create(code = row[0], name = row[1], link = row[2])

def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines