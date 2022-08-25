#Automation
from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from distutils.command.build_ext import extension_name_re
import shutil
path="D:\My Photos\April-22"
# #go inside path
os.chdir(path)
#list files inside path
def list_file_extentions():
    extentions=[]
    for file in os.listdir('.'):
        filename, file_extension = os.path.splitext(file)
        #print(filename,'     ',file_extension)
        if file_extension not in extentions:
            extentions.append(file_extension)
    print(extentions)
    

#     if file_extension not in extentions:
#         extentions.append(file_extension)
# print(extentions)
#['.jpg', '.mp4', '.PNG', '.JPG', '.jpeg']
def moving_files():
    folders=['images','videos']
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)

    for file in os.listdir('.'):
        filename, file_extension = os.path.splitext(file)
        if file_extension in ['.jpg', '.PNG', '.JPG', '.jpeg','.png']:
            shutil.move(file,'images')
            print(f'moving: {file}')

        elif file_extension in['.mp4','.webm']:
            shutil.move(file,'videos')
            print(f'moving: {file}')
   
#list_file_extentions()
moving_files()   

   
        