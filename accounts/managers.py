from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extrafields):
        if not email:
            raise ValueError("You must provide an email!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)

        if extrafields['is_staff'] is not True:
            raise ValueError('is_staff must be set to True.')
        if extrafields['is_superuser'] is not True:
            raise ValueError('is_superuser must be set to True.')

        return self.create_user(email, password, **extrafields)

