import tkinter as tk
import serial
import threading
import time
ser = serial.Serial('COM3', 9600) ## COM3 arduinonun bağlandıgı port 
havuz_data = 0 
 
def veri_okuma():
    global havuz_data 
  
    while True:
        if ser.in_waiting :
            
            data = float(ser.readline().decode('utf-8').strip())
            havuz_data= 15-data            
            root.after(0, label_var.set, f"Mesafe: {havuz_data:.2f} cm")
            
            if  data >= 15 :
                root.after(0, label1_var.set, "open")
            elif data <= 4 :
                root.after(0, label1_var.set, "close")            
                
        time.sleep(0.001)

def veri_yazma():
    thread = threading.Thread(target=veri_okuma, daemon=True)
    thread.start()
    



root = tk.Tk()
root.title("Arduino Mesafe Sensörü")
root.geometry("300x200")
tk.Label(root, text="havuzda kalan su seviyesi").pack()

label_var = tk.StringVar()
label_var.set("Veri bekleniyor...")
label1_var = tk.StringVar()

label = tk.Label(root, textvariable=label_var, font=("Arial", 14))
label.pack(pady=20)

label1 = tk.Label(root, textvariable=label1_var, font=("Arial",11))
label1.pack(pady=15)

veri_yazma()  

 
root.mainloop()



    
    
