## mat
This is a subdirectory CMake project that consists of a simple example library with a function and an executable linked to that library which invokes the function of the library.

### Requirements
#### Windows
Please use "command prompt" while following next steps
1. Install `chocolatey` by following https://chocolatey.org/install
1. Install CMake 
   ```
   choco install cmake
   ```
1. Install Python
   ```
   choco install python
   ```
1. Install conan 2.x 
   ```
   choco install conan
   ```
1. If you have Visual Studio 2022 (C++ Build Tools should be installed), please skip this step. To install Visual Studio 2022 Build  Tools using choco:
   ```
   choco install visualstudio2022buildtools
   ```
1. Create a default profile if you haven't got:
   ```
   conan profile detect --force
   ```

### Build and Run

1. Install dependencies using conan:
   ```
   conan install . --output-folder=build --build=missing --settings=build_type=Debug
   ```
1. Run CMake to configure project: (Replace "Visual Studio 17 2022" if you use another version of build tools, you can get a list of them using ```cmake```)
   ```
   cd build
   cmake .. -G "Visual Studio 17 2022" -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake
   ```
1. Build project:
   ```
   cmake --build . --config Debug
   ```

You can open the root folder using **Visual Studio**. But you should select "Debug" as Startup Item in the dropdown.

### Build Installer

```
python create_installer_windows.py

# set the wix bin/ path if the installed WiX isn't in the default path
python create_installer_windows.py # --wix_bin_path="<WIX_BIN_PATH>"
```