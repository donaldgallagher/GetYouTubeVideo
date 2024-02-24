import subprocess
import sys
import importlib.util
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def check_update_pip():
    try:
        # Run 'pip list --outdated' to check for outdated packages including pip
        result = subprocess.run([sys.executable, "-m", "pip", "list", "--outdated"], capture_output=True, text=True)
        
        # Check if 'pip' is in the list of outdated packages
        if "pip" in result.stdout:
          # There is an update available for pip
            try:
                print('Checking for pip updates...')
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade','pip'])
                print("pip has been updated.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to update pip: {e}")
        #else:
         #   print(False)  # Pip is up to date
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to check for pip updates: {e}")
        # Optionally, return or print False here, since the check couldn't be performed


def update_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("pip has been updated.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update pip automatically: {e}")
        print("Please update pip manually using 'python -m pip install --upgrade pip'")

def check_and_install_package(package_name):
    if importlib.util.find_spec(package_name) is None:
        print(f"{package_name} is not installed. Installing now...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', package_name])
            print(f"{package_name} has been successfully installed.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package_name}: {e}")
   # else:
        #print(f"{package_name} is already installed.")


if __name__ == "__main__":
    check_update_pip()  # Update pip before checking for other packages

    # Define 'package_name' before using it
    package_name = "pytube"
    check_and_install_package(package_name)
    
    # Assuming pytube is now installed and available
    try:
        from pytube import YouTube
        # Prompt user for the YouTube URL
        url = input("Enter a YouTube URL to download: ")
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if stream:
            print(f"Downloading video: {yt.title}")
            stream.download()
            print("Download completed.")
        else:
            print("No suitable stream found.")
    except Exception as e:
        print(f"An error occurred: {e}")
