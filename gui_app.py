import tkinter as tk

def start_camera():
    print("Camera Started")

def mouse_mode():
    print("Mouse Mode")

def gesture_mode():
    print("Gesture Mode")

root = tk.Tk()
root.title("AI Control System")
root.geometry("300x300")

label = tk.Label(roimport tkinter as tk
import subprocess

def start_camera():
    # This will run your hand_tracking.py
    subprocess.Popen(["python", "hand_tracking.py"])

def mouse_mode():
    print("Mouse Mode (we will connect later)")

def gesture_mode():
    print("Gesture Mode (later)")

root = tk.Tk()
root.title("AI Control System")
root.geometry("300x300")

label = tk.Label(root, text="AI Control System", font=("Arial", 16))
label.pack(pady=10)

tk.Button(root, text="Start Camera", command=start_camera).pack(pady=5)
tk.Button(root, text="Mouse Mode", command=mouse_mode).pack(pady=5)
tk.Button(root, text="Gesture Mode", command=gesture_mode).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()ot, text="AI Control System", font=("Arial", 16))
label.pack(pady=10)

tk.Button(root, text="Start Camera", command=start_camera).pack(pady=5)
tk.Button(root, text="Mouse Mode", command=mouse_mode).pack(pady=5)
tk.Button(root, text="Gesture Mode", command=gesture_mode).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()