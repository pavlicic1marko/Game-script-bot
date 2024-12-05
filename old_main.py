from tkinter import *
from Scripts.Remove_stale_roles import remove_all_stale_roles
from Scripts.approve_all_roles import approve_all_users
from Scripts.click_on_help_allies_image import  help_allies

root = Tk()
root.title('Game Bot')
canvas = Canvas(root, width=600, height=300)
canvas.pack()

# button approve users
approve_users = Button(root, text='Approve Users', command=approve_all_users)
canvas.create_window(200, 50, window=approve_users)
# button description
app_label = Label(root, text="approve users in list for all 5 roles", fg='blue', font=('Arial', 11))
canvas.create_window(200, 25, window=app_label)

# button help allies
help_allies = Button(root, text='Help allies', command=help_allies)
canvas.create_window(200, 125, window=help_allies)
# button description
app_label = Label(root, text="click on help allies button if visible", fg='blue', font=('Arial', 11))
canvas.create_window(200,100, window=app_label)


# button description
app_label = Label(root, text="remove user from roles, if time in role > 6min ", fg='blue', font=('Arial', 11))
canvas.create_window(200,200, window=app_label)
# button remove roles
remove_roles = Button(root, text='Remove users', command=remove_all_stale_roles)
canvas.create_window(200, 225, window=remove_roles)



# loop
root.mainloop()
