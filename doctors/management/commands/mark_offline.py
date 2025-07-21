from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from doctors.models import DoctorProfile

class Command(BaseCommand):
    help = "Marks inactive doctors as offline"

    def handle(self, *args, **kwargs):
        five_minutes_ago = now() - timedelta(minutes=5)
        DoctorProfile.objects.filter(last_seen__lt=five_minutes_ago).update(is_online=False)
        self.stdout.write(self.style.SUCCESS('Doctors marked offline successfully'))
