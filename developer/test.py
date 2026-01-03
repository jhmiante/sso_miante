import warnings
warnings.filterwarnings('ignore')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "developer.settings")

import django
django.setup()

from sso_miante.models import SsoMiante



id, secrets = SsoMiante.CREATE_HASHS()
print(id, secrets)
sso = SsoMiante.CREATE(id, secrets, 'APP 3')



print(int(16/2))


