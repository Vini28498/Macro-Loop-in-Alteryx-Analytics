Run Alteryx.help() for info about useful functions.
i.e., Alteryx.read("#1"), Alteryx.write(df,1), Alteryx.getWorkflowConstant("Engine.WorkflowDirectory")

# List all non-standard packages to be imported by your 
# script here (only missing packages will be installed)
from ayx import Package
#Package.installPackages(['pandas','numpy'])

from ayx import Alteryx

df = Alteryx.read("#1")

import time

starting_time = time.time()
final_time = time.time() - starting_time

while final_time < 10:
    final_time = time.time() - starting_time

Alteryx.write(df,1)

