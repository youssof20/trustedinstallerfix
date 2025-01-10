import os
import subprocess
import ctypes
import sys

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def take_ownership(folder_path):
    """Take ownership of the folder using the 'takeown' command."""
    try:
        subprocess.run(['takeown', '/F', folder_path, '/R', '/D', 'Y'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Ownership taken for {folder_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to take ownership: {e.stderr.decode().strip()}")

def remove_trustedinstaller(folder_path):
    """Remove TrustedInstaller as the owner and set the current user as the owner."""
    try:
        # Remove TrustedInstaller from the ACL
        subprocess.run(['icacls', folder_path, '/remove', 'NT SERVICE\\TrustedInstaller', '/T', '/C'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Removed TrustedInstaller from {folder_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to remove TrustedInstaller: {e.stderr.decode().strip()}")

def grant_full_control(folder_path):
    """Grant full control to the current user using the 'icacls' command."""
    try:
        subprocess.run(['icacls', folder_path, '/grant', '*S-1-3-4:F', '/T', '/C'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Full control granted for {folder_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to grant full control: {e.stderr.decode().strip()}")

def fix_permissions(folder_path):
    """Fix permissions for the specified folder."""
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    print(f"\nFixing permissions for {folder_path}...")
    take_ownership(folder_path)
    remove_trustedinstaller(folder_path)
    grant_full_control(folder_path)

def search_folders(root_dir, folder_name):
    """Search for folders with a specific name within a root directory."""
    matching_folders = []
    try:
        for root, dirs, files in os.walk(root_dir):
            if folder_name in dirs:
                matching_folders.append(os.path.join(root, folder_name))
    except PermissionError as e:
        print(f"Permission denied while searching in {root_dir}: {e}")
    except Exception as e:
        print(f"An error occurred while searching: {e}")
    return matching_folders

def main():
    if not is_admin():
        print("This script requires administrative privileges. Please run it as an administrator.")
        sys.exit(1)

    # Specify the folder name to search for
    folder_name_to_search = "WindowsApps"  # Change this to the folder name you want to search for
    root_directory = "C:\\"  # Change this to the root directory where you want to start the search

    print(f"Searching for folders named '{folder_name_to_search}' in '{root_directory}'...")
    matching_folders = search_folders(root_directory, folder_name_to_search)

    if not matching_folders:
        print(f"No folders named '{folder_name_to_search}' were found.")
        return

    print(f"Found {len(matching_folders)} folder(s):")
    for folder in matching_folders:
        print(f" - {folder}")

    # Fix permissions for each matching folder
    for folder in matching_folders:
        fix_permissions(folder)

    print("\nPermissions fixed successfully for all matching folders.")

if __name__ == "__main__":
    main()
