import tkinter as tk
from counter import Counter, start_counting
from gui import update_count, count_label, start_button

def start_counter():
    counter = Counter()
    start_counting(counter)
    update_count(count_label, counter.count)

def main():
    root = tk.Tk()
    start_button.config(command=start_counter)
    root.mainloop()

if __name__ == "__main__":
    main()