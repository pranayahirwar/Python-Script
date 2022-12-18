import os
import extension as ex

# Set the directory where the files are located
# directory = "C:\\Users\\XYZ\\Desktop\\Download"
directory = os.getcwd()
# print(directory)

# Get a list of all the files in the directory
files = os.listdir(directory)
# print(files)
missed_extCount = 0

for file in files:

    # Get the file extension
    extension = file.split('.')[-1]
    extension = '.' + extension

    # Check if the extension is in the list of known file types
    if extension in ex.extension_paths:
        # If the extension is in the list of known file types,
        # create a new directory for that file type if it doesn't already exist

        if not os.path.exists(os.path.join(directory, ex.extension_paths[extension])):
            os.makedirs(os.path.join(directory, ex.extension_paths[extension]))

        # Move the file to the appropriate directory
        os.rename(os.path.join(directory, file), os.path.join(directory, ex.extension_paths[extension], file))
    else:
        missed_extCount += 1

print('Special Extension Encountered')
print(f'All file moved, Except {missed_extCount} files.')

