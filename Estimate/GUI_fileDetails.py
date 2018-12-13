# Created by Naman Gupta (00512693)
# Created on 12-12-2018 at 09:33

import tkinter as tk
from tkinter import ttk
import datetime


now = datetime.datetime.now()

def detail_pane(window, row, column, columnspan):
    pane = ttk.Panedwindow(window, orient=tk.VERTICAL)
    pane.grid(row=row, column=column, columnspan=columnspan)  # Pack to make visible
    # first pane, which would get widgets gridded into it:
    frame = ttk.Labelframe(pane, text='Details')
    tk.Label(frame, text="Date:").grid(row=0, column=0, columnspan=1, padx=10, pady=5)
    tk.Label(frame, text=now.strftime("%d-%m-%Y")).grid(row=0, column=1, columnspan=1, padx=10, pady=5)
    tk.Label(frame, text="Name of the Work").grid(row=0, column=2, columnspan=1, padx=10, pady=5)
    work_name = tk.Entry(frame, width=100)
    work_name.grid(row=0, column=3, columnspan=1, padx=10, pady=5)
    tk.Label(frame, text="Ref. No.").grid(row=0, column=4, columnspan=1, padx=(10, 5), pady=5)
    tk.Label(frame, text="JD/").grid(row=0, column=5, columnspan=1, padx=(0, 0), pady=5)
    ref_num = tk.Entry(frame, width=20)
    ref_num.grid(row=0, column=6, columnspan=2, padx=(0, 5), pady=5)
    pane.add(frame)
