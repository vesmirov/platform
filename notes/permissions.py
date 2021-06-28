from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


class AdminPermission:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied()
