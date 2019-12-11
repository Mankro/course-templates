import sys
import os
import random

instance_dir = sys.argv[1]
if not os.path.exists(instance_dir):
    os.makedirs(instance_dir)

# 8 random bytes
data = bytes(random.sample(range(256), 8))

with open(os.path.join(instance_dir, "mydata"), "wb") as f:
    f.write(data)
