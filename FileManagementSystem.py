import tkinter as tk
from tkinter import messagebox, simpledialog


# File class to represent files
class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

    def __str__(self):
        return f"File(name={self.name})"

    def read_content(self):
        return self.content

    def write_content(self, content):
        self.content = content


# Folder class to represent folders
class Folder:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def __str__(self):
        return f"Folder(name={self.name})"

    def add_item(self, item):
        if item.name in self.children:
            raise ValueError(f"{item.name} already exists in {self.name}")
        self.children[item.name] = item

    def remove_item(self, name):
        if name in self.children:
            del self.children[name]
        else:
            raise ValueError(f"{name} not found in {self.name}")

    def get_item(self, name):
        return self.children.get(name)


# FileSystem class to manage folders and files
class FileSystem:
    def __init__(self):
        self.root = Folder("root")
        self.current_folder = self.root

    def create_folder(self, name):
        new_folder = Folder(name)
        self.current_folder.add_item(new_folder)

    def create_file(self, name, content=""):
        new_file = File(name, content)
        self.current_folder.add_item(new_file)

    def delete_item(self, name):
        self.current_folder.remove_item(name)

    def navigate_to_folder(self, folder_name):
        if folder_name in self.current_folder.children:
            folder = self.current_folder.children[folder_name]
            if isinstance(folder, Folder):
                self.current_folder = folder
            else:
                raise ValueError(f"{folder_name} is a file, not a folder.")
        else:
            raise ValueError(f"{folder_name} not found.")

    def list_items(self):
        return [str(item) for item in self.current_folder.children.values()]

    def read_file(self, name):
        file = self.current_folder.get_item(name)
        if isinstance(file, File):
            return file.read_content()
        raise ValueError(f"{name} is not a file.")

    def write_file(self, name, content):
        file = self.current_folder.get_item(name)
        if isinstance(file, File):
            file.write_content(content)
        else:
            raise ValueError(f"{name} is not a file.")


# GUI Class for File Management System
class FileManagementGUI:
    def __init__(self, root):
        self.fs = FileSystem()
        self.root = root
        self.root.title("File Management System")

        # Folder history stack
        self.folder_history = []

        # Frame for display and controls
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Listbox for displaying files and folders
        self.listbox = tk.Listbox(self.frame, width=50, height=15)
        self.listbox.pack()

        # Buttons for actions
        self.create_folder_button = tk.Button(self.frame, text="Create Folder", command=self.create_folder)
        self.create_folder_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.create_file_button = tk.Button(self.frame, text="Create File", command=self.create_file)
        self.create_file_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Item", command=self.delete_item)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.navigate_button = tk.Button(self.frame, text="Navigate", command=self.navigate_to_folder)
        self.navigate_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.open_button = tk.Button(self.frame, text="Open File", command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.back_button = tk.Button(self.frame, text="Back", command=self.go_back)
        self.back_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.update_listbox()

    # Function to update the listbox with current folder items
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        items = self.fs.list_items()
        for item in items:
            self.listbox.insert(tk.END, item)

    # Create a new folder
    def create_folder(self):
        name = simpledialog.askstring("Input", "Enter folder name:")
        if name:
            try:
                self.fs.create_folder(name)
                self.update_listbox()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    # Create a new file
    def create_file(self):
        name = simpledialog.askstring("Input", "Enter file name:")
        if name:
            content = simpledialog.askstring("Input", "Enter file content:")
            try:
                self.fs.create_file(name, content)
                self.update_listbox()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    # Delete a file or folder
    def delete_item(self):
        selected = self.listbox.get(tk.ACTIVE)
        name = selected.split("(")[1].split("=")[1][:-1]
        try:
            self.fs.delete_item(name)
            self.update_listbox()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Navigate to a folder
    def navigate_to_folder(self):
        selected = self.listbox.get(tk.ACTIVE)
        if "Folder" in selected:
            folder_name = selected.split("(")[1].split("=")[1][:-1]
            try:
                self.folder_history.append(self.fs.current_folder)  # Save the current folder in history
                self.fs.navigate_to_folder(folder_name)
                self.update_listbox()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Selected item is not a folder")

    # Go back to the previous folder
    def go_back(self):
        if self.folder_history:
            self.fs.current_folder = self.folder_history.pop()  # Restore the last folder from history
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "No previous folder to go back to.")

    # Open and read a file
    def open_file(self):
        selected = self.listbox.get(tk.ACTIVE)
        if "File" in selected:
            file_name = selected.split("(")[1].split("=")[1][:-1]
            try:
                content = self.fs.read_file(file_name)
                messagebox.showinfo("File Content", f"{file_name} content:\n{content}")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Selected item is not a file")


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = FileManagementGUI(root)
    root.mainloop()
