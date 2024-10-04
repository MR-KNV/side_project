import numpy as np
import aligator
import pinocchio as pin
import time

from aligator import (
    manifolds,
    dynamics,
    constraints,
)
from utils import load_talos_no_wristhead, ArgsBase


class Args(ArgsBase):
    tcp: str = None
    bounds: bool = True
    num_threads: int = 8
