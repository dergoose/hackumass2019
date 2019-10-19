from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess
import stat

num_max = -1
num_interval = -1

shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID = "spacelapse" #we change dis

clearCommand = ["--folder", "/store_00020001/DCIM/100CANON", \
                "-R", "--delete-all-files"]
triggerCommand = ["--trigger-capture"]
downloadCommand = ["--get-all-files"]

folder_name = "/" + shot_time + picID
save_location = "/media/pi/SANDISK 128/hackumassvii" + folder_name

def goodPrint(prin):
    print(datetime.now().strftime("%H:%M:%S") + " - " + prin)

#input desired photos and frequency of capture thru the terminal
def welcome():
    num_sec = input ("How long is your time lapse (seconds): ")
    num_int = input ("Enter how long your interval is (greater than 2): ")

    if int(num_sec) > 300:
        print("Invalid input")
        exit()

    num_pic = (int(num_sec) * 24) / int(num_int)

    global num_max
    num_max = int(num_pic)
    global num_interval
    num_interval = int(num_int)


    # if num_interval < 3 or num_max < 1:
    #     print("Invalid input")
    #     exit()

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

def createSaveFolder():
    print("was in: " + os.getcwd())
    os.chdir("/media/pi/SANDISK 128/hackumassvii/")
    print("now in: " + os.getcwd())

    os.chmod("/media/pi/SANDISK 128/hackumassvii/", stat.S_IRWXG )

    try:
        os.mkdir(folder_name, mode= 0o777)
    except Exception as e:
        print(e)
        exit()

    if not os.path.exists(save_location):
        print("Creation failure")
        exit()

    os.chdir(save_location)

def captureImages():
    gp(triggerCommand)
    goodPrint("took picture")
    sleep(num_interval)

def renameFiles():
    pictures = 1
    listPic = os.listdir(".")
    listPic.sort()
    for filename in listPic:
        # if len(filename) < 13:
            if filename.endswith(".JPG"):
                name = str(pictures)
                name = name.zfill(3)
                pictures += 1
                goodPrint("naming "+ filename +" to img" + name + ".JPG")
                os.rename(filename, ("img" + name + ".JPG"))
                goodPrint("renamed the jpg")

welcome()
killgphoto2Process()
gp(clearCommand)
createSaveFolder()

for i in range(num_max):
    captureImages()

gp(downloadCommand)
renameFiles()
gp(clearCommand)


bashCommand2 = "ffmpeg -start_number 001 -start_number_range " + str(num_max) + " -framerate 24 -i img%03d.JPG output.avi"


os.chdir(save_location)
print(os.getcwd())

process1 = subprocess.Popen("ls".split(), stdout=subprocess.PIPE)
output, error = process1.communicate()


process2 = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
output, error = process2.communicate()
