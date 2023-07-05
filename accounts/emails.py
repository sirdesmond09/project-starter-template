from djoser.email import PasswordResetEmail

from config.settings import Common

class CustomPasswordResetEmail(PasswordResetEmail):
    template_name = "email/password_reset.html"

    def get_context_data(self):
        # PasswordResetEmail can be deleted
        context = super().get_context_data()

        user = context.get("user")
        
            
        context["domain"] = self.request.META.get('HTTP_REFERER')
            
        
        return context