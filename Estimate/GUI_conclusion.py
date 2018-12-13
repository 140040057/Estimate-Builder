# Created by Naman Gupta (00512693)
# Created on 12-12-2018 at 09:51

import tkinter as tk
from tkinter import ttk


def conclusion(window, row, column, columnspan):
    pane = ttk.Panedwindow(window, orient=tk.VERTICAL)
    pane.grid(row=row, column=column, columnspan=columnspan)  # Pack to make visible
    # first pane, which would get widgets gridded into it:
    frame = ttk.Labelframe(pane, text='Balances')
    # Sub Total
    tk.Label(frame, text="Sub Total").grid(row=0, column=0, columnspan=1, padx=10, pady=5)
    sub_tot = tk.Entry(frame, width=15)
    sub_tot.grid(row=0, column=2, columnspan=1, padx=10, pady=5)
    # Discount
    tk.Label(frame, text="Discount").grid(row=1, column=0, columnspan=1, padx=10, pady=5)
    temp = tk.StringVar(frame)
    temp.set("18%")  # default value
    w = tk.OptionMenu(frame, temp, "8%", "18%", "28%")
    w.grid(row=1, column=1, columnspan=1, padx=10, pady=5)
    disc = tk.Entry(frame, width=15)
    disc.grid(row=1, column=2, columnspan=1, padx=10, pady=5)
    # Sub Total with Discount
    tk.Label(frame, text="Sub Total").grid(row=2, column=0, columnspan=1, padx=10, pady=5)
    sub_tot_d = tk.Entry(frame, width=15)
    sub_tot_d.grid(row=2, column=2, columnspan=1, padx=10, pady=5)
    # GST
    tk.Label(frame, text="GST").grid(row=3, column=0, columnspan=1, padx=10, pady=5)
    temp = tk.StringVar(frame)
    temp.set("18%")  # default value
    w = tk.OptionMenu(frame, temp, "8%", "18%", "28%")
    w.grid(row=3, column=1, columnspan=1, padx=10, pady=5)
    gst = tk.Entry(frame, width=15)
    gst.grid(row=3, column=2, columnspan=1, padx=10, pady=5)
    # Total
    tk.Label(frame, text="Total").grid(row=4, column=0, columnspan=1, padx=10, pady=5)
    total = tk.Entry(frame, width=15)
    total.grid(row=4, column=2, columnspan=1, padx=10, pady=5)
    pane.add(frame)
