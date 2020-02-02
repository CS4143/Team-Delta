from django.contrib.auth.mixins import LoginRequiredMixin

class StudentRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated \
            or not request.user.is_student \
            or request.user.is_superuser:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)