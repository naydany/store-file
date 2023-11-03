# import tkinter as tk
# import time
# import ImageTk

# class SplashScreen:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("400x300")
#         self.root.overrideredirect(True)

#         self.image = ImageTk.PhotoImage(file="image/background.png")
#         self.label = tk.Label(self.root, image=self.image)
#         self.label.pack()

#         self.root.after(3000, self.destroy_splash_screen)

#     def destroy_splash_screen(self):
#         self.root.destroy()

#     def start(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     splash_screen = SplashScreen()
#     splash_screen.start()


from tkinter import Tk, Label
from tkinter.ttk import Progressbar
root = Tk()
root.overrideredirect(True)  # Removes title bar and borders
root.geometry("300x200+500+250")  # Set the size and position of the window
root.configure(bg='white')  # Set the background color
label = Label(root, text="My Application", font=("Arial", 18), bg='white')
label.pack(pady=50)

progress_bar = Progressbar(root, length=200, mode='indeterminate')
progress_bar.pack(pady=20)

# Add any additional widgets you want to display on the splash screen
def splash_update():
    # Update the progress bar or perform any other tasks here
    # ...

    root.after(100, splash_update)  # Schedule the update function to run every 100 milliseconds

splash_update()  # Start the update process

root.mainloop()  # Run the Tkinter event loop
def close_splash():
    root.destroy()  # Close the splash screen window

root.after(3000, close_splash)  # Close the splash screen after 3000 milliseconds (3 seconds)
from tkinter import Tk, Label
from tkinter.ttk import Progressbar

root = Tk()
root.overrideredirect(True)
root.geometry("300x200+500+250")
root.configure(bg='white')

label = Label(root, text="My Application", font=("Arial", 18), bg='white')
label.pack(pady=50)

progress_bar = Progressbar(root, length=200, mode='indeterminate')
progress_bar.pack(pady=20)

def splash_update():
    # Update the progress bar or perform any other tasks here
    # ...

    root.after(100, splash_update)

splash_update()

def close_splash():
    root.destroy()

root.after(3000, close_splash)

root.mainloop()