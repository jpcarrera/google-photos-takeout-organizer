import os
import re

from random import randrange
import shutil

# the 'Google Photos' folder, used as input to this script
input_dir = '/Users/juan.carrera/Downloads/Takeout/GooglePhotos'

# the output directory, where all files will be written to
output_dir = '/Users/juan.carrera/Downloads/GooglePhotos'

photo_extensions = [
    '.jpg', '.jpeg', '.jpe', '.jfif', '.bmp', '.dib', '.gif',
    '.png', '.tif', '.tiff', '.heic', '.mp4', '.avi', '.wmv',
    '.flv',
]

video_extensions = [
    '.mp4', '.m4a', '.m4p', '.m4v', '.f4v', '.f4a', '.m4b', '.m4r', '.f4b',
    '.mov', '.3gp', '.3gp2', '.3g2', '.3gpp', '.3gpp2', '.ogg', '.oga', '.ogv',
    '.ogx', '.wmv', '.wma', '.asf', '.webm', '.flv', '.avi', '.gif', '.qt',
    '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.m2v'
]

for f in os.listdir(input_dir):
    subdir_path = os.path.join(input_dir, f)
    if not os.path.isdir(subdir_path):
        continue
    subdir_files = os.listdir(subdir_path)
    print('[status] processing directory: '
        + f
        + ' with '
        + str(len(subdir_files))
        + ' files.'
    )
    for filename in subdir_files:
        source_filepath = os.path.join(subdir_path, filename)
        
        root, ext = os.path.splitext(filename)
        ext = ext.lower()
        if ext not in photo_extensions \
                and ext not in video_extensions:
            continue
        try:
            path_list = source_filepath.split('/')
            subfolder = path_list[len(path_list) - 2 ]
            new_filename_without_ext = subfolder + '_' + root
            
            output_dire = output_dir
            
            r = re.compile('.{4}-.{2}-.{2}.*')
            if r.match(subfolder):
                date_array = subfolder.split('-')
                year_month = date_array[0] + '-' + date_array[1]
                output_dire = output_dir + '/' + year_month
            new_filepath_no_ext = os.path.join(output_dire, new_filename_without_ext + '_' + str(randrange(10)))
            new_filepath = new_filepath_no_ext + ext
            
            # create directory if it doesn't exist
            print('Copying ' + filename + ' to ' + new_filepath)
            if not os.path.exists(output_dire):
                os.mkdir(output_dire)
            
            # copy file
            shutil.copyfile(source_filepath, new_filepath)
        except:
            raise
