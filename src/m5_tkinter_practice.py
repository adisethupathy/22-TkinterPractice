"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Adi Sethupathy.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------

    root = tkinter.Tk()



    # ------------------------------------------------------------------
    # done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()
    # ------------------------------------------------------------------
    # done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------

    button = ttk.Button(frame1, text='RED')
    button.grid()

    # ------------------------------------------------------------------
    # done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    button['command'] = lambda:(print('hello'))

    # ------------------------------------------------------------------
    # done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------

    entry1 = ttk.Entry(frame1)
    entry1.grid()
    btn = ttk.Button(frame1, text='hello')
    btn.grid()

    def btn_stuff(entry):
        contents = entry1.get()
        if contents == 'ok':
            print('Goodbye')
        else:
            print('Hello')
    btn['command'] = lambda:(btn_stuff(entry1))

    # ------------------------------------------------------------------
    # done: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    entry2 = ttk.Entry(frame1)
    entry2.grid()
    btn2 = ttk.Button(frame1, text='bang')
    btn2.grid()

    btn2['command'] = lambda:(todo7(entry1, entry2))

    # ------------------------------------------------------------------
    # done: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    def todo7(entrya, entryb):
        s = entrya.get()
        n = int(s)
        strang = entryb.get()

        print(strang*n)
    root.mainloop()




# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
