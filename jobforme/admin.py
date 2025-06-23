from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'My Custom Admin Site'
    site_title = 'Admin Portal'
    index_title = 'Welcome to My Admin'

admin_site = MyAdminSite(name='myadmin')
