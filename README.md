# Fix TrustedInstaller Permissions Script

This Python script is designed to help users resolve the **"You Require Permission From TrustedInstaller"** error on Windows. It automates the process of taking ownership of protected folders (e.g., `WindowsApps`), removing `TrustedInstaller` as the owner, and granting full control to the current user.

## Features
- **Search Functionality:** Dynamically searches for folders by name (e.g., `WindowsApps`) within a specified root directory.
- **Permission Fixing:**
  - Takes ownership of the folder using the `takeown` command.
  - Removes `TrustedInstaller` as the owner using the `icacls` command.
  - Grants full control to the current user using the `icacls` command.
- **Error Handling:** Includes robust error handling to ensure the script runs smoothly and provides meaningful feedback.
- **Administrative Privileges:** Ensures the script is run with administrative privileges to modify system folders.

## Prerequisites
- **Python 3.x:** The script requires Python 3.x to run. Download and install Python from [python.org](https://www.python.org/).
- **Windows OS:** This script is designed for Windows operating systems.

## Usage

### 1. Download the Script
- Download the script file (`fix_trustedinstaller_permissions.py`) to your computer.

### 2. Run the Script as Administrator
- Right-click on the script file and select **"Run as administrator"**.

### 3. Modify Search Parameters (Optional)
- Open the script in a text editor or IDE.
- Modify the following variables if needed:
  - `folder_name_to_search`: The name of the folder you want to search for (e.g., `WindowsApps`).
  - `root_directory`: The root directory where the search will begin (e.g., `C:\`).

### 4. Execute the Script
- The script will:
  1. Search for folders matching the specified name.
  2. List all matching folders.
  3. Fix permissions for each matching folder.

### Example Output
```
Searching for folders named 'WindowsApps' in 'C:\'...
Found 2 folder(s):
 - C:\Program Files\WindowsApps
 - C:\Program Files (x86)\WindowsApps

Fixing permissions for C:\Program Files\WindowsApps...
Ownership taken for C:\Program Files\WindowsApps
Removed TrustedInstaller from C:\Program Files\WindowsApps
Full control granted for C:\Program Files\WindowsApps

Fixing permissions for C:\Program Files (x86)\WindowsApps...
Ownership taken for C:\Program Files (x86)\WindowsApps
Removed TrustedInstaller from C:\Program Files (x86)\WindowsApps
Full control granted for C:\Program Files (x86)\WindowsApps

Permissions fixed successfully for all matching folders.
```

## Important Notes
- **Backup Your System:** Always back up your system before running scripts that modify system permissions.
- **Run as Administrator:** The script must be run with administrative privileges to modify system folders.
- **Test on Non-Critical Folders:** Test the script on non-critical folders first to ensure it works as expected.
- **System Stability:** Modifying system folders can have serious consequences, including breaking your operating system. Use this script at your own risk.

## Troubleshooting
- **Permission Denied Errors:** If the script encounters folders it cannot access, it will skip them and continue.
- **No Folders Found:** If no matching folders are found, double-check the `folder_name_to_search` and `root_directory` variables.
- **Script Fails to Run:** Ensure Python is installed and the script is run as an administrator.

## License
This script is provided under the **MIT License**. Feel free to modify and distribute it as needed.

---

## Code Overview

### Key Functions
1. **`is_admin()`:** Checks if the script is running with administrative privileges.
2. **`take_ownership(folder_path)`:** Takes ownership of the folder using the `takeown` command.
3. **`remove_trustedinstaller(folder_path)`:** Removes `TrustedInstaller` as the owner using the `icacls` command.
4. **`grant_full_control(folder_path)`:** Grants full control to the current user using the `icacls` command.
5. **`search_folders(root_dir, folder_name)`:** Searches for folders with a specific name within a root directory.
6. **`fix_permissions(folder_path)`:** Fixes permissions for the specified folder.

### Example Configuration
```python
# Specify the folder name to search for
folder_name_to_search = "WindowsApps"  # Change this to the folder name you want to search for
root_directory = "C:\\"  # Change this to the root directory where you want to start the search
```

---

## Contributing
If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.
