import tkinter as tk
from tkinter import scrolledtext
import wmi
 
 
def get_hardware_info():
   hardware_info.delete(1.0, tk.END)  # Clear previous info
 
 
   c = wmi.WMI()
 
 
   hardware_info.insert(tk.END, "Disk Drives:\n")
   for disk in c.Win32_DiskDrive():
       hardware_info.insert(tk.END, f"Model: {disk.Model}\n")
       hardware_info.insert(tk.END, f"Interface Type: {disk.InterfaceType}\n")
       hardware_info.insert(tk.END, f"Size: {int(disk.Size) / (1024 ** 3):.2f} GB\n")
       hardware_info.insert(tk.END, f"Serial Number: {disk.SerialNumber}\n")
       hardware_info.insert(tk.END, f"Status: {disk.Status}\n\n")
 
 
   hardware_info.insert(tk.END, "\nNetwork Adapters:\n")
   for interface in c.Win32_NetworkAdapter():
       hardware_info.insert(tk.END, f"Name: {interface.Name}\n")
       hardware_info.insert(tk.END, f"Description: {interface.Description}\n")
       hardware_info.insert(tk.END, f"MAC Address: {interface.MACAddress}\n")
       if interface.Speed is not None:
           if interface.Speed.isdigit():  # Check if speed is a digit
               hardware_info.insert(tk.END,
                                    f"Speed: {int(interface.Speed) / 10 ** 6} Mbps\n")  # Convert to integer before division
           else:
               hardware_info.insert(tk.END, f"Speed: Unknown\n")
       else:
           hardware_info.insert(tk.END, f"Speed: Unknown\n")
       hardware_info.insert(tk.END, f"Manufacturer: {interface.Manufacturer}\n")
       hardware_info.insert(tk.END, f"Net Connection ID: {interface.NetConnectionID}\n\n")
 
 
   hardware_info.insert(tk.END, "\nGraphics Processing Units (GPUs):\n")
   for gpu in c.Win32_VideoController():
       hardware_info.insert(tk.END, f"Name: {gpu.Name}\n")
       hardware_info.insert(tk.END, f"Adapter RAM: {gpu.AdapterRAM / (1024 ** 3):.2f} GB\n")
       hardware_info.insert(tk.END, f"Caption: {gpu.Caption}\n")
       hardware_info.insert(tk.END, f"Status: {gpu.Status}\n\n")
 
 
# Create the main application window
root = tk.Tk()
root.title("Hardware Information - The Pycodes")
 
 
# Create a scrolled text widget to display hardware info
hardware_info = scrolledtext.ScrolledText(root, width=80, height=30, wrap=tk.WORD)
hardware_info.pack(expand=True, fill="both", padx=10, pady=10)
 
 
# Create a button to fetch hardware info
fetch_button = tk.Button(root, text="Fetch Hardware Info", command=get_hardware_info)
fetch_button.pack(pady=10)
 
 
# Run the Tkinter event loop
root.mainloop()
