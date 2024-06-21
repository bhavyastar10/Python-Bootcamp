import os        # for os path related functions
import shutil    # for copy of files

# finding current file location
current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(current_dir):

    # for Image folder creation
    if filename.endswith(('.jpg', '.png', '.gif')):
        if not os.path.exists("Images"): 
            os.makedirs('Images')
        shutil.copy(filename, 'Images')
        os.remove(filename)
        print('Images folder done')

    # for Document folder creation
    if filename.endswith(('.pdf', '.docx')):
        if not os.path.exists("Documents"): 
            os.makedirs('Documents')
        shutil.copy(filename, 'Documents')
        os.remove(filename)
        print('Documents folder done')

    # for Apps folder creation
    if filename.endswith(('.apk', '.exe')):
        if not os.path.exists("Apps"): 
            os.makedirs('Apps')
        shutil.copy(filename, 'Apps')
        os.remove(filename)
        print('Apps folder done')

    # for Videos folder creation
    if filename.endswith(('.mp4', '.wmv')):
        if not os.path.exists("Videos"): 
            os.makedirs('Videos')
        shutil.copy(filename, 'Videos')
        os.remove(filename)
        print('Videos folder done')

print('all done')