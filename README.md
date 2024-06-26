# Nasa Apod

![Logo](https://github.com/panostrian/imageRepo/blob/main/apodLogo.jpg?raw=true)

### Features

- Automatically sets NASA Astronomical Picture of the Day as desktop wallpaper.
- Manually select a date from user friendly GUI and set that date's image as the desktop wallpaper.
- Saves the images in local user drive for future use.

## Run the Program

### Trial Run 
On the cmd, make sure the cloned repo is open.
Run:
```
python apod_wallpaper_setter.py
```
See if the wallpaper is changed.

### Create a batch file

Open nasa_apod_wallpaper_batch_file.bat
Change the *D:\PythonAuto\* in the file, to the location where you have cloned the repo and where *apod_wallpaper_setter.py* is accessible.

For Example: I had this file in D drive, in a folder named PythonAuto

Just double click the batch file to see if it updates your wallpaper.
Make sure you have the right path in the batchfile.

Note :
+ Make sure you've entered the correct path
+ Make sure you can access internet through python on your device.


### Manual Wallpaper Setter
In the command promt, with the cloned repo open in it, run:
```
python manual_wallpaper_changer.py
```

Select the date and click on "set as wallpaper".
You can select any date from 2008* to today.
*Need to change it to go all the way back to 2000s
Click on "Use Today's Pic" to use today's pic.

### Set Automatic Wallpaper changer
You can refer to [this](https://www.geeksforgeeks.org/schedule-a-python-script-to-run-daily/) article to setup automatic Wallpaper changer.

1. Make sure you have edited the batch file and it is working.
2. Go to Windows search bar and search "Task Scheduler".
3. Click on ‘Create Basic Task….’ in the Actions Tab. And give a suitable Name like "NASA APOD Auto WAllpaper", and Description of your task that you want to Automate and click on Next.
4. In the next step, you have to select at what time intervals your script should be executed. Select ‘Daily’ and click Next. Now you need to specify at what time your Python Script should be executed daily and then Click on Next. I reccommend using a time when your PC is most likely to be on and unlocked. For me, it was 2pm. For this test, I recommend choosing 10 mins after current time. Later you can edit this time.
5. Click on browse and find and select the batch file we had edited. Now click Next.
6. See if everything looks fine. Then click on finish.

### Note:

+ You are only allowed to make 30 API calls per hours. This is due to the demo key. You can bypass this by generating a real key from [here](https://api.nasa.gov/) and updating it in wallpaper_utility.py
+ Saved images are stored in "C:\Users\ [USERNAME]\Pictures\NasaApod"

## References:

+ NASA APOD : https://apod.nasa.gov/apod/

+ NASA APOD API: https://github.com/nasa/apod-api

