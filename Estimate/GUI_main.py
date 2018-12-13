# Created by Naman Gupta (00512693)
# Created on 11-12-2018 at 15:34

import tkinter as tk
from tkinter import ttk
from GUI_fileDetails import detail_pane
from GUI_tableParticulars import table
from GUI_conclusion import conclusion

window=tk.Tk()

# Open window in maximized mode
# window.state('zoomed')
window.wm_iconbitmap('estimate.ico')
window.title('Estimate Builder')

# Title of the Window
tk.Label(window, text="Estimate").grid(row=0, column=0, columnspan = 6, padx=10, pady=5)

# Details
detail_pane(window,1,0,6)

# Table
table(window,2,0,6)

# Tabular Conclusion
conclusion(window,3,5,1)

# Print
pane = ttk.Panedwindow(window, orient=tk.VERTICAL)
pane.grid(row=4, column=5, columnspan = 1)  # Pack to make visible
# first pane, which would get widgets gridded into it:
frame = ttk.Labelframe(pane, text='Print')
tk.Button(frame, text="Print").grid(row=0, column=0, columnspan=1, padx=10, pady=5)  # Add command later
tk.Button(frame, text="Print Preview").grid(row=0, column=1, columnspan=1, padx=10, pady=5)  # Add command later
pane.add(frame)

# Note
pane = ttk.Panedwindow(window, orient=tk.VERTICAL)
pane.grid(row=5, column=0 , columnspan = 6)  # Pack to make visible
# first pane, which would get widgets gridded into it:
f1 = ttk.Labelframe(pane, text='Note')
note1 = tk.Entry(f1, width=100)
note1.grid(row=0, column=0, columnspan=1, padx=10, pady=5)
note2 = tk.Entry(f1, width=100)
note2.grid(row=1, column=0, columnspan=1, padx=10, pady=5)
note2 = tk.Entry(f1, width=100)
note2.grid(row=2, column=0, columnspan=1, padx=10, pady=5)
note2 = tk.Entry(f1, width=100)
note2.grid(row=3, column=0, columnspan=1, padx=10, pady=5)
pane.add(f1)

# Add About
pane = ttk.Panedwindow(window, orient=tk.VERTICAL)
pane.grid(row=6, column=0 , columnspan = 6)  # Pack to make visible
# first pane, which would get widgets gridded into it:
f1 = ttk.Labelframe(pane, text='About')
tk.Label(f1, text="v1.0.0").grid(row=0, column=0, padx=10, sticky="E")
tk.Label(f1, text=" ").grid(row=0, column=1, ipadx=300, sticky="W")
tk.Label(f1, text="Created by: Naman Gupta (00512693)").grid(row=0, column=2, padx=10, sticky="W")
pane.add(f1)

window.mainloop()