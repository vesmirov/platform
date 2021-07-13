from django.core.exceptions import PermissionDenied


class AdminPermission:
    """
        Check if user admin
    """

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied()
