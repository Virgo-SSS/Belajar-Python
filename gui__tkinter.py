#belajar membuat button
# masih setengah belajar dan masih belum paham




from functools import partial
import tkinter as tk

BTNLIST = [0.0, 0.1, 0.2]

def btn_clicked(payload=None):
    """Just prints out given payload."""
    print('Me was clicked. Payload: {}'.format(payload))


def init_controls():
    """Prepares GUI controls and starts mainloop"""
    root = tk.Tk()
    menu = tk.Menu(root)
    root.config(menu=menu)
    sample_menu = tk.Menu(menu)
    menu.add_cascade(label="Destiny", menu=sample_menu)
    for btn_value in BTNLIST:
        sample_menu.add_command(
            label=btn_value,
            # Here is the trick with partial
            command=partial(btn_clicked, btn_value)
        )
    root.mainloop()


init_controls()