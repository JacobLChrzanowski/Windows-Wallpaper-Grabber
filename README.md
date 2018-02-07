# Windows-Wallpaper-Grabber
Grabs Windows 10 logon screen background files and lets you sort through for ones you like. This will eventually be automated.

This repo is NOT YET COMMENTED.

Get Wallpapers will grab files
C:\Users\<USERPATH>\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\
and move them to 
C:\Users\<USERPATH>\Desktop\images\

The python script is mostly reappropriated code from a stackoverflow post that happened to work perfectly for my use-case.
Credit goes to 'Fred the Fantastic'
https://stackoverflow.com/questions/8032642/how-to-obtain-image-size-using-standard-python-class-without-using-external-lib
It moves images from "\Desktop\\images\\" to directories in "\Desktop\\Wallpapers\\" named after the image's dimensions.


My goal is to convert this to a purely python scipt that will differentiate between images and non-images, saving the trouble
of manually sorting images from non-image.
