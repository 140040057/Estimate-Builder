# Created by Naman Gupta (00512693)
# Created on 12-12-2018 at 09:47

import tkinter as tk
from tkinter import ttk


def table(window, row, column, columnspan):
    pane = ttk.Panedwindow(window, orient=tk.VERTICAL)
    pane.grid(row=row, column=column, columnspan=columnspan)  # Pack to make visible
    # first pane, which would get widgets gridded into it:
    frame = ttk.Labelframe(pane, text='Table')
    tk.Label(frame, text="S. No.").grid(row=0, column=0, columnspan=1, padx=10, pady=5)
    tk.Label(frame, text="Description of works").grid(row=0, column=1, columnspan=1, padx=10, pady=5)
    tk.Label(frame, text="Qty.").grid(row=0, column=2, columnspan=1, padx=(10, 5), pady=5)
    tk.Label(frame, text="Unit").grid(row=0, column=3, columnspan=1, padx=(0, 0), pady=5)
    tk.Label(frame, text="Rate").grid(row=0, column=4, columnspan=1, padx=10, pady=5)
    tk.Label(frame, text="Amount").grid(row=0, column=5, columnspan=1, padx=10, pady=5)

    # Tabular Row
    s_no = tk.Entry(frame, width=15)
    s_no.grid(row=1, column=0, columnspan=1, padx=10, pady=5)
    desc = tk.Entry(frame, width=84)
    desc.grid(row=1, column=1, columnspan=1, padx=10, pady=5)
    qty = tk.Entry(frame, width=15)
    qty.grid(row=1, column=2, columnspan=1, padx=10, pady=5)
    unit = tk.Entry(frame, width=15)
    unit.grid(row=1, column=3, columnspan=1, padx=10, pady=5)
    rate = tk.Entry(frame, width=15)
    rate.grid(row=1, column=4, columnspan=1, padx=10, pady=5)
    amt = tk.Entry(frame, width=15)
    amt.grid(row=1, column=5, columnspan=1, padx=10, pady=5)

    # Add row
    tk.Button(frame, text="Add row").grid(row=2, column=0, columnspan=1, padx=10, pady=5)  # Add command later
    pane.add(frame)
