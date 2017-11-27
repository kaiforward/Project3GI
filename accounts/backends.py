from models import User

# overriding 2 of django's default functions authenticate and get_user
# autheticate checks wether users password and email is correct,
# get user checks if the user already exist's or could check user status
# such as a ban.
 
class EmailAuth(object):
 
    def authenticate(self, email=None, password=None):
        """
       Get an instance of User using the supplied email and check its password
       """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
 
        except User.DoesNotExist:
            return None
 
    def get_user(self, user_id):
        """
       Used by the django authentication system to retrieve an instance of User
       """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None