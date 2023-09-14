import tkinter
from tkinter import END

# ------------------------VARIABLES---------------------------
TEXT_TOP = "You have: "
TEXT_BOTTOM = "Text disappear when you stop write after: "

# -----------------FUNCTIONS-------------------


def count_down(count, label, reset, text):
    new_id = root.eval('after info').split()
    if count > 0 and not reset:
        label['text'] = f"{text} {count}.sec"
        root.after(1000, lambda: count_down(count-1, label, reset=False, text=text))

        if len(new_id) == 3:
            root.after_cancel(new_id[1])

        if len(new_id) > 2:
            root.after_cancel(new_id[0])

    elif count == 0:
        text_entry.delete("1.0", END)

    elif reset:
        count_down(count=count, label=label, reset=False, text=text)


def countdown():
    root.after(300000, lambda: root.destroy())


# --------------------WINDOW MAIN LOOP------------------------
root = tkinter.Tk()
root.title("Disappearing text app")
root.configure(borderwidth="4", bg="black")
root.geometry("800x600")

# ---------------------------WIDGETS--------------------------
label_top_text = tkinter.Label(root, text="Start writing something:")
label_top_text.config(font=("Calibri", 20), bg='black', fg="white")
label_top_text.grid(row=0, column=0)

label_top_countdown = tkinter.Label(root, text=f"{TEXT_TOP}5.min")
label_top_countdown.config(font=("Calibri", 20), fg="white", bg="black")
label_top_countdown.grid(row=0, column=1)

label_bottom_count = tkinter.Label(root, text=f"{TEXT_BOTTOM}10.sec")
label_bottom_count.config(font=("Calibri", 20), bg="black", fg="white")
label_bottom_count.grid(row=2, column=0)

text_entry = tkinter.Text(root, width=56, height=15, bg="grey", highlightthickness=2)
text_entry.config(font=("Calibri", 20))
text_entry.grid(row=1, column=0, columnspan=2)

countdown()

# -----------KeyBoard detection---------------------------
root.bind('<Any-KeyPress>', lambda e: count_down(count=10, label=label_bottom_count,
          reset=True, text=TEXT_BOTTOM))

root.mainloop()
