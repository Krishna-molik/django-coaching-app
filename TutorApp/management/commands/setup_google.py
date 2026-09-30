import os
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

class Command(BaseCommand):
    help = "Creates Site + Google SocialApp from environment variables"

    def handle(self, *args, **options):
        domain = os.environ.get("RENDER_EXTERNAL_HOSTNAME", "127.0.0.1:8000")
        site, _ = Site.objects.update_or_create(
            id=1, defaults={"domain": domain, "name": "CareerStar"})

        client_id = os.environ.get("GOOGLE_CLIENT_ID")
        secret = os.environ.get("GOOGLE_CLIENT_SECRET")
        if client_id and secret:
            app, _ = SocialApp.objects.update_or_create(
                provider="google",
                defaults={"name": "Google", "client_id": client_id, "secret": secret})
            app.sites.add(site)
            self.stdout.write(self.style.SUCCESS("Google SocialApp ready"))
        else:
            self.stdout.write(self.style.WARNING("GOOGLE_CLIENT_ID/SECRET missing, skipped"))

        # superuser (for admin panel )
        user = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        pwd = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
        if user and pwd:
            from django.contrib.auth.models import User
            if not User.objects.filter(username=user).exists():
                User.objects.create_superuser(user, os.environ.get("DJANGO_SUPERUSER_EMAIL", ""), pwd)
                self.stdout.write(self.style.SUCCESS("Superuser created"))
