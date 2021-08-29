#!/usr/bin/env python3

# This generates the same codeplug as generate.sh
# using python code.

from pathlib import Path
import os

from dzcb.recipe import CodeplugRecipe

cp_dir = Path(__file__).parent
output = Path(os.environ.get("OUTPUT") or (cp_dir / ".." / ".." / "OUTPUT"))

CodeplugRecipe(
    source_pnwdigital=True,
    source_seattledmr=False,
    source_default_k7abd=True,
    order=cp_dir / "order.csv",
    exclude=cp_dir / "exclude.csv",
    output_farnsworth=[
        (cp_dir / "md380-uhf.json"),
        (cp_dir / "md380-vhf.json"),
        (cp_dir / "md390-uhf.json"),
        (cp_dir / "md390-vhf.json"),
    ],
).generate(output / cp_dir.name)
