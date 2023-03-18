import os
import shutil
import subprocess
import tempfile
import getopt
import sys

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
wix_bin_path = "C:\\Program Files (x86)\\WiX Toolset v3.11\\bin\\"
argumentList = sys.argv[1:]
options = "hw:"
long_options = ["help", "wix_bin_path"]

# prints help text
def print_usage():
    print("\nUsage: \ncreate_installer_windows.py [options]")
    print("\nOptions:\n"
          "-h, --help         = Show help\n"
          "-w, --wix_bin_path = Explicity specify wix source path, default: C:\\Program Files (x86)\\WiX Toolset v3.11\\bin")

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--help"):
            print_usage()
            exit()
             
        elif currentArgument in ("-w", "--wix_bin_path"):
            wix_bin_path = sys.argv[0]

except getopt.error as err:
    print (str(err))
    print_usage()
    exit()

output_msi_file = "./dist/MatApp_Setup.msi"

# create a temp directory
temp_dir = tempfile.mkdtemp()

try:
    # compile release version of the app
    subprocess.check_call(["conan", "install", ".", "--output-folder=dist/build", "--build=missing", "--settings=build_type=Release"])
    subprocess.check_call(["cmake", ".", "-B", "dist/build", "-DCMAKE_TOOLCHAIN_FILE=dist/build/conan_toolchain.cmake"])
    subprocess.check_call(["cmake", "--build", "dist/build", "--config", "Release"])

    # compile wixobj
    object_file = os.path.join(temp_dir, "output.wixobj")
    candle_exe = os.path.join(wix_bin_path, "candle.exe")
    subprocess.check_call([candle_exe, "-o", object_file, "mat.wxs"])

    # link the object file into an MSI file
    light_exe = os.path.join(wix_bin_path, "light.exe")
    subprocess.check_call([light_exe, "-out", output_msi_file, object_file])

    print(bcolors.OKGREEN + "Installer created successfully: %s" % output_msi_file + bcolors.ENDC)

except subprocess.CalledProcessError as e:
    print("Error building installer: %s" % e)

finally:
    # clean up the temp directory
    shutil.rmtree(temp_dir)