from datetime import datetime
import os
import shutil
import tkinter as tk
from tkinter import filedialog

# hidden root window
root = tk.Tk()
root.withdraw()

# get dir that needs to be sorted
init_dir = '/home'
directory = filedialog.askdirectory(title="Select Directory To Sort", initialdir=init_dir)



# go into dir and sub-dirs... call sortFile when appropriate
def sortDir(dir):
    for entry in os.listdir(dir):
        full_path = os.path.join(dir, entry)

        # go into sub-dir to sort its files
        if os.path.isdir(full_path):
            #print(full_path)
            sortDir(full_path)

        # sort the file
        if os.path.isfile(full_path):
            sortFile(full_path, os.path.splitext(os.path.basename(full_path))[0], os.path.splitext(full_path)[1])



#sort the file into /sorted/yyyy/mm
# filepath = full path include name and extension, filename only (no extension), extension only
def sortFile(full_origin_path, filename, extension):
    # get date file was created and date it was modified
    try: created_datetime = os.path.getctime(full_origin_path)
    except: created_datetime = datetime.now()
    
    try: modified_datetime = os.path.getmtime(full_origin_path)
    except: modified_datetime = datetime.now()

    # use the older of the two datetimes for sorting
    useDateMode = 'modified' if (created_datetime > modified_datetime or created_datetime == modified_datetime) else 'created'


    if useDateMode == 'modified':
        fileYear = datetime.fromtimestamp(modified_datetime).strftime('%Y')
        fileMonth = datetime.fromtimestamp(modified_datetime).strftime('%m')

    if (useDateMode == 'created'):
        fileYear = datetime.fromtimestamp(created_datetime).strftime('%Y')
        fileMonth = datetime.fromtimestamp(created_datetime).strftime('%m')

    if useDateMode == None:
        fileYear = datetime.now().strftime('%Y')
        fileMonth = datetime.now().strftime('%m')


    # make sure the destination directory exists
    destdir = f'{str(directory)}/SORTED/{fileYear}/{fileMonth}'
    if not os.path.exists(destdir): os.makedirs(destdir)
    
    # if the file already exists in the destination, change destination to duplicates
    if os.path.exists(f'{destdir}/{filename}{extension}'):
        destdir = f'{str(directory)}/SORTED/DUPLICATES/{fileYear}/{fileMonth}'
        if not os.path.exists(destdir): os.makedirs(destdir)
        #print('detected duplicate')

    # if the file already exists in the duplicates destination, change the filename to have current datetime on it
    if os.path.exists(f'{destdir}/{filename}{extension}'):
        filename = f'{filename}_{datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}'
        # print('detected duplicate in duplicates')

    full_dest_path = f'{destdir}/{filename}{extension}'
    try:
        shutil.move(full_origin_path, full_dest_path)
        # print(f'moved {filename}{extension} to {full_dest_path}\n')
    except:
        print(f'failed to move {filename}{extension} to {full_dest_path}\n')







# okay to sort... go!
if directory:
    # creat destination "sorted" folder
    if not os.path.exists(str(directory) + '/SORTED'):
        os.makedirs(str(directory) + '/SORTED')

    print(f'Start in {directory}\n')
    sortDir(directory)  # initialize the interations
    print('COMPLETED SORT!')
else:
    print('User did not select a directory to sort, or selected an invalid directory.')
