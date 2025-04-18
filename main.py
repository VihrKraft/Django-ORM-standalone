import os
from dotenv import load_dotenv
import django


load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    for passcard in passcards:
        active_passcards = Passcard.objects.filter(is_active=True)
print(f"Всего пропусков {Passcard.objects.count()}\nАктивных пропусков {len(active_passcards)}")