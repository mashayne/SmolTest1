import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("Counter App")

    count_label = tk.Label(root, text="0", font=("Helvetica", 48), fg="black")
    count_label.pack(pady=10)

    start_button = tk.Button(root, text="Start Counting", command=None)
    start_button.pack(pady=10)

    return root, count_label, start_button

def update_count(count):
    count_label['text'] = str(count)
    root.update()