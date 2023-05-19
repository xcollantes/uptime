"""Show uptime of a service."""

import time


def uptime(start_uptime: time.perf_counter) -> str:
    """Return human readable time elapsed since program start.

    Example usage:
    ```
    import time
    start_uptime = time.perf_counter()
    print(uptime(start_uptime))
    ```

    Args:
        start_uptime: A perf_counter object which is equivalent of calling
        now().

    Returns:
        String of time elapsed.
    """
    units = {
        "months": 2629746, "weeks": 604800, "days": 86400,
        "hours": 3600, "minutes": 60, "seconds": 1
    }

    elapsed_sec = time.perf_counter() - start_uptime

    result = ""
    for unit, count in units.items():
        value = int(elapsed_sec // count)
        if value >= 1:
            if value == 1:
                unit = unit.rstrip("s")
            result += f"{value} {unit}, "
            elapsed_sec -= (count * value)
    return result.rstrip(", ")
