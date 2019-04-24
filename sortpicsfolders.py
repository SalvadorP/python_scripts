# https://stackoverflow.com/questions/47594644/create-folder-based-on-date
# https://stackoverflow.com/questions/34411061/python-create-directory-structure-based-on-the-date
# https://github.com/ivandokov/phockup/blob/master/phockup.py

# Iterate recursively the files of each origin folder
# Put the files in the destination folder structure sorted by date
# year/yyyy-mm-dd/files.*


import glob
import exifread
import os
from shutil import copyfile

for file in glob.iglob('originals/**/*.jpg', recursive=True):
    tmp_file = open(file, 'rb')
    tags = exifread.process_file(tmp_file)
    file_date = str(tags['Image DateTime']).split()
    date_chunks = file_date[0].split(':')
    # 0 year // 1 month // 2 day
    print(date_chunks)
    year = date_chunks[0]
    month_day = date_chunks[1] + '-' + date_chunks[2]
    path = './sorted/' + year + '/' + month_day
    try:
        os.mkdir(path)
    except OSError:  
        print ("Directory %s exists" % path)
    else:  
        print ("Successfully created the directory %s " % path)
    filename = file.split('/')
    filename = filename[len(filename)-1]
    dst_path = path + '/' + filename
    try:
        copyfile(file, dst_path)
    except OSError:
        print ("Error copying file %s " % dst_path)
    else:
        print ("File copied %s " % dst_path)
    
        
