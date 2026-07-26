from analysis import analyze_market
from validation import validate_signal


def get_signal():
    """
    Generate and validate a signal.

    Returns None when there is no valid setup.
    """

    signal = analyze_market()
    return validate_signal(signal)
