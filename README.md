# File Management System

A Python-based File Management System with a graphical interface built using Tkinter. This project simulates basic file operations, allowing users to create, delete, and navigate through folders and files, making it a great tool to understand file organization and GUI development in Python.

## Features

- **Create Files and Folders**: Users can create new folders and files within any directory.
- **Delete Items**: Supports deletion of files and folders in the current directory.
- **Navigate Through Folders**: Navigate into folders to view their contents.
- **Back Button**: Return to the previous folder with a functional back button.
- **File Operations**: View and edit file content.

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/vansh070605/file-management-system.git
   cd file-management-system
   ```
2. Run the application:
   ```bash
   python file_management.py
   ```

## Project Structure

- **File Class**: Represents individual files with name and content attributes.
- **Folder Class**: Manages folders and their contents (other folders and files).
- **FileSystem Class**: Handles core file and folder operations (create, delete, navigate).
- **FileManagementGUI Class**: Provides a Tkinter GUI for user interaction.

## Requirements

- **Python 3.x**
- **Tkinter** (usually pre-installed with Python)

## How to Use

1. **Create Folder/File**: Use the buttons to add folders or files in the current directory.
2. **Delete Item**: Select an item and click "Delete Item" to remove it.
3. **Navigate**: Select a folder and click "Navigate" to enter it. Use "Back" to return to the previous folder.
4. **Open File**: Select a file and click "Open File" to view its content.
