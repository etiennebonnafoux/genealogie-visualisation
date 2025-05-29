import re


def dms_to_dd(dms_str: str) -> float:
    """Converts degrees, minutes, seconds string to decimal degrees."""
    parts = re.split("[°'\"]", dms_str)
    degrees = int(parts[0]) if parts[0].isdigit() else round(float(parts[0]))
    minutes = (
        int(parts[1]) if len(parts) > 1 and parts[1] and parts[1].isnumeric() else 0
    )
    seconds = (
        float(parts[2])
        if len(parts) > 2 and parts[2] and parts[2].strip().isnumeric()
        else 0
    )
    direction = parts[-1].strip()

    dd = degrees + minutes / 60 + seconds / 3600
    if direction in ["W", "S"]:
        dd *= -1
    return dd
