from django.contrib.auth.decorators import user_passes_test
def manager_required(view):
    return user_passes_test(lambda u: u.is_authenticated and (u.is_superuser or getattr(getattr(u, 'profile', None), 'role', '') == 'manager'))(view)
