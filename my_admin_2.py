import admin_and_privileges

my_admin = admin_and_privileges.Admin("karen", "jones", 52, "female")
my_admin.privileges.privileges = [
    "can add post",
    "can delete post",
    "can ban user"
]

my_admin.privileges.show_privileges()