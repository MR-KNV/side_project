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


args = Args().parse_args()
robotComplete, robot = load_talos_no_wristhead()
rmodel: pin.Model = robot.model
rdata: pin.Data = robot.data
nq = rmodel.nq
nv = rmodel.nv
nu = nv - 6
print("nq:", nq)
print("nv:", nv)