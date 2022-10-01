class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def color_message(color, message, colorend=bcolors.ENDC, bold=False):
    if bold:
        return bcolors.BOLD + color_message(color, message, colorend, False)

    return color + message + colorend


def print_color(color, message, colorend=bcolors.ENDC, bold=False, end="\n"):
    print(color_message(color, message, colorend, bold=bold), end=end)


def print_info(message, bold=False, end="\n"):
    print_color(bcolors.OKBLUE, message, bold=bold, end=end)


def print_success(message, bold=False):
    print_color(bcolors.OKGREEN, message, bold=bold)


def print_warning(message, bold=False):
    print_color(bcolors.WARNING, message, bold=bold)


def print_error(message, bold=False):
    print_color(bcolors.FAIL, message, bold=bold)


def progress_bar(part, total, length=100):
    frac = part / total
    completed = int(frac * length)
    missing = length - completed
    bar = f"[{'#' * completed}{'-' * missing}] {frac:.2%}"
    return bar
