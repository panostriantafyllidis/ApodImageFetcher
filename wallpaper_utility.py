import ctypes

APOD_API_KEY = "yjdOU0OzXE53lNYoaWZQ6H5Fodjy8gJs4APnZW4r"
SERVICE_NAME = "NASA Wallpaper"

# constant to work with windows 
SPI_SETDESKWALLPAPER = 20
# changes the wallpaper of our system
def changeBG(path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)