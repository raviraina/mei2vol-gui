from tkinter import *
from tkinter import filedialog, messagebox
import mei2volpiano

# setup
root = Tk()
root.title("MEI2Volpiano")
root.geometry("1000x400")
lib = mei2volpiano.MEItoVolpiano()

# open button functionality
def open_txt():
    mei_file = filedialog.askopenfilename(initialdir="~")
    print()
    if mei_file is None:
        return

    with open(mei_file, "r") as f:
        try:
            volpiano_str = lib.convert_mei_volpiano(f)
        except:
            messagebox.showerror("Error", "Invalid file or corrupted MEI formatting.")
            return

        if len(text.get("1.0", END)) >= 1:
            text.delete("1.0", END)

        text.insert(END, volpiano_str)

    return volpiano_str


# save button functionality
def save_txt():
    if len(text.get("1.0", END)) > 1:
        vol_file = filedialog.asksaveasfilename()

        with open(vol_file, "w") as f:
            f.write(text.get(1.0, END))
    else:
        messagebox.showerror("Error", "Did not find volpiano string to export.")

# gui
text = Text(root, width=400, height=10, font=("Helvetica", 16))
text.pack(pady=20)

open_button = Button(root, text="Open MEI File", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save Volpiano String", command=save_txt)
save_button.pack(pady=20)

root.mainloop()
