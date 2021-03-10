from django.contrib import admin
from .models import Usuario, Disciplina, Professor, UsuarioDisciplina
from django.contrib.auth import admin as auth_admin
from .form import CustomUserCreationForm, CustomUserChangeForm

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['username', 'first_name', 'last_name', 'email', 'status','is_superuser', 'is_active', 'is_staff', ]

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'titulo', 'professor', 'descricao_longa']

class UsuarioDisciplinaAdmin(admin.ModelAdmin):
    list_display = ['id','disciplina', 'status', 'usuario', 'data_reserva', ]


admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Professor)
admin.site.register(UsuarioDisciplina,UsuarioDisciplinaAdmin)









