from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from sys import exit as sysExit
import os

class gui:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title('erfan011')
        self.window.resizable(False, False)
        self.window.iconbitmap("icon.ico")
        self.r = 2


class Encryptor(gui):
    def __init__(self) -> None:
        super().__init__()
        self.key_file = ".key.key"
        
        if not os.path.exists(self.key_file):
            self.key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(self.key)
        
        with open(self.key_file, "rb") as f:
            self.fernet = Fernet(f.read())


    def decryptf(self, file):
        with open(file, "rb") as f:
            defile = self.fernet.decrypt(f.read())
        
        with open(file, "wb") as f:
            f.write(defile)


    def encryptf(self, file):
        with open(file, "rb") as f:
            enfile = self.fernet.encrypt(f.read())
        
        with open(file, "wb") as f:
            f.write(enfile)


    def crop(self, dir, func, t):
        if os.path.isfile(dir):
            func(dir)
        
        elif os.path.isdir(dir):
            for root, subs, files in os.walk(dir):
                for file in files:
                    func(f"{root}/{file}")
        
        Label(self.window, text=t, fg="#00a000").grid(row=self.r, columnspan=10)
        self.r += 1


    def generate_new_key(self):
        yn = messagebox.askyesno("attention", "are you sure you want to change the key?\nits recommended to decrypt all the files that were encrypted before changing the key!", default="no")
        if yn:
            new_key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.truncate(0)
                f.write(new_key)
            with open(self.key_file, "rb") as f:
                self.fernet = Fernet(f.read())
            Label(self.window, text="key changed successfully", fg="#00a000").grid(row=self.r, columnspan=10)
            self.r += 1
    
    
    def openFile(self, entry:Entry):
        entry.delete(0, END)
        entry.insert(END, filedialog.askopenfilename(title="Select a file of any type",
                                                     filetypes=[("All files", "*.*")]))


    def openFolder(self, entry:Entry):
        entry.delete(0, END)
        entry.insert(END, filedialog.askdirectory(title="Select a directory"))


def main():
    c = Encryptor()
    
    
    Label(c.window, text="directory: ", bd=0).grid(row=0, column=0)
    e = Entry(c.window,
              bg = "#000000",
              fg = "#ffffff",
              width = 12,
              bd = 4)
    e.grid(row=0, column=1)

    open_file_btn = Button(c.window,
                           text="file",
                           bg="#000000",
                           fg="#ffffff",
                           width=11,
                           activebackground="#ffffff",
                           activeforeground="#000000",
                           bd=6,
                           command=lambda: c.openFile(e))
    open_file_btn.grid(row=0, column=2)
	
    open_folder_btn = Button(c.window,
                             text="folder",
                             bg="#000000",
                             fg="#ffffff",
                             width=10,
                             activebackground="#ffffff",
                             activeforeground="#000000",
                             bd=6,
                             command=lambda: c.openFolder(e))
    open_folder_btn.grid(row=0, column=3)
    
    encrypt_btn = Button(c.window,
                         text = "encrypt",
                         bg = "#000000",
                         fg = "#ffffff",
                         width = 10,
                         activebackground = "#ffffff",
                         activeforeground = "#000000",
                         bd = 6,
                         command = lambda: c.crop(e.get(), c.encryptf, "successfully encrypted"))
    encrypt_btn.grid(row=1, column=0)
    
    decrypt_btn = Button(c.window,
                         text = "decrypt",
                         bg = "#000000",
                         fg = "#ffffff",
                         width = 10,
                         activebackground = "#ffffff",
                         activeforeground = "#000000",
                         bd = 6,
                         command = lambda: c.crop(e.get(), c.decryptf, "successfully decrypted"))
    decrypt_btn.grid(row=1, column=1)
    
    change_key_btn = Button(c.window,
                            text="change key",
                            bg="#000000",
                            fg="#ffffff",
                            width=11,
                            activebackground="#ffffff",
                            activeforeground="#000000",
                            bd=6,
                            command=c.generate_new_key)
    change_key_btn.grid(row=1, column=2)
    
    quit_btn = Button(c.window,
                      text = "QUIT",
                      bg = "#000000",
                      fg = "#ffffff",
                      width = 10,
                      activebackground = "#ffffff",
                      activeforeground = "#000000",
                      bd = 6,
                      command = sysExit)
    quit_btn.grid(row=1, column=3)
    
    c.window.mainloop()


if __name__ == "__main__":
    main()