from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from os.path import getsize
import os

from Chaos.Encryption import encrypt
from Chaos.Decryption import decrypt

root = Tk()
root.geometry("600x600")
root.configure(background="#26292c")
root.title("Chaos Based Image Encryption")
curr = os.getcwd()

save_directory = StringVar()

# Function to choose a file from the system directory
def askopenfile():
    path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
    input_file_entry.delete(0, 'end')
    input_file_entry.insert(END, path)
    
    if path:
        im = Image.open(path)
        im = im.resize((200, 200), Image.LANCZOS)
        tkimage = ImageTk.PhotoImage(im)
        print(getsize(path))
        myvar = Label(root, image=tkimage)
        myvar.image = tkimage
        myvar.grid(row=1, column=0)

# Function to choose a directory to save encrypted images
def choose_save_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        save_directory.set(folder_selected)
        save_location_entry.delete(0, 'end')
        save_location_entry.insert(END, folder_selected)

# Encrypt function with file saving
def doencrypt():
    loc = input_file_entry.get()
    key = password_entry.get()
    
    if not save_directory.get():
        print("⚠ Please select a save location first.")
        return
    
    encrypted_image = encrypt(loc, key)
    save_path = os.path.join(save_directory.get(), "encrypted_image.png")
    encrypted_image.save(save_path)
    
    im = Image.open(save_path)
    im = im.resize((200, 200), Image.LANCZOS)
    tkimage = ImageTk.PhotoImage(im)
    myvar = Label(root, image=tkimage)
    myvar.image = tkimage
    myvar.grid(row=1, column=1)
    print(f"🔒 Encrypted image saved at: {save_path}")

# Decrypt function
def dodecrypt():
    loc = os.path.join(save_directory.get(), "encrypted_image.png")
    decrypted_image = decrypt(loc, password_entry.get())
    save_path = os.path.join(save_directory.get(), "decrypted_image.png")
    decrypted_image.save(save_path)
    
    im = Image.open(save_path)
    im = im.resize((200, 200), Image.LANCZOS)
    tkimage = ImageTk.PhotoImage(im)
    myvar = Label(root, image=tkimage)
    myvar.image = tkimage
    myvar.grid(row=1, column=1)
    print(f"🔓 Decrypted image saved at: {save_path}")

browse_input_file = Button(root, text="Select Image", command=askopenfile, width=15, height=2, bg="#657cc3")
input_file_entry = Entry(root, width=28)

password = Label(root, text="Enter Key", width=18, height=1, bg="#657cc3")
password_entry = Entry(root, width=20)

save_location_label = Label(root, text="Save Location", width=18, height=1, bg="#657cc3")
save_location_entry = Entry(root, width=28)
choose_save_button = Button(root, text="Choose Folder", command=choose_save_directory, width=15, height=2, bg="#657cc3")

encryptb = Button(root, text="Encrypt Image", width=18, height=2, command=doencrypt, bg="#37b448")
decryptb = Button(root, text="Decrypt Image", width=18, height=2, command=dodecrypt, bg="#37b448")

browse_input_file.grid(row=0, padx=80, pady=10)
input_file_entry.grid(row=0, column=1, padx=50)
password.grid(row=2, columnspan=5, pady=10)
password_entry.grid(row=3, columnspan=5)
save_location_label.grid(row=4, columnspan=5, pady=10)
save_location_entry.grid(row=5, column=0, padx=50)
choose_save_button.grid(row=5, column=1)
encryptb.grid(row=6, columnspan=5, pady=10)
decryptb.grid(row=7, columnspan=5, pady=15)

root.mainloop()

