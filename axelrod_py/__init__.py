import os

cwd = os.getcwd()
os.chdir(cwd + '/axelrod_py')
os.system("make")
os.chdir(cwd)

from axl_network import *
from axl_agent import *

import random as rand
import matplotlib.pyplot as plt
import numpy as np

