import os
from datetime import datetime
import shutil
from PIL import Image

class PhotoOrganizer:

    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']

    def create_folder_path(self, file):
        date = self.shooting_date(file)
        return date.strftime('%Y') + '/' + datetime.strftime('%Y:%m:%d')

    def shooting_date(self, file):
        photo = Image.open(file)
        info = photo._getexif()
        if 36867 in info:
            date = info[36867]
            date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        else:
            date = datetime.fromtimestamp(os.path.getmtime(file))
            
        return date


    def move_photo(self, file):
        new_folder = self.create_folder_path(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)
        
    def organize(self):
        photos = []
        files = os.listdir('.')
        for filename in files:
            for ext in self.extensions:
                if filename.endswith(ext):
                    photos.append(filename)
                       
        for filename in photos:
            self.move_photo(filename)
        
ORGANIZER = PhotoOrganizer()
ORGANIZER.organize()