# Introduction

A simple python script that requests a dir then sorts all files into folders based on date. Attempts to weed out duplicates. 

## How It Works

###

#### Run Script

Run the sort-files-by-date Python3 script in a terminal.

#### Initialization

User is prompted (via dialog box) for the directory the sorting should begin in. If the directory is valid, the program initializes sorting (sortDir).

#### def sortDir

Loops through each entry in the user-provided dir. If it is a directory, it goes into it. If it is a file, it executes def sortFile() on it.

#### def sortFile

Attempts to get the created and modified datetimes for the file. Will use the older datetime for sorting.

Next, the destination directory is determined (ie {user-directory}/SORTED/yyyy/mm where yyyy is the older datetime year and mm is the older datetime month.) 

If a file with the same name already exists in the directory, the destination directory is changed to {user-directory}/SORTED/DUPLICATES/yyyy/mm.

If a file with the same name already exists in the duplicates directory, the filename has the current datetime appended to it, in order to prevent accidental deletion of old images (ie, images with partial datetime metadata and the same time could be mistakenly considered the same image).

Finally, the file is actually moved to the destination. If it fails, the CLI prints a message stating that the file failed to move.

#### Once Sorted

Once all of the files are sorted, the CLI prints a messaged stating the sort has been completed.

## Contributions

This project is currently considered completed. However, I will still review pull requests if you strongly belive a feature should be added. Any features requested should be very simple in nature as to fit with the purpose of this script.
