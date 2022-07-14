from pathlib import Path

import controls


def resource(relative_path):
    return str(
        Path(controls.__file__).parent.parent.joinpath(f'resources/{relative_path}')
    )
