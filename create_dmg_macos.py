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

# create a temp directory
temp_dir = tempfile.mkdtemp()

build_dir = os.path.join(temp_dir, "build")

# payload directory for pkg installer
payload_dir = os.path.join(temp_dir, "payload")

try:
    # create required paths
    if not os.path.exists("./dist"):
        os.makedirs("./dist")
    
    os.makedirs(payload_dir)
    os.makedirs("%s/Applications/" % payload_dir);
    os.makedirs("%s/Library/Frameworks/" % payload_dir);
    os.makedirs("%s/pkg/" % temp_dir);

    # compile release version of the app
    subprocess.check_call(["conan", "install", ".", "--output-folder=%s" % build_dir, "--build=missing", "--settings=build_type=Release"])
    subprocess.check_call(["cmake", ".", "-G", "Xcode", "-B", build_dir, "-DCMAKE_TOOLCHAIN_FILE=%s/conan_toolchain.cmake" % build_dir, "-DCMAKE_BUILD_TYPE=Release"])
    subprocess.check_call(["cmake", "--build", build_dir, "--config", "Release"])
    
    # copy app and framework
    subprocess.check_call(["cp", "-rf", "%s/Release/mat.app" % build_dir, "%s/Applications/" % payload_dir])
    subprocess.check_call(["cp", "-rf", "%s/lib/Release/" % build_dir, "%s/Library/Frameworks/" % payload_dir])
    
    # build the .pkg installer
    subprocess.check_call(["pkgbuild", "--root", payload_dir, "--identifier", "com.baris.mat", "--component-plist", "matapp_component.plist", "%s/pkg/matapp.pkg" % temp_dir])
    
    # add .pkg into the .dmg
    subprocess.check_call(["hdiutil", "create", "-volname", "MatApp Install", "-srcfolder", "%s/pkg/" % temp_dir, "-ov", "-format", "UDZO", "./dist/matapp.dmg"])

    print(bcolors.OKGREEN + "Installer created successfully: ./dist/matapp.dmg" + bcolors.ENDC)

except subprocess.CalledProcessError as e:
    print("Error building installer: %s" % e)

finally:
    # clean up the temp directory
    shutil.rmtree(temp_dir)