from Lists.admin import Admin

my_admin = Admin('paavan', 'gopala', 'iampaavan', 'bangalore')
my_admin.describe_user()
print(f'*********************************************************************')
my_privileges = ['can reset passwords', 'can moderate discussions', 'can suspend accounts']
my_admin.privileges.privileges = my_privileges
print(f"Admin {my_admin.username} has the following privileges:")
my_admin.privileges.show_privileges()
