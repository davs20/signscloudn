class User(AbstractBaseUser, PermissionsMixin):
 email =  models.EmailField(
    verbose_name='email address',
    max_length=255,
    unique=True,
 )
 first_name = models.CharField(max_length=30)
 last_name = models.CharField(max_length=30)

 USERNAME_FIELD = 'email'