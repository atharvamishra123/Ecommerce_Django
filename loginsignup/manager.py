from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **other_fields):
        if not email:
            raise ValueError('Enter an email address')
        if not username:
            raise ValueError('Enter a username')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.is_superuser = True
        # user.is_staff = True
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        print(user)
        return user

















    # def create_superuser(self, username, email, password, **other_fields):
    #     other_fields.setdefault('is_staff', False)
    #     other_fields.setdefault('is_superuser', False)
    #     other_fields.setdefault('is_active', True)

    # def create_superuser(self, username, email, password, **other_fields):
    #     if not email:
    #         raise ValueError('Enter an email address')
    #     if not username:
    #         raise ValueError('Enter a username')
    #     email = self.normalize_email(email)
    #     user = self.model(username=username, email=email, password=password, **other_fields)
    #     # user.is_superuser = True
    #     # user.is_staff = False
    #     user.is_admin = True
    #     user.save()