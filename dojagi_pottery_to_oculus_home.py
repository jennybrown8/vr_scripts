import sys, os
import glob
import subprocess

# Python script that copies the Dojagi OBJ pottery exports over to
# Oculus Home directory, converting the file format on the way over.
#
# Written April 2019 with obj2gltf https://github.com/AnalyticalGraphicsInc/obj2gltf already installed.
#

USER="jenny"
DOJAGI_DIR="""/Users/{}/Documents/DOJAGI/Exports""".format(USER)
OCULUS_DIR="""/Users/{}/Documents/Oculus Home/_Import""".format(USER)


# Get a list of potteries to convert and copy - absolute paths
# glob produces the super ugly /a/b/c\\d.obj style file path.
sourcefiles = glob.glob(DOJAGI_DIR + "/Pottery*.obj")
sourcefilenames = [f.replace(DOJAGI_DIR, '').replace('\\','') for f in sourcefiles]

# Get a list of potteries already copied
destfiles = glob.glob(OCULUS_DIR + "/Pottery*.glb")
destfilenames = [f.replace(OCULUS_DIR, '').replace('\\','') for f in destfiles]

# Eliminate the already-done ones from the source list, for speed.
sources = [f for f in sourcefilenames if f.replace('obj', 'glb') not in destfilenames]
#print("Going to export these new files from Dojagi to Oculus Home: \n" + str(sources))


# For each new pottery, convert and copy in one step
os.chdir(DOJAGI_DIR)
for pottery in sources:
    #cmd=["obj2gltf", "--binary", "--specularGlossiness", "-i", pottery, "-o", 
    cmd=["obj2gltf", "--binary", "-i", pottery, "-o", 
            "{}\\{}".format(OCULUS_DIR.replace("/", """\\"""), pottery.replace('obj', 'glb'))]
    print(cmd)
    print(subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, cwd=DOJAGI_DIR).stdout.decode('utf-8'))

if not sources:
    print("No files to copy - already up to date.")
