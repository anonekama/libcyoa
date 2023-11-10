import subprocess
import sys

from alembic.config import Config
from alembic import command

from libcyoa.main import ROOT


alembic_cfg = Config(ROOT / "alembic.ini")

subprocess.run([sys.executable, "./libcyoa/backend_pre_start.py"])
command.upgrade(alembic_cfg, "head")
subprocess.run([sys.executable, "./libcyoa/initial_data.py"])