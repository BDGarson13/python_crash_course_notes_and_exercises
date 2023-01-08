import social_media_classes

my_admin = social_media_classes.Admin("karen", "jones", 52, "female")
my_admin.privileges.privileges = [
    "can add post",
    "can delete post",
    "can ban user"
    ]

my_admin.privileges.show_privileges()
