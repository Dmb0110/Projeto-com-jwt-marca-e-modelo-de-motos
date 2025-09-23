'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Base  # ← Aqui você importa os modelos
target_metadata = Base.metadata  # ← Aqui você define os metadados

'''

