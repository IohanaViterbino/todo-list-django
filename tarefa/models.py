from django.db import models
from django.conf import settings
from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin

class UserManager(UserManager):
    def create_user(self, email, username, cpf, password=None, **extra_fields):
        """
        Cria e salva um usuário com o email, nome de usuário, cpf e senha fornecidos.
        """
        if not email:
            raise ValueError('O campo Email deve ser preenchido')
        if not cpf:
            raise ValueError('O campo CPF deve ser preenchido')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, cpf, password=None, **extra_fields):
        """
        Cria e salva um superusuário com o email, nome de usuário, cpf e senha fornecidos.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário precisa ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário precisa ter is_superuser=True.')

        return self.create_user(email, username, cpf, password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
    cpf = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf']

    objects = UserManager()

class Task(models.Model):
    CATEGORY_NAME = (
        ('I', 'Inicializado'),
        ('E', 'Em Andamento'),
        ('F', 'Finalizado'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField(null=True, blank=True)
    # data de vencimento da tarefa
    due_date = models.DateField(null=True, blank=True) 
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    fk_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    category = models.CharField(max_length=1, choices=CATEGORY_NAME, default='I', null=False, blank=False)

    def __str__(self):
        return self.title

    # Método para retornar as tags associadas como uma string separada por vírgulas
    def get_tags(self):
        return ", ".join([tag.tag_name for tag in self.tags.all()])
    get_tags.short_description = 'Tags' 

class Tag(models.Model):
    tag_name = models.CharField(max_length=70)
    tasks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tags')

    def __str__(self):
        return self.tag_name
    
class Comment(models.Model):
    comment_text = models.TextField(blank=True, null=True)
    fk_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    fk_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
  
class Notification(models.Model):
    fk_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    notification_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Attachment(models.Model):
    attachment_name = models.CharField(null=False, max_length=100)
    fk_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')
    fk_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attachments')
    attachment = models.FileField(upload_to='attachments/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.attachment_name