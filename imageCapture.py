from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

num_shot = 0
num_max = -1
num_interval = -1

def welcome():
    num_pic = input ("Enter how many photos you'd like to take: ") 
    num_int = input ("Enter how long your interval is (greater than 3): ") 
    if num_int < 3:
        print("Invalid interval")
        exit()
    global num_max
    num_max = int(num_pic)
    global num_interval
    num_interval = int(num_int)
    
#kill gphoto2 process that starts whenever we connect the camera
def killgphoto2Process():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    
    #search for the line that has the process we want to kill
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            #kill the process
            pid = int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)

shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID = "spacelapse" #we change dis

clearCommand = ["--folder", "/store_00020001/DCIM/100CANON", \
                "-R", "--delete-all-files"]
triggerCommand = ["--trigger-capture"]
downloadCommand = ["--get-all-files"]

folder_name = shot_date + picID
save_location = "/home/pi/Desktop/gphoto/images" + folder_name

def createSaveFolder():
    try:
        os.makedirs(save_location)
    except:
        print("Failed to create the new directory.")
    os.chdir(save_location)
    
def captureImages():
    if(num_max < 0 or num_interval < 0):
        print("Something has gone terribly wrong")
        exit()
    for i in range(num_max):
        gp(triggerCommand)
        global num_shot
        num_shot += 1
        sleep(num_interval)
        gp(downloadCommand)
        gp(clearCommand)
    
def renameFiles(ID):
    name = str(num_shot)
    name.zfill(3)
    for filename in os.listdir("."):
        if len(filename) < 13:
            if filename.endswith(".JPG"):
                os.rename(filename, ("img" + name + ".JPG"))
                print("renamed the jpg")
            #elif filename.endswith(".CR2"):
                #os.rename(filename, (shot_time + ID + ".CR2"))
                #print("renamed the cr2")
                
welcome()
killgphoto2Process()
gp(clearCommand)
createSaveFolder()
captureImages()
renameFiles(picID)

                          