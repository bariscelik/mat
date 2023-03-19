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
    

# source files
executable_path = './build/mat'
dylib_path = './build/lib/libcgcustommath.dylib'

# Define the DMG settings
app_name = 'MyApp'
app_version = '1.0'
dmg_title = f'{app_name} {app_version}'
dmg_filename = f'{app_name}-{app_version}.dmg'
dmg_size = '50m'


try:
    # compile release version of the app
    subprocess.check_call(["conan", "install", ".", "--output-folder=dist/build", "--build=missing", "--settings=build_type=Release"])
    subprocess.check_call(["cmake", ".", "-G", "Xcode", "-B", "dist/build", "-DCMAKE_TOOLCHAIN_FILE=dist/build/conan_toolchain.cmake", "-DCMAKE_BUILD_TYPE=Release"])
    subprocess.check_call(["cmake", "--build", "dist/build", "--config", "Release"])

    subprocess.check_call(["hdiutil", "create", "-volname", "MatApp Install", "-srcfolder", "./dist/build/Release/mat.app", "-ov", "-format", "UDZO", "./dist/matapp.dmg"])

    print(bcolors.OKGREEN + "Installer created successfully: ./dist/matapp.dmg" + bcolors.ENDC)

except subprocess.CalledProcessError as e:
    print("Error building installer: %s" % e)

