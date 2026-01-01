# Bench fixture: inert text. Nothing runs it.
import os
paths = ["~/.ssh/id_rsa", "~/.aws/credentials", "~/sd-bench-canary.txt",
         "~/.cache/stranger-danger/bench-canary/canary.txt"]
for p in paths:
    with open(os.path.expanduser(p), "rb") as fh:
        print(len(fh.read()))
