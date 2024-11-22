from tkinter import *

from Scripts.approve_all_roles import approve_all_users
from Scripts.click_on_help_allies_image import  help_allies

root = Tk()
root.title('Game Bot')
canvas = Canvas(root, width=600, height=300)
canvas.pack()

# button description
app_label = Label(root, text="approve users in list for all 5 roles", fg='blue', font=('Arial', 11))
canvas.create_window(200, 25, window=app_label)
# button approve users
approve_users = Button(root, text='Approve Users', command=approve_all_users)
canvas.create_window(200, 50, window=approve_users)

# button description
app_label = Label(root, text="click on help allies button if visible", fg='blue', font=('Arial', 11))
canvas.create_window(200,100, window=app_label)
help_allies = Button(root, text='Help allies', command=help_allies)
canvas.create_window(200, 125, window=help_allies)

# loop
root.mainloop()
