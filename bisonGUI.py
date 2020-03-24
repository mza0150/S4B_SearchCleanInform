import tkinter as tk

window = tk.Tk()
window.title("Search-Clean-Inform")

greeting_frame = tk.Frame(master=window, height=25)
greeting_frame.grid(row=0, column=0)

greeting_label = tk.Label(master=greeting_frame, text="Welcome to Search-Clean-Inform!")
greeting_label.grid(row=0, column=0)


species_entry_frame = tk.Frame(master=window)
species_entry_frame.grid(row=1, column=0)
#species_entry_frame.pack(fill=tk.X)

species_entry = tk.Entry(master=species_entry_frame)
species_entry.insert(0, "Ex: Bison bison")
species_entry.grid(row=0, column=0)
#species_entry.pack()

species_name = species_entry.get()
print(species_name)

window.mainloop()
