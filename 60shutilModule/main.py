import shutil
import os

# shutil.copy("60shutilModule/main.py","60shutilModule/main2.py")  #used to copy and paste the whole data into another file
# shutil.copytree("60shutilModule/.tutorial", "60shutilModule/mytutorial")  #used to copy and paste the whole data into another folder with its file
# shutil.move("60shutilModule/.tutorial/file.file", "60shutilModule/file.file")  #used to move file from one folder to another
# shutil.rmtree( "mytutorial") #it is use to remove or delete the file or folder, it is not working due to some reasons so for that we can use "os module to remove anything"
os. remove("60shutilModule/file.file")  #used to delete the file