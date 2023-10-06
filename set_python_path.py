import sys

# Add the directory you want to include in the Python path
directory_to_include = "D:\HSC_RPA_POC\"
sys.path.append(directory_to_include)

# Now you can import modules from the specified directory
#import your_module
# set PYTHONPATH=D:\HSC_RPA_POC;%PYTHONPATH%
# set PYTHONPATH=C:\Users\satya\AppData\Local\Programs\Python\Python311\Lib\site-packages;%PYTHONPATH%

python -m robot.libdoc robotframework-imaplibrary2 robotframework-imaplibrary2.libspec