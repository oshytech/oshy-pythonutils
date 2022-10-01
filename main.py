import time

import display_utils as display


def run():
    display.print_info("info works")
    display.print_info("info works bold", True)
    display.print_success("Print success")
    display.print_success("Print success bold", True)
    display.print_warning("Print warning")
    display.print_warning("Print warning bold", True)
    display.print_error("Print error")
    display.print_error("Print error bold", True)

    n = 100
    for i in range(n +1 ):
        time.sleep(0.1)
        display.print_info(display.progress_bar(i, n, 30), end="\r")


if __name__ == "__main__":
    run()
